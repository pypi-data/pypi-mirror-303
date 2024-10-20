def sech(x: float | complex) -> float | complex:
    """
    Return the hyperbolic secant of x.
    """
    from .cosh import cosh
    return 1/cosh(x)
