def ceil(x: float) -> int:
    """
    Return the ceiling of x, the smallest integer greater than or equal to x.
    """
    if x == int(x) or x <= 0:
        return int(x)
    return int(x)+1