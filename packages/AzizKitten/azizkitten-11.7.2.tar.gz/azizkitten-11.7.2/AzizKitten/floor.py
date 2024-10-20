def floor(x: float) -> int:
    """
    Return the floor of x, the largest integer less than or equal to x.
    """
    if x == int(x) or x >= 0:
        return int(x)
    return int(x)-1