def sec(x:float | complex, deg=False) -> float | complex:
    """
    Return the secant of x.

    Measured in radians as defualt.
    """
    from .cos import cos
    from .constants import pi
    if deg:
        x = pi*(x/180)
    return 1/cos(x)
