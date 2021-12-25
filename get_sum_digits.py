#Find the sum of digits in an integer
def get_sum_digits(num):
    num1 = num % 10
    num //= 10    
   
    num2 = num % 10
    num //= 10 
    
    num3 = num % 10
    num //= 10 
    
    num4 = num % 10
    num //= 10 
   
    num5 = num % 10
    num //= 10  
    
    """
    Get sum of digits in integer
    
    
    Args:
        num (int): integer to get sum of digits of
    
    Returns:
        int: sum of digits in integer
    """
    # return sum of digits in integer
    return  num1 + num2 + num3 + num4 + num5