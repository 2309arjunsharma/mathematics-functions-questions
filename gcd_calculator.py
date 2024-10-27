def gcd(n, m):
    """
    Function to find the GCD of two integers without using built-in functions and recursion.
    
    Parameters:
    n (int): The first integer.
    m (int): The second integer.
    
    Returns:
    int: The GCD of n and m.
    """
    # Your code here
    n=abs(n)
    m=abs(m)
    while m!=0:
        m, n= n%m, m
    return n 
        
print(gcd(121,1331))
