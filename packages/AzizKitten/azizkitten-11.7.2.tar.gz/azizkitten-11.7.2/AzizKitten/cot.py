def cot(x: float | complex, deg=False) -> float | complex:
    """
    Return the cotangent of x.

    Measured in radians as defualt.
    """
    from .sin import sin
    from .cos import cos
    from .constants import pi
    if deg:
        x = pi*(x/180)
    return cos(x)/sin(x)