def power_numbers(*args):
    return [x ** 2 for x in args]


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(number):
    if (number == 0) or (number == 1):
        return False
    for i in range(2, (number // 2) + 1):
        if number % i == 0:
            return False
    return True


def filter_numbers(numbers_list: list, filter_type: str):
    if filter_type == ODD:
        return list(filter(lambda x: x % 2 != 0, numbers_list))
    elif filter_type == EVEN:
        return list(filter(lambda x: x % 2 == 0, numbers_list))
    else:
        return list(filter(is_prime, numbers_list))


print(filter_numbers([1, 2, 3, 5, 6, 8, 9, 11, 12, 7], PRIME))
