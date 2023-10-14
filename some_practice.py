from typing import Generator

def ret_list(frst: list[str], scnd: list[str], arg: str = 'A') -> list[str]:
    result = []
    for item in frst:
        if item.startswith(arg):
            result.append(item)
    for hyu in scnd:
        if hyu.startswith(arg):
            result.append(hyu)
    return result

print(ret_list(['ahdkdkf', 'AaaAAAAAAaaaaAA', 'AAdyksjjfjd', 'kfkfkld'], ['fjidso', 'fjdkid']))

def positive_digits(lst: list[int]) -> int:
    result = 0
    for i in lst:
        if i >= 0:
            result += i
    return result

print(positive_digits([1, -5, 6, 0, -1, -5]))

def gen_fib(n: int) -> Generator:
    fib1 = 1
    fib2 = 1
    i = 0
    while i < n - 2:
        fib_sum = fib1 + fib2
        fib1 = fib2
        fib2 = fib_sum
        i = i + 1
    yield fib2  

for i in (gen_fib(2)):
    print(i)

def union_digits(digits: list[int]) -> list[int]:
    try:
        return list(set(digits))
    except ValueError:
        raise ValueError('Вы вводите что-то не то')

print(union_digits([1, 3, 1, 4]))

