def tan(x: float | complex, deg=False) -> float | complex:
    """
    Return the tangent of x.

    Measured in radians as defualt.
    """
    from .sin import sin
    from .cos import cos
    from .constants import pi
    if deg:
        x = pi*(x/180)
    return sin(x)/cos(x)
