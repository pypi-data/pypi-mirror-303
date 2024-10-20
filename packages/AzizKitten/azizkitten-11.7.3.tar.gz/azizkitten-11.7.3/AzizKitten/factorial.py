def factorial(x: float) -> float:
    """
    Return the factorial of x where x ∉ {-1, -2, -3, ...}.
    """
    from .exp import exp
    from .integrate import integrate
    if int(x) == x:
        if x < 0:
            raise ValueError("Factorial of a negative integer is undefined.")
        else:
            ans = 1
            for i in range(1,int(x)+1):
                ans *= i
            return ans
    def integrand(t):
        return t**x * exp(-t)
    return integrate(integrand, 0, 100)