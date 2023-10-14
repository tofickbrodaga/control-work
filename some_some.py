from typing import Generator, Callable

def ret_min(*args: list[str]) -> str:
    for arg in args:
        for item in arg:
            arg = min(item)
    return arg

print(ret_min(['aaaa', 'aaaaaaaaa', 'bbbbbbbb'], ['aaaaa', 'ajdjdkk', 'a']))

def find_idx() -> str:
    num = list(map(str, input('Введите значения разделенные пробелом: ').split()))
    idx = int(input(f'Введите индекс одного из чисел от 0 до {len(num) - 1}: '))
    try:
        return f'Значение вашего индекса {idx} = {num[idx]}'
    except IndexError:
        raise IndexError ('Вы ввели индекс за пределами списка')

# print(find_idx())

def combo_makdonalds(cheeseburger: dict[str: int|float], maccombo: dict[str: int|float], N: int = 4) -> dict[str: int|float]:
    result = {}
    for key, values in cheeseburger.items():
        if len(key) >= N:
            result[key] = values
    for key, values in maccombo.items():
        if len(key) >= N:
            result[key] = values
    return result

print(combo_makdonalds({'fjllsls': 1, 'fjsklsl': 2, 'fjkd': 3, 'djksk': 4}, {'fjs': 1, 'fjsklsl': 2, 'fjkd': 3, 'djksk': 4}))

def gen_repeat(n: int, phrase: str) -> Generator:
    for j in range(1, n + 1):
        yield j * phrase

for i in (gen_repeat(5, 'hello')):
    print(i)

def check_args_count(func):
    def wrapper(*args):
        if len(args) != 3:
            raise ValueError('Эта функция принимает 3 аргумента: не больше и не меньше!')
        return func(*args)
    return wrapper

@check_args_count
def my_func(a, b, c):
    return a + b + c

print(my_func(1, 2, 3))
