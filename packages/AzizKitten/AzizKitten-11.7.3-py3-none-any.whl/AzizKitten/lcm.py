def lcm(a:int,b:int) -> int:
    """
    Return the least common multiple of two integers a and b.
    """
    from .gcd import gcd
    return abs(a*b) // gcd(a,b)
