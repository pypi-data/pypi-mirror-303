def acsc(x:float) -> float:
    """
    Return the arc cosecant (measured in radians) of x.
    """
    from .asin import asin
    return asin(1/x)
