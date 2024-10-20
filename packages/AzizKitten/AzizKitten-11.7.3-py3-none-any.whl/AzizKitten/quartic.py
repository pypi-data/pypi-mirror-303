def quartic(a:float | complex,b: float | complex,c: float | complex,d: float | complex,e: float | complex) -> list:
    """
    Return the solutions of the quartic equation (form of: ax⁴ + bx³ + cx² + dx + e = 0).
    """
    from .sqrt import sqrt
    from .cubic import cubic
    if a == 0:
        raise ValueError("Value of 'a' must be different to 0.")
    if e == 0:
        cubic(a,b,c,d)
        quartic.x1, quartic.x2, quartic.x3, quartic.x4 = 0, cubic.x1, cubic.x2, cubic.x3
    elif a+b+c+d+e == 0:
        A = a
        B = b+A
        C = c+B
        D = -e
        cubic(A,B,C,D)
        quartic.x1, quartic.x2, quartic.x3, quartic.x4 = 1, cubic.x1, cubic.x2, cubic.x3
    elif a-b+c-d+e == 0:
        A = a
        B = b-A
        C = c-B
        D = e
        cubic(A,B,C,D)
        quartic.x1, quartic.x2, quartic.x3, quartic.x4 = -1, cubic.x1, cubic.x2, cubic.x3
    else:
        p = (8*a*c-3*b**2)/(8*a**2)
        q = (b**3-4*a*b*c+8*a**2*d)/(8*a**3)
        r = (16*a*c*b**2-3*b**4-64*a**2*d*b+256*a**3*e)/(256*a**4)
        cubic(1,5*p/2,2*p**2-r,(4*p**3-4*p*r-q**2)/8)
        z = cubic.x1
        quartic.x1 = (sqrt(p+2*z)+sqrt(-3*p-2*z-2*q/sqrt(p+2*z)))/2-b/(4*a)
        quartic.x2 = (sqrt(p+2*z)-sqrt(-3*p-2*z-2*q/sqrt(p+2*z)))/2-b/(4*a)
        quartic.x3 = (-sqrt(p+2*z)+sqrt(-3*p-2*z+2*q/sqrt(p+2*z)))/2-b/(4*a)
        quartic.x4 = (-sqrt(p+2*z)-sqrt(-3*p-2*z+2*q/sqrt(p+2*z)))/2-b/(4*a)
    pre_result = [quartic.x1, quartic.x2, quartic.x3, quartic.x4]
    result = []
    for solution in pre_result:
        if solution not in result:
            result.append(solution)
    return result