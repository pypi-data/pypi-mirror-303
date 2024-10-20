def sin(x: float | complex, deg=False) -> float | complex:
    """
    Return the sine of x.

    Measured in radians as defualt.
    """
    from .constants import pi, e
    if deg:
        x = pi*(x/180)
    if type(x) is not complex:
        return ((e**(1j*x)-e**(1j*-x))/2j).real
    if abs(((e**(1j*x)-e**(1j*-x))/2j).imag) < 1e-6:
        return ((e**(1j*x)-e**(1j*-x))/2j).real
    return (e**(1j*x)-e**(1j*-x))/2j