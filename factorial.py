def cal_factorial(n: int) -> int:
    """
    calculate factorial of given number

    Args:
        n (int): given natural number

    Returns:
        int: factorial of n
    """
    if n == 1 or n == 0:
        return 1
    
    return n * cal_factorial(n-1)