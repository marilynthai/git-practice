def max_value(numbers):
    """ This function returns the largest number
        in the list.
    """
    num = 0
    for number in numbers:
        if number > num:
            num = number
    return num


if __name__ == "__main__":
    print(max_value([1, 12, 2, 42, 8, 3]))
