def exp(x: float | complex) -> float | complex:
    """
    Return the exponential function of x.
    """
    from .constants import e
    return e**x
