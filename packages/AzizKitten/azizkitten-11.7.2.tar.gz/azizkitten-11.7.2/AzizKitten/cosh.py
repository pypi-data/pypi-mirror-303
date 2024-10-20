def cosh(x: float | complex) -> float | complex:
    """
    Return the hyperbolic cosine of x.
    """
    from .constants import e
    return (e**x+e**(-x))/2
