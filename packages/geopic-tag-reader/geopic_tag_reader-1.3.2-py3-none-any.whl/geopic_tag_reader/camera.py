from typing import Optional, Dict, List

# List of equirectangular cameras (make, model)
# https://en.wikipedia.org/wiki/List_of_omnidirectional_(360-degree)_cameras
EQUIRECTANGULAR_MODELS: Dict[str, List[str]] = {
    "Panono": ["Panono"],
    "Vuze": ["Vuze"],
    "Vuze+": ["Vuze+"],
    "BUBL": ["Bublcam"],
    "Ricoh": ["Theta", "Theta m15", "Theta S", "Theta SC", "Theta SC2", "Theta V", "Theta Z1"],
    "Insta360": ["4K", "Nano", "Air", "One", "Pro", "One X", "One R", "X3", "Titan"],
    "Samsung": ["Gear360"],
    "LG": ["360 CAM"],
    "MadV": ["Madventure 360"],
    "Nikon": ["Keymission 360"],
    "Xiaomi": ["米家全景相机"],
    "小蚁(YI)": ["小蚁VR全景相机"],
    "Giroptic iO": ["Giroptic iO"],
    "Garmin": ["Virb 360"],
    "Nokia": ["OZO"],
    "Z Cam": ["S1 Pro", "V1 Pro"],
    "Rylo": ["Rylo"],
    "GoPro": ["Fusion", "Max"],
    "FXG": ["SEIZE", "FM360 Duo"],
}


def is_360(make: Optional[str] = None, model: Optional[str] = None, width: Optional[str] = None, height: Optional[str] = None) -> bool:
    """
    Checks if given camera is equirectangular (360°) based on its make, model and dimensions (width, height).

    >>> is_360()
    False
    >>> is_360("GoPro")
    False
    >>> is_360("GoPro", "Max 360")
    True
    >>> is_360("GoPro", "Max 360", "2048", "1024")
    True
    >>> is_360("GoPro", "Max 360", "1024", "768")
    False
    >>> is_360("RICOH", "THETA S", "5376", "2688")
    True
    """

    # Check make and model are defined
    if not make or not model:
        return False

    # Check width and height are equirectangular
    if not ((width is None or height is None) or int(width) == 2 * int(height)):
        return False

    # Find make
    matchMake = next((m for m in EQUIRECTANGULAR_MODELS.keys() if make.lower() == m.lower()), None)
    if matchMake is None:
        return False

    # Find model
    return any(model.lower().startswith(m.lower()) for m in EQUIRECTANGULAR_MODELS[matchMake])
