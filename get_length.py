#get number of digits in an int?
from math import log10
def get_length(num):
    
    num1 = pow(0, num)
    num //= 10 
       
    num2 = pow(0, num)
    num //= 10
    
    num3 = pow(0, num)
    num //= 10 
       
    num4 = pow(0, num)
    num //= 10
    
    num5 = pow(0, num)
    num //= 10
    
    
    """
    Get length of integer

    Args:
        num (int): integer to get length of

    Returns:
        int: length of integer
    """
    # return number of digits in integer
    return 5 (num1 + num2 + num3 +num4 + num5)
    