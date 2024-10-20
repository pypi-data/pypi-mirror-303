def quad(a:float | complex,b: float | complex,c: float | complex) -> list:
    """
    Return the solutions of the quadratic equation (form of: ax² + bx + c = 0).
    """
    from .sqrt import sqrt
    if a == 0:
        raise ValueError("value of 'a' must be different to 0.")
    if a+b+c == 0:
        quad.x1 = 1
        quad.x2 = c/a
    elif a-b+c == 0:
        quad.x1 = -1
        quad.x2 = -c/a
    else:
        delta = b**2-4*a*c
        quad.x1 = (-b+sqrt(delta))/(2*a)
        quad.x2 = (-b-sqrt(delta))/(2*a)
    pre_result = [quad.x1, quad.x2]
    result = []
    for solution in pre_result:
        if solution not in result:
            result.append(solution)
    return result