def sum_numbers(numbers=None):
    if numbers == []:
        return 0
    elif not numbers:
        return sum(range(1, 101))
    else:
        return sum(numbers)
