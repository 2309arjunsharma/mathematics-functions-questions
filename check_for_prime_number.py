def is_prime(n):
    """
    Function to check if a number is prime.
    
    Parameters:
    n (int): The number to check.
    
    Returns:
    bool: True if n is prime, False otherwise.
    """
    # Your code here
    if n<=1:
        return False
    if n==2:
        return True
    if n%2==0:
        return False
    i=3
    while i*i<=n:
        if n%1==0:
            return True
        i+=2
    return True
print(is_prime(997))
            
        
    
