from typing import Generator

def return_minimum(*args: list[str]) -> str:
    return min(item for sublist in args for item in sublist)

print(return_minimum(['b', 'aaaaaaaaa', 'bbbbbbbb'], ['fjdkfk']))

def find_idx() -> str:
    num = list(map(str, input('Введите значения разделенные пробелом: ').split()))
    try: 
        idx = int(input(f'Введите индекс одного из чисел от 0 до {len(num) - 1}: '))
        if not isinstance(idx, int):
            raise ValueError(f'Индекс должен быть целым числом')
    except:
        raise ValueError(f'Индекс должен быть целым числом')
    try:
        return f'Значение вашего индекса {idx} = {num[idx]}'
    except IndexError:
        raise IndexError ('Вы ввели индекс за пределами списка')

print(find_idx())

def combo_makdonalds(cheeseburger: dict[str: int|float], beafburger: dict[str: int|float], N: int = 4) -> dict[str: int|float]:
    result = {}
    for key, values in cheeseburger.items():
        if len(key) >= N:
            result[key] = values
    for key, values in beafburger.items():
        if len(key) >= N:
            result[key] = values
    return result

print(combo_makdonalds({'aaaaa': 5, 'fjskkdkd': 'fkdlslsd', 'fjdkkfdkf': 8.0, 'fjkdldldlfd': 2, 'a': 3}, {'aaaaa': 5, 'fjskkdkd': 6, 'fjdkkfdkf': 8.0, 'fjkdldldlfd': 2, 'a': 3}, 2 ))

def generator_repeat(n: int, phrase: str) -> Generator:
    for j in range(1, n + 1):
        yield j * phrase

for i in (generator_repeat(3, 'kw')):
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
