from typing import Generator

# 1
def return_square(frst: list, snd: list) -> list:
    result = []
    n = len(frst)

    for item_frst in range(n):
        if frst[item_frst] ** 2 in snd:
            result.append(frst[item_frst])
    return result

print(return_square([1, 4, 6], [16, 1, 27]))


# 2
def square_number():
    while True:
        value=input("Введите число квадрат которого хотите получить либо введите q для завершения программы:")
        if value=="q":
            break
        else:
            try:
                print(f'Квадрат числа {value} равен {int(value)**2}')
            except ValueError:
                print("Возвращайте числа")

# 3
def combine_dictionaries(dict1: dict[str, int|float], dict2: dict[str, int|float], N: int = 8) -> dict:
    try:
        result = {}
        for key, value in dict1.items():
            if len(key) <= N:
                result[key] = value
        for key, value in dict2.items():
            if len(key) <= N:
                result[key] = value
        return result
    except TypeError:
        return 'Ключ не строковый формат'

print(combine_dictionaries({1: 1, 'b': 2, 'cаллввмсв': 3}, {'didkdkdkd': 4, 'e': 5, 'f': 6}))

# 4
def even_or_not_even(n: int, flag: bool = True) -> Generator:
    if flag == True:
        for i in range(0, n):
            if i % 2 == 0:
                yield i
    else:
        for i in range(0, n):
            if i % 2 != 0:
                yield i

for i in (even_or_not_even(10, False)):
    print(i)

# 5
def validate_arguments(func):
    def wrapper(*args):
        try:
            for arg in args:
                if not isinstance(arg, (int, float)):
                    raise ValueError ('Функция должна принимать только числа int|float')
            return func(*args)
        except ValueError:
            raise TypeError ('Функция должна принимать только числа int|float')
    return wrapper

@validate_arguments
def check_this(a, b):
    return a + b

print(check_this(1, 'q'))
print(check_this(4, 3))



