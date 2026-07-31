

def upperCse(ip:str) -> str :
    return ip.upper()


def lowerCse(ip:str) -> str :
    return ip.lower()



def add(x, y):
    """Returns the sum of two numbers."""
    return x + y

def divide(x, y):
    """Returns the quotient, raises ValueError on division by zero."""
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y
