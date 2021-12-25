#get number of digits in an int?
def get_length(num):
    num1 = num % 10
    num //= 10 
    num1 -= num1 + 1  
   
    num2 = num % 10
    num //= 10 
    num2 -= num2 + 1
    
    num3 = num % 10
    num //= 10 
    num3 -= num3 + 1
    
    num4 = num % 10
    num //= 10 
    num4 -= num4 + 1
   
    num5 = num % 10
    num //= 10 
    num5 -= num5 + 1       
    """
    Get length of integer

    Args:
        num (int): integer to get length of

    Returns:
        int: length of integer
    """
    # return number of digits in integer
    return num1 - num2 - num3 - num4 - num5

 