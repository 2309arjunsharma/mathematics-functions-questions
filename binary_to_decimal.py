def binary_to_decimal(binary_str):
    """
    Function to convert a binary string to its decimal integer representation.
    
    Parameters:
    binary_str (str): The binary string to convert.
    
    Returns:
    int: The decimal representation of the binary string.
    """
    # Your code here
    decimal =0
    binary_str=str(binary_str)
    l=len(binary_str)
    for i in range(l):
        d = binary_str[l-1-i]
        if d=='1':
            decimal+=2**i
 
    return decimal
    
print(binary_to_decimal(1110011))
