from math import *


def resolveEqFirstDegree(equation):
    """
    Resolve a mathematical equation of first degree.
    Example of equation: ax +b = 0.
    This function returns x = -b/a as a solution for this equation.
    """
    posX = equation.find('x')
    posEqual =equation.find('=')
    a = equation[0:posX]
    b = equation[posX+1:posEqual]

    return -int(b)/int(a)

def getFormula(expression):
    """
    Returns an algebra formula for the given expression.
    It returns an empty string if no corresponding formula could be found.
    """
    formula = ""
    exp = expression.replace(" ","") #remove whitespaces from expression

    if exp == "(a+b)²":
        formula = "a²+2ab+b²"
    elif exp == "(a-b)²":
        formula ="a²-2ab+b²"
    elif exp == "(a+b)(a-b)" or exp == "(a-b)(a+b)":
        formula ="a²-b²" 
    elif exp == "(a+b+c)²":
        formula = "a²+b²+c²+2ab+2ac+2bc"

    if formula != "":
        formula = exp + "=" + formula   
    
    return formula  
def resolveEqSecondDegree(equation):
    """Resolves a second degree equation
    The given equation should be in the from of ax²+bx+c=0. 
    """
    eq = equation.replace(" ","")
    posSquare = eq.find('²')
    
    for i in range(0,len(eq)):
        if eq[i] == 'x':
            posx = i
        
    posEqual = eq.find('=')

    a = int(eq[0:posSquare-1])
    b = int(eq[posSquare+1:posx])
    c = int(eq[posx+1:posEqual])

    solution = []
    delta = b** -4*a*c
    if delta == 0:
        x0 =-b/2*a
        solution[x0]
    elif delta > 0:
        x1=(-b+sqrt(delta))/2*a
        x2=(-b-sqrt(delta))/2*a
        solution=[x1,x2]

    return solution
