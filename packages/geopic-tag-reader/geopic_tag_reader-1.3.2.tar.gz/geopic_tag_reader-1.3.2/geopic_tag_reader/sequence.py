from dataclasses import dataclass
from enum import Enum
from typing import Optional, List, Tuple
from pathlib import PurePath
from geopic_tag_reader.reader import GeoPicTags
import datetime
import math


class SortMethod(str, Enum):
    filename_asc = "filename-asc"
    filename_desc = "filename-desc"
    time_asc = "time-asc"
    time_desc = "time-desc"


@dataclass
class MergeParams:
    maxDistance: Optional[float] = None
    maxRotationAngle: Optional[int] = None

    def is_merge_needed(self):
        # Only check max distance, as max rotation angle is only useful when dist is defined
        return self.maxDistance is not None


@dataclass
class SplitParams:
    maxDistance: Optional[int] = None
    maxTime: Optional[int] = None

    def is_split_needed(self):
        return self.maxDistance is not None or self.maxTime is not None


@dataclass
class Picture:
    filename: str
    metadata: GeoPicTags

    def distance_to(self, other) -> float:
        """Computes distance in meters based on Haversine formula"""
        R = 6371000
        phi1 = math.radians(self.metadata.lat)
        phi2 = math.radians(other.metadata.lat)
        delta_phi = math.radians(other.metadata.lat - self.metadata.lat)
        delta_lambda = math.radians(other.metadata.lon - self.metadata.lon)
        a = math.sin(delta_phi / 2.0) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2.0) ** 2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        distance = R * c
        return distance


class SplitReason(str, Enum):
    time = "time"
    distance = "distance"


@dataclass
class Split:
    prevPic: Picture
    nextPic: Picture
    reason: SplitReason


@dataclass
class Sequence:
    pictures: List[Picture]

    def from_ts(self) -> Optional[datetime.datetime]:
        """Start date/time of this sequence"""

        if len(self.pictures) == 0:
            return None
        return self.pictures[0].metadata.ts

    def to_ts(self) -> Optional[datetime.datetime]:
        """End date/time of this sequence"""

        if len(self.pictures) == 0:
            return None
        return self.pictures[-1].metadata.ts

    def delta_with(self, otherSeq) -> Optional[Tuple[datetime.timedelta, float]]:
        """
        Delta between the end of this sequence and the start of the other one.
        Returns a tuple (timedelta, distance in meters)
        """

        if len(self.pictures) == 0 or len(otherSeq.pictures) == 0:
            return None

        return (otherSeq.from_ts() - self.to_ts(), otherSeq.pictures[0].distance_to(self.pictures[-1]))  # type: ignore


@dataclass
class DispatchReport:
    sequences: List[Sequence]
    duplicate_pictures: Optional[List[Picture]] = None
    sequences_splits: Optional[List[Split]] = None


def sort_pictures(pictures: List[Picture], method: Optional[SortMethod] = SortMethod.time_asc) -> List[Picture]:
    """Sorts pictures according to given strategy

    Parameters
    ----------
    pictures : Picture[]
        List of pictures to sort
    method : SortMethod
        Sort logic to adopt (time-asc, time-desc, filename-asc, filename-desc)

    Returns
    -------
    Picture[]
        List of pictures, sorted
    """

    if method is None:
        method = SortMethod.time_asc

    if method not in [item.value for item in SortMethod]:
        raise Exception("Invalid sort strategy: " + str(method))

    # Get the sort logic
    strat, order = method.split("-")

    # Sort based on filename
    if strat == "filename":
        # Check if pictures can be sorted by numeric notation
        hasNonNumber = False
        for p in pictures:
            try:
                int(PurePath(p.filename or "").stem)
            except:
                hasNonNumber = True
                break

        def sort_fct(p):
            return PurePath(p.filename or "").stem if hasNonNumber else int(PurePath(p.filename or "").stem)

        pictures.sort(key=sort_fct)

    # Sort based on picture ts
    elif strat == "time":
        # Check if all pictures have GPS ts set
        missingGpsTs = next(
            (p for p in pictures if p.metadata is None or p.metadata.ts_by_source is None or p.metadata.ts_by_source.gps is None), None
        )
        if missingGpsTs:
            # Check if all pictures have camera ts set
            missingCamTs = next(
                (p for p in pictures if p.metadata is None or p.metadata.ts_by_source is None or p.metadata.ts_by_source.camera is None),
                None,
            )
            # Sort by best ts available
            if missingCamTs:
                pictures.sort(key=lambda p: p.metadata.ts.isoformat() if p.metadata is not None else "0000-00-00T00:00:00Z")
            # Sort by camera ts
            else:
                pictures.sort(
                    key=lambda p: (
                        p.metadata.ts_by_source.camera.isoformat(),  # type: ignore
                        p.metadata.ts_by_source.gps.isoformat() if p.metadata.ts_by_source.gps else "0000-00-00T00:00:00Z",  # type: ignore
                    )
                )
        # Sort by GPS ts
        else:
            pictures.sort(
                key=lambda p: (
                    p.metadata.ts_by_source.gps.isoformat(),  # type: ignore
                    p.metadata.ts_by_source.camera.isoformat() if p.metadata.ts_by_source.camera else "0000-00-00T00:00:00Z",  # type: ignore
                )
            )

    if order == "desc":
        pictures.reverse()

    return pictures


def find_duplicates(pictures: List[Picture], params: Optional[MergeParams] = None) -> Tuple[List[Picture], List[Picture]]:
    """
    Finds too similar pictures.
    Note that input list should be properly sorted.

    Parameters
    ----------
    pictures : list of sorted pictures to check
    params : parameters used to consider two pictures as a duplicate

    Returns
    -------
    (Non-duplicates pictures, Duplicates pictures)
    """

    if params is None or not params.is_merge_needed():
        return (pictures, [])

    nonDups: List[Picture] = []
    dups: List[Picture] = []
    lastNonDuplicatedPicId = 0

    for i, currentPic in enumerate(pictures):
        if i == 0:
            nonDups.append(currentPic)
            continue

        prevPic = pictures[lastNonDuplicatedPicId]

        if prevPic.metadata is None or currentPic.metadata is None:
            nonDups.append(currentPic)
            continue

        # Compare distance
        dist = prevPic.distance_to(currentPic)

        if dist <= params.maxDistance:  # type: ignore
            # Compare angle (if available on both images)
            if params.maxRotationAngle is not None and prevPic.metadata.heading is not None and currentPic.metadata.heading is not None:
                deltaAngle = abs(currentPic.metadata.heading - prevPic.metadata.heading)

                if deltaAngle <= params.maxRotationAngle:
                    dups.append(currentPic)
                else:
                    lastNonDuplicatedPicId = i
                    nonDups.append(currentPic)
            else:
                dups.append(currentPic)
        else:
            lastNonDuplicatedPicId = i
            nonDups.append(currentPic)

    return (nonDups, dups)


def split_in_sequences(pictures: List[Picture], splitParams: Optional[SplitParams] = SplitParams()) -> Tuple[List[Sequence], List[Split]]:
    """
    Split a list of pictures into many sequences.
    Note that this function expect pictures to be sorted and have their metadata set.

    Parameters
    ----------
    pictures : Picture[]
            List of pictures to check, sorted and with metadata defined
    splitParams : SplitParams
            The parameters to define deltas between two pictures

    Returns
    -------
    List[Sequence]
            List of pictures splitted into smaller sequences
    """

    # No split parameters given -> just return given pictures
    if splitParams is None or not splitParams.is_split_needed():
        return ([Sequence(pictures)], [])

    sequences: List[Sequence] = []
    splits: List[Split] = []
    currentPicList: List[Picture] = []

    for pic in pictures:
        if len(currentPicList) == 0:  # No checks for 1st pic
            currentPicList.append(pic)
        else:
            lastPic = currentPicList[-1]

            # Missing metadata -> skip
            if lastPic.metadata is None or pic.metadata is None:
                currentPicList.append(pic)
                continue

            # Time delta
            timeDelta = lastPic.metadata.ts - pic.metadata.ts
            if (
                lastPic.metadata.ts_by_source
                and lastPic.metadata.ts_by_source.gps
                and pic.metadata.ts_by_source
                and pic.metadata.ts_by_source.gps
            ):
                timeDelta = lastPic.metadata.ts_by_source.gps - pic.metadata.ts_by_source.gps
            elif (
                lastPic.metadata.ts_by_source
                and lastPic.metadata.ts_by_source.camera
                and pic.metadata.ts_by_source
                and pic.metadata.ts_by_source.camera
            ):
                timeDelta = lastPic.metadata.ts_by_source.camera - pic.metadata.ts_by_source.camera
            timeOutOfDelta = False if splitParams.maxTime is None else (abs(timeDelta)).total_seconds() > splitParams.maxTime

            # Distance delta
            distance = lastPic.distance_to(pic)
            distanceOutOfDelta = False if splitParams.maxDistance is None else distance > splitParams.maxDistance

            # One of deltas maxed -> create new sequence
            if timeOutOfDelta or distanceOutOfDelta:
                sequences.append(Sequence(currentPicList))
                currentPicList = [pic]
                splits.append(Split(lastPic, pic, SplitReason.time if timeOutOfDelta else SplitReason.distance))

            # Otherwise, still in same sequence
            else:
                currentPicList.append(pic)

    sequences.append(Sequence(currentPicList))

    return (sequences, splits)


def dispatch_pictures(
    pictures: List[Picture],
    sortMethod: Optional[SortMethod] = None,
    mergeParams: Optional[MergeParams] = None,
    splitParams: Optional[SplitParams] = None,
) -> DispatchReport:
    """
    Dispatches a set of pictures into many sequences.
    This function both sorts, de-duplicates and splits in sequences all your pictures.

    Parameters
    ----------
    pictures : set of pictures to dispatch
    sortMethod : strategy for sorting pictures
    mergeParams : conditions for considering two pictures as duplicates
    splitParams : conditions for considering two sequences as distinct

    Returns
    -------
    DispatchReport : clean sequences, duplicates pictures and split reasons
    """

    # Sort
    myPics = sort_pictures(pictures, sortMethod)

    # De-duplicate
    (myPics, dupsPics) = find_duplicates(myPics, mergeParams)

    # Split in sequences
    (mySeqs, splits) = split_in_sequences(myPics, splitParams)

    return DispatchReport(mySeqs, dupsPics if len(dupsPics) > 0 else None, splits if len(splits) > 0 else None)
