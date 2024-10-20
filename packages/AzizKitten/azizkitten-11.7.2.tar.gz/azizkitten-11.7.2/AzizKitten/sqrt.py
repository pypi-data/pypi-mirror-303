def sqrt(x: float | complex) -> float | complex:
    """
    Return the square root of x.
    """
    if type(x) is not complex:
        if x < 0:
            return (-x)**.5*1j
    return x**.5