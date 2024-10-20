def is_prime(x: int) -> bool:
    from .floor import floor
    from .sqrt import sqrt
    if int(x) != x or x < 0:
        raise TypeError("Value input must be a positive integer.")
    if x == 0 or x == 1:
        return False
    if x == 2:
        return True
    for i in range(2, floor(sqrt(x))+1):
        if int(x) % i == 0:
            return False
    return True
