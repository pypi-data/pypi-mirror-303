def cos(x: float | complex, deg=False) -> float | complex:
    """
    Return the cosine of x.

    Measured in radians as defualt.
    """
    from .constants import pi, e
    if deg:
        x = pi*(x/180)
    if type(x) is not complex:
        return ((e**(1j*x)+e**(1j*-x))/2).real
    if abs(((e**(1j*x)+e**(1j*-x))/2).imag) < 1e-6:
        return ((e**(1j*x)+e**(1j*-x))/2).real
    return (e**(1j*x)+e**(1j*-x))/2