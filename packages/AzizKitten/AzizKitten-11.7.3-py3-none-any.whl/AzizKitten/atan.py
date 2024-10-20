def atan(x: float) -> float:
    """
    Return the arc tangent (measured in radians) of x.
    """
    from .integrate import integrate
    def integrand(t):
        return 1/(1+t**2)
    return integrate(integrand, 0, x)
