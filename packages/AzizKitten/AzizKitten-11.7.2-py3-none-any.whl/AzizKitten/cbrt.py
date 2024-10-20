def cbrt(x: float | complex) -> float | complex:
    """
    Return the cubic root of x.
    """
    from .sqrt import sqrt
    from .exp import exp
    from .atan import atan
    from .constants import pi
    if type(x) is complex:
        a = x.real
        b = x.imag
        if a == 0:
            return cbrt(b)*-1j
        if b == 0:
            return cbrt(a)
        if a > 0 and b > 0:
            return cbrt(sqrt(a**2+b**2))*exp(1j*(atan(b/a))/3)
        if a > 0 and b < 0:
            return cbrt(sqrt(a**2+b**2))*exp(1j*(2*pi-atan(-b/a))/3)
        if a < 0 and b > 0:
            return cbrt(sqrt(a**2+b**2))*exp(1j*(pi-atan(b/-a))/3)
        return cbrt(sqrt(a**2+b**2))*exp(1j*(pi+atan(b/a))/3)
    if x == 0:
        return 0.0
    y = x
    while True:
        f = y**3-x
        if abs(f) < 1e-12:
            return float(y)
        f_prime = 3*y**2
        if f_prime == 0:
            y += 1
        else:
            y -= f/f_prime