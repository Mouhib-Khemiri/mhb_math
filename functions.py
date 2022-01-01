def div(a, b):
    """
    Returns a/b
    """
    if b != 0:
        return a/b

def add(a, b):
    """
    Returns a + b
    """
    return a+b

def power(a, n):
    """Returns a to the power n"""
    p = 1
    for k in range(1,n+1):
        p = p * a
    
    if n < 0:
        n = -n
        for k in range(1,n+1):
            p = p * a
        p = div(1,p) 

    return p