def acot(x: float) -> float:
    """
    Return the arc cotangent (measured in radians) of x.
    """
    from .atan import atan
    return atan(1/x)
