def power_numbers(*args):
    return [x ** 2 for x in args]


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(lst:list):
    new_lst = []
    for i in range(len(lst)):
        check = 0
        for j in range(2, lst[i]):
            if lst[i] % j == 0:
                check += 1
        if check == 0:
            new_lst.append(lst[i])
    return new_lst


def filter_numbers(l:list, s:str):
    if s == ODD:
        return list(filter(lambda x: x % 2 != 0, l))
    elif s == EVEN:
        return list(filter(lambda x: x % 2 == 0, l))
    else:
        return list(filter(lambda x: x > 1, is_prime(l)))


# print(filter_numbers([1, 2, 3, 5, 6, 8, 9, 11, 12, 7], PRIME))
