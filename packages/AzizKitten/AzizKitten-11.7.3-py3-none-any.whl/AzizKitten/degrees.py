def degrees(x: float) -> float:
    """
    Convert a value from the unit radians to the unit degrees.
    """
    from .constants import pi
    return x*180/pi