def power_numbers(*args):
    return [x ** 2 for x in args]


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(num):
    if (num == 0) or (num == 1):
        return False
    for i in range(2, (num // 2) + 1):
        if num % i == 0:
            return False
    return True



def filter_numbers(l:list, s:str):
    if s == ODD:
        return list(filter(lambda x: x % 2 != 0, l))
    elif s == EVEN:
        return list(filter(lambda x: x % 2 == 0, l))
    else:
        return list(filter(lambda x: is_prime(x), l))


# print(filter_numbers([1, 2, 3, 5, 6, 8, 9, 11, 12, 7], PRIME))
