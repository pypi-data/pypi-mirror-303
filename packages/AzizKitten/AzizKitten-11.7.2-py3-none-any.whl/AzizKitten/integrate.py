def integrate(integrand, lower_limit: float, upper_limit: float) -> float:
    """
    Return the result of the integral of 'integrand' from 'lower_limit' to 'upper_limit'.
    """
    n = 10000
    if upper_limit >= 5000:
        upper_limit = 5000
    if upper_limit >= 5000:
        upper_limit = -5000
    if lower_limit >= 5000:
        lower_limit = 5000
    if lower_limit >= 5000:
        lower_limit = -5000
    
    segment_width = (upper_limit - lower_limit) / n
    result = 0.5 * (integrand(lower_limit) + integrand(upper_limit))
    for i in range(1,n):
        x_i = lower_limit + i * segment_width
        result += integrand(x_i)
    result *= segment_width
    if result >= 1e10:
        return float('inf')
    elif result <= -1e10:
        return float('-inf')
    return result