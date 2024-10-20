def asec(x:float) -> float:
    """
    Return the arc secant (measured in radians) of x.
    """
    from .acos import acos
    return acos(1/x)
