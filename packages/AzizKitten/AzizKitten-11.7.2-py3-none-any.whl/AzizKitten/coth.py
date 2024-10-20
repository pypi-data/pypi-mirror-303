def coth(x: float | complex) -> float | complex:
    """
    Return the hyperbolic cotangent of x.
    """
    from .sinh import sinh
    from .cosh import cosh
    return cosh(x)/sinh(x)
