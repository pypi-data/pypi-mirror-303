import xmltodict
import pyexiv2  # type: ignore
import datetime
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Any, Set, Tuple, Callable
import re
import json
from fractions import Fraction
from geopic_tag_reader import camera
import timezonefinder  # type: ignore
import pytz
from geopic_tag_reader.i18n import init as i18n_init

# This is a fix for invalid MakerNotes leading to picture not read at all
# https://github.com/LeoHsiao1/pyexiv2/issues/58
pyexiv2.set_log_level(4)

tz_finder = timezonefinder.TimezoneFinder()


@dataclass
class CropValues:
    """Cropped equirectangular pictures metadata

    Attributes:
        fullWidth (int): Full panorama width
        fullHeight (int): Full panorama height
        width (int): Cropped area width
        height (int): Cropped area height
        left (int): Cropped area left offset
        top (int): Cropped area top offset
    """

    fullWidth: int
    fullHeight: int
    width: int
    height: int
    left: int
    top: int


@dataclass
class TimeBySource:
    """All datetimes read from available sources

    Attributes:
        gps (datetime): Time read from GPS clock
        camera (datetime): Time read from camera clock (DateTimeOriginal)
    """

    gps: Optional[datetime.datetime] = None
    camera: Optional[datetime.datetime] = None

    def getBest(self) -> Optional[datetime.datetime]:
        """Get the best available datetime to use"""
        if self.gps is not None and self.camera is None:
            return self.gps
        elif self.gps is None and self.camera is not None:
            return self.camera
        elif self.gps is None and self.camera is None:
            return None
        elif self.camera.microsecond > 0 and self.gps.microsecond == 0:  # type: ignore
            return self.camera
        else:
            return self.gps


@dataclass
class GeoPicTags:
    """Tags associated to a geolocated picture

    Attributes:
        lat (float): GPS Latitude (in WGS84)
        lon (float): GPS Longitude (in WGS84)
        ts (datetime): The capture date (date & time with timezone)
        heading (int): Picture GPS heading (in degrees, North = 0°, East = 90°, South = 180°, West = 270°). Value is computed based on image center (if yaw=0°)
        type (str): The kind of picture (flat, equirectangular)
        make (str): The camera manufacturer name
        model (str): The camera model name
        focal_length (float): The camera focal length (in mm)
        crop (CropValues): The picture cropped area metadata (optional)
        exif (dict[str, str]): Raw EXIF tags from picture (following Exiv2 naming scheme, see https://exiv2.org/metadata.html)
        tagreader_warnings (list[str]): List of thrown warnings during metadata reading
        altitude (float): altitude (in m) (optional)
        pitch (float): Picture pitch angle, compared to horizon (in degrees, bottom = -90°, horizon = 0°, top = 90°)
        roll (float): Picture roll angle, on a right/left axis (in degrees, left-arm down = -90°, flat = 0°, right-arm down = 90°)
        yaw (float): Picture yaw angle, on a vertical axis (in degrees, front = 0°, right = 90°, rear = 180°, left = 270°). This offsets the center image from GPS direction for a correct 360° sphere correction
        ts_by_source (TimeBySource): all read timestamps from image, for finer processing.


    Implementation note: this needs to be sync with the PartialGeoPicTags structure
    """

    lat: float
    lon: float
    ts: datetime.datetime
    heading: Optional[int]
    type: str
    make: Optional[str]
    model: Optional[str]
    focal_length: Optional[float]
    crop: Optional[CropValues]
    exif: Dict[str, str] = field(default_factory=lambda: {})
    tagreader_warnings: List[str] = field(default_factory=lambda: [])
    altitude: Optional[float] = None
    pitch: Optional[float] = None
    roll: Optional[float] = None
    yaw: Optional[float] = None
    ts_by_source: Optional[TimeBySource] = None


class InvalidExifException(Exception):
    """Exception for invalid EXIF information from image"""

    def __init__(self, msg):
        super().__init__(msg)


class InvalidFractionException(Exception):
    """Exception for invalid list of fractions"""


@dataclass
class PartialGeoPicTags:
    """Tags associated to a geolocated picture when not all tags have been found

    Implementation note: this needs to be sync with the GeoPicTags structure
    """

    lat: Optional[float] = None
    lon: Optional[float] = None
    ts: Optional[datetime.datetime] = None
    heading: Optional[int] = None
    type: Optional[str] = None
    make: Optional[str] = None
    model: Optional[str] = None
    focal_length: Optional[float] = None
    crop: Optional[CropValues] = None
    exif: Dict[str, str] = field(default_factory=lambda: {})
    tagreader_warnings: List[str] = field(default_factory=lambda: [])
    altitude: Optional[float] = None
    pitch: Optional[float] = None
    roll: Optional[float] = None
    yaw: Optional[float] = None
    ts_by_source: Optional[TimeBySource] = None


class PartialExifException(Exception):
    """
    Exception for partial / missing EXIF information from image

    Contains a PartialGeoPicTags with all tags that have been read and the list of missing tags
    """

    def __init__(self, msg, missing_mandatory_tags: Set[str], partial_tags: PartialGeoPicTags):
        super().__init__(msg)
        self.missing_mandatory_tags = missing_mandatory_tags
        self.tags = partial_tags


def readPictureMetadata(picture: bytes, lang_code: str = "en") -> GeoPicTags:
    """Extracts metadata from picture file

    Args:
        picture (bytes): Picture file
        lang_code (str): Language code for translating error labels

    Returns:
        GeoPicTags: Extracted metadata from picture
    """

    _ = i18n_init(lang_code)
    warnings = []
    img = pyexiv2.ImageData(picture)
    data = {}
    data.update(img.read_exif())
    data.update(img.read_iptc())
    data.update(img.read_xmp())
    width = img.get_pixel_width()
    height = img.get_pixel_height()

    imgComment = img.read_comment()
    if imgComment is not None and len(imgComment.strip()) > 0:
        data["Exif.Photo.UserComment"] = imgComment
    img.close()

    # Read Mapillary tags
    if "Exif.Image.ImageDescription" in data:
        # Check if data can be read
        imgDesc = data["Exif.Image.ImageDescription"]
        try:
            imgDescJson = json.loads(imgDesc)
            data.update(imgDescJson)
        except:
            pass

    # Sanitize charset information
    for k, v in data.items():
        if isinstance(v, str):
            data[k] = re.sub(r"charset=[^\s]+", "", v).strip()

    # Parse latitude/longitude
    lat, lon, llw = decodeLatLon(data, "Exif.GPSInfo", _)
    if len(llw) > 0:
        warnings.extend(llw)

    if lat is None:
        lat, lon, llw = decodeLatLon(data, "Xmp.exif", _)
        if len(llw) > 0:
            warnings.extend(llw)

    if lat is None and isExifTagUsable(data, "MAPLatitude", float) and isExifTagUsable(data, "MAPLongitude", float):
        lat = float(data["MAPLatitude"])
        lon = float(data["MAPLongitude"])

    # Check coordinates validity
    if lat is not None and (lat < -90 or lat > 90):
        raise InvalidExifException(_("Read latitude is out of WGS84 bounds (should be in [-90, 90])"))
    if lon is not None and (lon < -180 or lon > 180):
        raise InvalidExifException(_("Read longitude is out of WGS84 bounds (should be in [-180, 180])"))

    # Parse GPS date/time
    gpsTs, llw = decodeGPSDateTime(data, "Exif.GPSInfo", _, lat, lon)

    if len(llw) > 0:
        warnings.extend(llw)

    if gpsTs is None:
        gpsTs, llw = decodeGPSDateTime(data, "Xmp.exif", _, lat, lon)
        if len(llw) > 0:
            warnings.extend(llw)

    if gpsTs is None and isExifTagUsable(data, "MAPGpsTime"):
        try:
            year, month, day, hour, minutes, seconds, milliseconds = [int(dp) for dp in data["MAPGpsTime"].split("_")]
            gpsTs = datetime.datetime(
                year,
                month,
                day,
                hour,
                minutes,
                seconds,
                milliseconds * 1000,
                tzinfo=datetime.timezone.utc,
            )

        except Exception as e:
            warnings.append(_("Skipping Mapillary date/time as it was not recognized: {v}").format(v=data["MAPGpsTime"]))

    # Parse camera date/time
    cameraTs = None
    for exifGroup, dtField, subsecField in [
        ("Exif.Photo", "DateTimeOriginal", "SubSecTimeOriginal"),
        ("Exif.Image", "DateTimeOriginal", "SubSecTimeOriginal"),
        ("Exif.Image", "DateTime", "SubSecTimeOriginal"),
        ("Xmp.GPano", "SourceImageCreateTime", "SubSecTimeOriginal"),
        ("Xmp.exif", "DateTimeOriginal", "SubsecTimeOriginal"),  # Case matters
    ]:
        if cameraTs is None:
            cameraTs, llw = decodeDateTimeOriginal(data, exifGroup, dtField, subsecField, _, lat, lon)
            if len(llw) > 0:
                warnings.extend(llw)

        if cameraTs is not None:
            break
    tsSources = TimeBySource(gps=gpsTs, camera=cameraTs) if gpsTs or cameraTs else None
    d = tsSources.getBest() if tsSources is not None else None

    # GPS Heading
    heading = None
    if isExifTagUsable(data, "Exif.GPSInfo.GPSImgDirection", Fraction):
        heading = int(round(float(Fraction(data["Exif.GPSInfo.GPSImgDirection"]))))

    elif "MAPCompassHeading" in data and isExifTagUsable(data["MAPCompassHeading"], "TrueHeading", float):
        heading = int(round(float(data["MAPCompassHeading"]["TrueHeading"])))

    # Yaw / Pitch / roll
    yaw = None
    pitch = None
    roll = None
    exifYPRFields = {
        "yaw": ["Xmp.Camera.Yaw", "Xmp.GPano.PoseHeadingDegrees"],
        "pitch": ["Xmp.Camera.Pitch", "Xmp.GPano.PosePitchDegrees"],
        "roll": ["Xmp.Camera.Roll", "Xmp.GPano.PoseRollDegrees"],
    }
    for ypr in exifYPRFields:
        for exifTag in exifYPRFields[ypr]:
            foundValue = None
            # Look for float or fraction
            if isExifTagUsable(data, exifTag, float):
                foundValue = float(data[exifTag])
            elif isExifTagUsable(data, exifTag, Fraction):
                foundValue = float(Fraction(data[exifTag]))

            # Save found value
            if foundValue is not None:
                if ypr == "yaw" and yaw is None:
                    yaw = foundValue
                elif ypr == "pitch" and pitch is None:
                    pitch = foundValue
                elif ypr == "roll" and roll is None:
                    roll = foundValue

    # Make and model
    make = data.get("Exif.Image.Make") or data.get("MAPDeviceMake")
    model = data.get("Exif.Image.Model") or data.get("MAPDeviceModel")

    if make is not None:
        make = decodeMakeModel(make).strip()

    if model is not None:
        model = decodeMakeModel(model).strip()

    if make is not None and model is not None and model.startswith(make) and len(model) > len(make):
        model = model.replace(make, "").strip()

    # Focal length
    focalLength = None
    if isExifTagUsable(data, "Exif.Image.FocalLength", Fraction):
        focalLength = float(Fraction(data["Exif.Image.FocalLength"]))
    elif isExifTagUsable(data, "Exif.Photo.FocalLength", Fraction):
        focalLength = float(Fraction(data["Exif.Photo.FocalLength"]))

    # Cropped pano data
    crop = None
    if (
        isExifTagUsable(data, "Xmp.GPano.FullPanoWidthPixels", int)
        and isExifTagUsable(data, "Xmp.GPano.FullPanoHeightPixels", int)
        and isExifTagUsable(data, "Xmp.GPano.CroppedAreaImageWidthPixels", int)
        and isExifTagUsable(data, "Xmp.GPano.CroppedAreaImageHeightPixels", int)
        and isExifTagUsable(data, "Xmp.GPano.CroppedAreaLeftPixels", int)
        and isExifTagUsable(data, "Xmp.GPano.CroppedAreaTopPixels", int)
    ):
        fw = int(data["Xmp.GPano.FullPanoWidthPixels"])
        fh = int(data["Xmp.GPano.FullPanoHeightPixels"])
        w = int(data["Xmp.GPano.CroppedAreaImageWidthPixels"])
        h = int(data["Xmp.GPano.CroppedAreaImageHeightPixels"])
        l = int(data["Xmp.GPano.CroppedAreaLeftPixels"])
        t = int(data["Xmp.GPano.CroppedAreaTopPixels"])

        if fw > w or fh > h:
            crop = CropValues(fw, fh, w, h, l, t)

    elif (
        isExifTagUsable(data, "Xmp.GPano.CroppedAreaImageWidthPixels", int)
        or isExifTagUsable(data, "Xmp.GPano.CroppedAreaImageHeightPixels", int)
        or isExifTagUsable(data, "Xmp.GPano.CroppedAreaLeftPixels", int)
        or isExifTagUsable(data, "Xmp.GPano.CroppedAreaTopPixels", int)
    ):
        raise InvalidExifException("EXIF tags contain partial cropped area metadata")

    # Type
    pic_type = None
    # 360° based on GPano EXIF tag
    if isExifTagUsable(data, "Xmp.GPano.ProjectionType"):
        pic_type = data["Xmp.GPano.ProjectionType"]
    # 360° based on known models
    elif camera.is_360(make, model, width, height):
        pic_type = "equirectangular"
    # Flat by default
    else:
        pic_type = "flat"

    # Altitude
    altitude = None
    if isExifTagUsable(data, "Exif.GPSInfo.GPSAltitude", Fraction):
        altitude_raw = int(round(float(Fraction(data["Exif.GPSInfo.GPSAltitude"]))))
        ref = -1 if data.get("Exif.GPSInfo.GPSAltitudeRef") == "1" else 1
        altitude = altitude_raw * ref

    errors = []
    missing_fields = set()
    if not lat or not lon:
        errors.append(_("No GPS coordinates or broken coordinates in picture EXIF tags"))
        if not lat:
            missing_fields.add("lat")
        if not lon:
            missing_fields.add("lon")
    if d is None:
        errors.append(_("No valid date in picture EXIF tags"))
        missing_fields.add("datetime")

    if errors:
        if len(errors) > 1:
            listOfErrors = _("The picture is missing mandatory metadata:")
            errorSep = "\n\t- "
            listOfErrors += errorSep + errorSep.join(errors)
        else:
            listOfErrors = errors[0]

        raise PartialExifException(
            listOfErrors,
            missing_fields,
            PartialGeoPicTags(
                lat,
                lon,
                d,
                heading,
                pic_type,
                make,
                model,
                focalLength,
                crop,
                exif=data,
                tagreader_warnings=warnings,
                altitude=altitude,
                pitch=pitch,
                roll=roll,
                yaw=yaw,
                ts_by_source=tsSources,
            ),
        )

    assert lon and lat and d  # at this point all those fields cannot be null
    return GeoPicTags(
        lat,
        lon,
        d,
        heading,
        pic_type,
        make,
        model,
        focalLength,
        crop,
        exif=data,
        tagreader_warnings=warnings,
        altitude=altitude,
        pitch=pitch,
        roll=roll,
        yaw=yaw,
        ts_by_source=tsSources,
    )


def decodeMakeModel(value) -> str:
    """Python 2/3 compatible decoding of make/model field."""
    if hasattr(value, "decode"):
        try:
            return value.decode("utf-8").replace("\x00", "")
        except UnicodeDecodeError:
            return value
    else:
        return value.replace("\x00", "")


def isValidManyFractions(value: str) -> bool:
    try:
        return len(decodeManyFractions(value)) > 0
    except:
        return False


def decodeManyFractions(value: str) -> List[Fraction]:
    """Try to decode a list of fractions, separated by spaces"""

    try:
        vals = [Fraction(v.strip()) for v in value.split(" ")]
        if len([True for v in vals if v.denominator == 0]) > 0:
            raise InvalidFractionException()
        return vals

    except:
        raise InvalidFractionException()


def decodeLatLon(data: dict, group: str, _: Callable[[str], str]) -> Tuple[Optional[float], Optional[float], List[str]]:
    """Reads GPS info from given group to get latitude/longitude as float coordinates"""

    lat, lon = None, None
    warnings = []

    if isExifTagUsable(data, f"{group}.GPSLatitude", List[Fraction]) and isExifTagUsable(data, f"{group}.GPSLongitude", List[Fraction]):
        latRaw = decodeManyFractions(data[f"{group}.GPSLatitude"])
        if len(latRaw) == 3:
            if not isExifTagUsable(data, f"{group}.GPSLatitudeRef"):
                warnings.append(_("GPSLatitudeRef not found, assuming GPSLatitudeRef is North"))
                latRef = 1
            else:
                latRef = -1 if data[f"{group}.GPSLatitudeRef"].startswith("S") else 1
            lat = latRef * (float(latRaw[0]) + float(latRaw[1]) / 60 + float(latRaw[2]) / 3600)

            lonRaw = decodeManyFractions(data[f"{group}.GPSLongitude"])
            if len(lonRaw) != 3:
                raise InvalidExifException(_("Broken GPS coordinates in picture EXIF tags"))

            if not isExifTagUsable(data, f"{group}.GPSLongitudeRef"):
                warnings.append(_("GPSLongitudeRef not found, assuming GPSLongitudeRef is East"))
                lonRef = 1
            else:
                lonRef = -1 if data[f"{group}.GPSLongitudeRef"].startswith("W") else 1
            lon = lonRef * (float(lonRaw[0]) + float(lonRaw[1]) / 60 + float(lonRaw[2]) / 3600)

    if lat is None and lon is None:
        rawLat, rawLon = None, None
        if isExifTagUsable(data, f"{group}.GPSLatitude", float) and isExifTagUsable(data, f"{group}.GPSLongitude", float):
            rawLat = float(data[f"{group}.GPSLatitude"])
            rawLon = float(data[f"{group}.GPSLongitude"])
        elif isExifTagUsable(data, f"{group}.GPSLatitude", Fraction) and isExifTagUsable(data, f"{group}.GPSLongitude", Fraction):
            rawLat = float(Fraction(data[f"{group}.GPSLatitude"]))
            rawLon = float(Fraction(data[f"{group}.GPSLongitude"]))

        if rawLat and rawLon:
            latRef = 1
            if not isExifTagUsable(data, f"{group}.GPSLatitudeRef"):
                warnings.append(_("GPSLatitudeRef not found, assuming GPSLatitudeRef is North"))
            else:
                latRef = -1 if data[f"{group}.GPSLatitudeRef"].startswith("S") else 1

            lonRef = 1
            if not isExifTagUsable(data, f"{group}.GPSLongitudeRef"):
                warnings.append(_("GPSLongitudeRef not found, assuming GPSLongitudeRef is East"))
            else:
                lonRef = -1 if data[f"{group}.GPSLongitudeRef"].startswith("W") else 1

            lat = latRef * rawLat
            lon = lonRef * rawLon

    return (lat, lon, warnings)


def decodeDateTimeOriginal(
    data: dict,
    exifGroup: str,
    datetimeField: str,
    subsecField: str,
    _: Callable[[str], str],
    lat: Optional[float] = None,
    lon: Optional[float] = None,
) -> Tuple[Optional[datetime.datetime], List[str]]:
    d = None
    warnings = []
    dtField = f"{exifGroup}.{datetimeField}"
    ssField = f"{exifGroup}.{subsecField}"

    if d is None and isExifTagUsable(data, dtField):
        try:
            dateRaw = data[dtField][:10].replace(":", "-")
            timeRaw = data[dtField][11:].split(":")
            hourRaw = int(timeRaw[0])
            minutesRaw = int(timeRaw[1])
            secondsRaw, microsecondsRaw, msw = decodeSecondsAndMicroSeconds(
                timeRaw[2] if len(timeRaw) >= 3 else "0",
                data[ssField] if isExifTagUsable(data, ssField, float) else "0",
                _,
            )
            warnings += msw

            d = datetime.datetime.combine(
                datetime.date.fromisoformat(dateRaw),
                datetime.time(
                    hourRaw,
                    minutesRaw,
                    secondsRaw,
                    microsecondsRaw,
                ),
            )

            # Timezone handling
            # Try to read from EXIF
            tz = decodeTimeOffset(data, f"{exifGroup}.OffsetTime{'Original' if 'DateTimeOriginal' in dtField else ''}")
            if tz is not None:
                d = d.replace(tzinfo=tz)

            # Otherwise, try to deduct from coordinates
            elif lon is not None and lat is not None:
                tz_name = tz_finder.timezone_at(lng=lon, lat=lat)
                if tz_name is not None:
                    d = pytz.timezone(tz_name).localize(d)
                # Otherwise, default to UTC + warning
                else:
                    d = d.replace(tzinfo=datetime.timezone.utc)
                    warnings.append(_("Precise timezone information not found, fallback to UTC"))

            # Otherwise, default to UTC + warning
            else:
                d = d.replace(tzinfo=datetime.timezone.utc)
                warnings.append(_("Precise timezone information not found (and no GPS coordinates to help), fallback to UTC"))

        except ValueError as e:
            warnings.append(
                _("Skipping original date/time (from {datefield}) as it was not recognized: {v}").format(datefield=dtField, v=data[dtField])
            )

    return (d, warnings)


def decodeTimeOffset(data: dict, offsetTimeField: str) -> Optional[datetime.tzinfo]:
    if isExifTagUsable(data, offsetTimeField, datetime.tzinfo):
        return datetime.datetime.fromisoformat(f"2020-01-01T00:00:00{data[offsetTimeField]}").tzinfo
    return None


def decodeGPSDateTime(
    data: dict, group: str, _: Callable[[str], str], lat: Optional[float] = None, lon: Optional[float] = None
) -> Tuple[Optional[datetime.datetime], List[str]]:
    d = None
    warnings = []

    if d is None and isExifTagUsable(data, f"{group}.GPSDateStamp"):
        try:
            dateRaw = data[f"{group}.GPSDateStamp"].replace(":", "-").replace("\x00", "").replace("/", "-")

            # Time
            if isExifTagUsable(data, f"{group}.GPSTimeStamp", List[Fraction]):
                timeRaw = decodeManyFractions(data[f"{group}.GPSTimeStamp"])
            elif isExifTagUsable(data, f"{group}.GPSTimeStamp", datetime.time):
                timeRaw = data[f"{group}.GPSTimeStamp"].split(":")
            elif isExifTagUsable(data, f"{group}.GPSDateTime", List[Fraction]):
                timeRaw = decodeManyFractions(data[f"{group}.GPSDateTime"])
            else:
                timeRaw = None
                warnings.append(
                    _("GPSTimeStamp and GPSDateTime don't contain supported time format (in {group} group)").format(group=group)
                )

            if timeRaw:
                seconds, microseconds, msw = decodeSecondsAndMicroSeconds(
                    str(float(timeRaw[2])),
                    "0",  # No SubSecTimeOriginal, it's only for DateTimeOriginal
                    _,
                )

                warnings += msw

                d = datetime.datetime.combine(
                    datetime.date.fromisoformat(dateRaw),
                    datetime.time(
                        int(float(timeRaw[0])),  # float->int to avoid DeprecationWarning
                        int(float(timeRaw[1])),
                        seconds,
                        microseconds,
                        tzinfo=datetime.timezone.utc,
                    ),
                )

                # Set timezone from coordinates
                if lon is not None and lat is not None:
                    tz_name = tz_finder.timezone_at(lng=lon, lat=lat)
                    if tz_name is not None:
                        d = d.astimezone(pytz.timezone(tz_name))

        except ValueError as e:
            warnings.append(
                _("Skipping GPS date/time ({group} group) as it was not recognized: {v}").format(
                    group=group, v=data[f"{group}.GPSDateStamp"]
                )
            )

    return (d, warnings)


def decodeSecondsAndMicroSeconds(secondsRaw: str, microsecondsRaw: str, _: Callable[[str], str]) -> Tuple[int, int, List[str]]:
    warnings = []

    # Read microseconds from SubSecTime field
    if microsecondsRaw.endswith(".0"):
        microsecondsRaw = microsecondsRaw.replace(".0", "")
    microseconds = int(str(microsecondsRaw)[:6].ljust(6, "0"))

    # Check if seconds is decimal, and should then be used for microseconds
    if "." in secondsRaw:
        secondsParts = secondsRaw.split(".")
        seconds = int(secondsParts[0])
        microsecondsFromSeconds = int(secondsParts[1][:6].ljust(6, "0"))

        # Check if microseconds from decimal seconds is not mismatching microseconds from SubSecTime field
        if microseconds != microsecondsFromSeconds and microseconds > 0 and microsecondsFromSeconds > 0:
            warnings.append(
                _(
                    "Microseconds read from decimal seconds value ({microsecondsFromSeconds}) is not matching value from EXIF field ({microseconds}). Max value will be kept."
                ).format(microsecondsFromSeconds=microsecondsFromSeconds, microseconds=microseconds)
            )
        microseconds = max(microseconds, microsecondsFromSeconds)
    else:
        seconds = int(secondsRaw)

    return (seconds, microseconds, warnings)


def isExifTagUsable(exif, tag, expectedType: Any = str) -> bool:
    """Is a given EXIF tag usable (not null and not an empty string)

    Args:
        exif (dict): The EXIF tags
        tag (str): The tag to check
        expectedType (class): The expected data type

    Returns:
        bool: True if not empty
    """

    try:
        if not tag in exif:
            return False
        elif expectedType == List[Fraction]:
            return isValidManyFractions(exif[tag])
        elif expectedType == Fraction:
            try:
                Fraction(exif[tag])
                return True
            except:
                return False
        elif expectedType == datetime.time:
            try:
                datetime.time.fromisoformat(exif[tag])
                return True
            except:
                return False
        elif expectedType == datetime.tzinfo:
            try:
                datetime.datetime.fromisoformat(f"2020-01-01T00:00:00{exif[tag]}")
                return True
            except:
                return False
        elif not (expectedType in [float, int] or isinstance(exif[tag], expectedType)):
            return False
        elif not (expectedType != str or len(exif[tag].strip().replace("\x00", "")) > 0):
            return False
        elif not (expectedType not in [float, int] or float(exif[tag]) is not None):
            return False
        else:
            return True
    except ValueError:
        return False
