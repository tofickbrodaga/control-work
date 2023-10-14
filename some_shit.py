from typing import Callable, Generator
# 1
def sum_all():
    summary = 0
    while True:
        value = (input('Введите числа: '))
        if value=='q':
            print('Программа завершена')
            break
        else:
            try:
                summary += int(value)
            except ValueError:
                return 'Возвращайте числа'
    return summary

# print(sum_all())

# 2
def get_filtered_strings(frst: list[str], scnd: list[str]) -> list[str]:

    min_length = min(len(item) for item in scnd)
    filtered_strings = [s for s in frst if len(s) <= min_length]

    return filtered_strings

print(get_filtered_strings(['aopsps', 'pspssoos', 'dksls', '4', '5'], ['1', '2', '3', '4', '5']))

# 3
def get_dict(frst: dict[str, int|float], scnd: dict[str, int|float], N: str = 'a') -> dict:
    result = {}
    for key, value in frst.items():
        if key in N:
            result[key] = value
    for key, value in scnd.items():
        if key in N:
            if value not in result:
                result[key] = value
    return result

print(get_dict({'a': 1, 'b': 2, 'c': 3}, {'d': 4, 'aaaaa': 2, 'e': 5, 'f': 6}))

# 4
def gen_square(n: int) -> Generator:
    for i in range(0, n):
        yield i**n

for i in (gen_square(4)):
    print(i) 

# 5
def decorate_this(func: Callable) -> Callable:
    def new(*args):
            for arg in args:
                if not isinstance(arg, (int, float)):
                   raise ValueError('Функция должна принимать только числа int|float')
            return func(*args)
    return new

@decorate_this
def true_decorate(a, b):
    return a + b

print(true_decorate(1, 'a'))