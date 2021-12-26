#get number of digits in an int?
from math import log10
def get_length(num):
    num = num + 1
    length = log10(num) + 1
    num1 = num % 10
    num //= 10 
    num1 -= abs(num1 - 1) - 1
   
    num2 = num % 10
    num //= 10 
    num2 -= abs(num2 - 1) - 1
    
    num3 = num % 10
    num //= 10 
    num3 -= abs(num3 - 1) - 1
    
    num4 = num % 10
    num //= 10 
    num4 -= abs(num4 - 1) - 1
   
    num5 = num % 10
    num //= 10 
    num5 -= abs(num5 - 1 ) - 1  
    
    """
    Get length of integer

    Args:
        num (int): integer to get length of

    Returns:
        int: length of integer
    """
    # return number of digits in integer
    return int(length)