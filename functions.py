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
    # to be implemented

def estPremier(n):
    """
    Cette fonction permet de verifier si le nombre donne est premier ou non premier.
    """
    premier = True
    for i in range(1,n+1):
        if i != 1 and i != n:
            if n % i == 0:
                premier = False
    return premier

def division_euclidienne(devidende, diviseur):
    """
    Faire la division euclidienne.
    """
    q = devidende // diviseur #quotient
    r = devidende % diviseur #reste
    
    return (q,r)

def estDivisiblePar11(n):
    """
    Verifier si le nombre donne est divisible par 11.
    la fonction retourne (True,0) si le nombre est divisible par 11,sinon elle retourne (False,r)
    avec r: est le reste de la division.
    """       
    divisible = False
    multiple=[0,11,22,33,44,55,66,77,88,99]
    d = 0
    r = 0 
    digits = []
    while n>0:
        u = n%10
        digits.append(u)
        n = n//10
    
    for i in range(0,len(digits)):
        if i % 2 > 0:
            d = d - digits[i]
        else:
            d = d + digits[i]
    if d >=0:
        if d in multiple:
            divisible = True
        else:
            r = d % 11
    else: # d<0
        for k in multiple:
            if d+k >= 0:
                m = k # le plus petit multiple de 11 qui donne d+m >= 0.
                if d+m in multiple:
                    divisible = True
                else:
                    r = d+m        
                break
    return (divisible,r)