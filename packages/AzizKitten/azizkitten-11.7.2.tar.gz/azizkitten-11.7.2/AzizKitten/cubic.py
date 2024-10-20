def cubic(a: float | complex,b: float | complex,c: float | complex,d: float | complex) -> list:
    """
    Return the solutions of the cubic equation (form of: ax³ + bx² + cx + d = 0).
    """
    from .cbrt import cbrt
    from .sqrt import sqrt
    from .quad import quad
    if a == 0:
        raise ValueError("value of 'a' must be different to 0.")
    if a+b+c+d == 0:
        A = a
        B = b+a
        C = -d
        quad(A,B,C)
        cubic.x1, cubic.x2, cubic.x3 = 1, quad.x1, quad.x2
    elif -a+b-c+d == 0:
        A = a
        B = b-a
        C = d
        quad(A,B,C)
        cubic.x1, cubic.x2, cubic.x3 = -1, quad.x1, quad.x2
    else:
        p = (3*a*c-b**2)/(3*a**2)
        q = (2*b**3-9*a*b*c+27*a**2*d)/(27*a**3)
        if type(-q/2+sqrt(q**2/4+p**3/27)) is complex:
            cubic.x1 = cbrt(-q/2+sqrt(q**2/4+p**3/27))+(cbrt(-q/2+sqrt(q**2/4+p**3/27))).real-1j*(cbrt(-q/2+sqrt(q**2/4+p**3/27))).imag-b/(3*a)
            cubic.x2 = (-1+sqrt(-3))/2*cbrt(-q/2+sqrt(q**2/4+p**3/27))+(-1-sqrt(-3))/2*((cbrt(-q/2+sqrt(q**2/4+p**3/27))).real-1j*(cbrt(-q/2+sqrt(q**2/4+p**3/27))).imag)-b/(3*a)
            cubic.x3 = (-1-sqrt(-3))/2*cbrt(-q/2+sqrt(q**2/4+p**3/27))+(-1+sqrt(-3))/2*((cbrt(-q/2+sqrt(q**2/4+p**3/27))).real-1j*(cbrt(-q/2+sqrt(q**2/4+p**3/27))).imag)-b/(3*a)
        else:
            cubic.x1 = cbrt(-q/2+sqrt(q**2/4+p**3/27))+cbrt(-q/2-sqrt(q**2/4+p**3/27))-b/(3*a)
            cubic.x2 = (-1+sqrt(-3))/2*cbrt(-q/2+sqrt(q**2/4+p**3/27))+(-1-sqrt(-3))/2*cbrt(-q/2-sqrt(q**2/4+p**3/27))-b/(3*a)
            cubic.x3 = (-1-sqrt(-3))/2*cbrt(-q/2+sqrt(q**2/4+p**3/27))+(-1+sqrt(-3))/2*cbrt(-q/2-sqrt(q**2/4+p**3/27))-b/(3*a)
    if type(cubic.x1) is complex:
        if abs(cubic.x1.imag) < 1e-6:
            cubic.x1 = cubic.x1.real+0j
        if abs(cubic.x1.real) < 1e-6:
            cubic.x1 = 0+cubic.x1.imag*1j
        if cubic.x1.imag == 0:
            cubic.x1 = cubic.x1.real
    if type(cubic.x2) is complex:
        if abs(cubic.x2.imag) < 1e-6:
            cubic.x2 = cubic.x2.real+0j
        if abs(cubic.x2.real) < 1e-6:
            cubic.x2 = 0+cubic.x2.imag*1j
        if cubic.x2.imag == 0:
            cubic.x2 = cubic.x2.real
    if type(cubic.x3) is complex:
        if abs(cubic.x3.imag) < 1e-6:
            cubic.x3 = cubic.x3.real+0j
        if abs(cubic.x3.real) < 1e-6:
            cubic.x3 = 0+cubic.x3.imag*1j
        if cubic.x3.imag == 0:
            cubic.x3 = cubic.x3.real
    if type(cubic.x1) is not complex:
        if abs(cubic.x1) < 1e-6:
            cubic.x1 = 0
    if type(cubic.x2) is not complex:
        if abs(cubic.x2) < 1e-6:
            cubic.x2 = 0
    if type(cubic.x3) is not complex:
        if abs(cubic.x3) < 1e-6:
            cubic.x3 = 0
    pre_result = [cubic.x1,cubic.x2,cubic.x3]
    result = []
    for solution in pre_result:
        if solution not in result:
            result.append(solution)
    return result