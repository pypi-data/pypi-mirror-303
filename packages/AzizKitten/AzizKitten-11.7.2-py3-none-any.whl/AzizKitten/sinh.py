def sinh(x: float | complex) -> float | complex:
    """
    Return the hyperbolic sine of x.
    """
    from .constants import e
    return (e**x-e**(-x))/2