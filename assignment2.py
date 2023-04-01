def sum_of_squares(numbers):
    """
    Returns the sum of the squares of all the numbers in the input list.
    """
    sum = 0
    for num in numbers:
        sum += num ** 2
    return sum
