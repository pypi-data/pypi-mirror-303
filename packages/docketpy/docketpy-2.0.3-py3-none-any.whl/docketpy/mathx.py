import math

def square_root(x):
    """
    Calculate the square root of a number.
    
    Args:
        x (float): The number for which to calculate the square root.
        
    Returns:
        float: The square root of the input number.
    """
    return math.sqrt(x)

def cube_root(x):
    """
    Calculate the cube root of a number.
    
    Args:
        x (float): The number for which to calculate the cube root.
        
    Returns:
        float: The cube root of the input number.
    """
    return x**(1/3)

def fourth_root(x):
    """
    Calculate the fourth root of a number.
    
    Args:
        x (float): The number for which to calculate the fourth root.
        
    Returns:
        float: The fourth root of the input number.
    """
    return x**(1/4)


def fifth_root(x):
    return x**(1/5)


def sixth_root(x):
    return x**(1/6)


if __name__ == "__main__":
    print(square_root(4))
    print(cube_root(8))
    print(fourth_root(16))
    print(fifth_root(32))
    print(fifth_root(64))
    