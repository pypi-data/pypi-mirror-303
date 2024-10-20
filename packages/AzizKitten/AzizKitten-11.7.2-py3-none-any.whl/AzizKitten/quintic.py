def quintic(a:float | complex,b: float | complex,c: float | complex,d: float | complex,e: float | complex, f: float | complex) -> list:
    """
    Return the solutions of the quintic equation (form of ax⁵ + bx⁴ + cx³ + dx² + ex + f = 0).
    """
    from .quartic import quartic
    from .derivative import derivative
    if a == 0:
        raise ValueError("Value of 'a' must be different to 0.")
    if f == 0:
        quartic(a,b,c,d,e)
        quintic.x1, quintic.x2, quintic.x3, quintic.x4, quintic.x5 = 0, quartic.x1, quartic.x2, quartic.x3, quartic.x4
    elif a+b+c+d+e+f == 0:
        A = a
        B = b+A
        C = c+B
        D = d+C
        E = -f
        quartic(A,B,C,D,E)
        quintic.x1, quintic.x2, quintic.x3, quintic.x4, quintic.x5 = 1, quartic.x1, quartic.x2, quartic.x3, quartic.x4
    elif -a+b-c+d-e+f == 0:
        A = a
        B = b-A
        C = c-B
        D = d-C
        E = f
        quartic(A,B,C,D,E)
        quintic.x1, quintic.x2, quintic.x3, quintic.x4, quintic.x5 = -1, quartic.x1, quartic.x2, quartic.x3, quartic.x4
    else:
        quintic.x1 = 1
        def func(x):
            return a*x**5+b*x**4+c*x**3+d*x**2+e*x+f
        while True:
            g = func(quintic.x1)
            if abs(func(quintic.x1)) < 1e-12:
                break
            g_prime = derivative(func, quintic.x1)
            if abs(g_prime) < 1e-6:
                quintic.x1 += 1
            else:
                quintic.x1 -= g/g_prime
        A = a
        B = b+A*quintic.x1
        C = c+B*quintic.x1
        D = d+C*quintic.x1
        E = -f/quintic.x1
        quartic(A,B,C,D,E)
        quintic.x2, quintic.x3, quintic.x4, quintic.x5 = quartic.x1, quartic.x2, quartic.x3, quartic.x4
    solutions = [quintic.x1, quintic.x2, quintic.x3, quintic.x4, quintic.x5]
    result = []
    for solution in solutions:
        if solution not in result:
            result.append(solution)
    return result