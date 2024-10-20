def log(x: float, base=10) -> float | complex:
    """
    Return the logarithm of x in 'base'.

    Default base is 10 for decimal logarithm.
    """
    from .ln import ln
    return(ln(x)/ln(base))
