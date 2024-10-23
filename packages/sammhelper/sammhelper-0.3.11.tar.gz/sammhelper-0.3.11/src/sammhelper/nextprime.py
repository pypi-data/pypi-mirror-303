import numpy as np
    
def nextprime(n):
    
    """
    Finds the next prime number.
    
    Args:
        n (int): Any number.
    
    Returns:
        p (int): Next prime number.
    """ 
    
    p=n+1
    for i in range(2,p):
        if(np.mod(p,i)==0):
            p=p+1
    else:
        return p