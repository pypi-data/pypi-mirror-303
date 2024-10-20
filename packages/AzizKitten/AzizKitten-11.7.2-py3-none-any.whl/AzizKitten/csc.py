def csc(x: float | complex, deg=False) -> float | complex:
    """
    Return the cosecant of x.

    Measured in radians as defualt.
    """
    from .sin import sin
    from .constants import pi
    if deg:
        x = pi*(x/180)
    return 1/sin(x)
