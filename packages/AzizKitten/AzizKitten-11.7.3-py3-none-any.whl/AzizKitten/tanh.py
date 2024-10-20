def tanh(x: float | complex) -> float | complex:
    """
    Return the hyperbolic tangent of x.
    """
    from .sinh import sinh
    from .cosh import cosh
    return sinh(x)/cosh(x)
