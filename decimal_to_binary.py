def int_to_binary(n):
    """
    Function to convert an integer to its binary representation.
    
    Parameters:
    n (int): The integer to convert.
    
    Returns:
    str: The binary representation of the integer.
    """
    # Your code here
    if n==0:
        return "0"
    binary=""
    i=n<0
    if i:
        n=-n
    while n>0:
        r=n%2
        binary=str(r)+binary
        n=n//2
    if i:
        binary="-"+binary
    return binary
    
print(int_to_binary(276))
    
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
