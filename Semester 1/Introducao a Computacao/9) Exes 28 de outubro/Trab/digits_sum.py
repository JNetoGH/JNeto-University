def get_sum_of_digits(num_as_str: str) -> int:
    sum = 0
    for digit in num_as_str:
        sum += int(digit)
    return sum


def is_even(num: int) -> bool:
    if num == 0:
        return True
    return num % 2 == 0


def check(num: int) -> None:
    n = str(num)
    print(f"is {n} digit sum even? sum = {get_sum_of_digits(n)}  is even = {is_even(get_sum_of_digits(n))}")


for i in range(100, 200+1):
    check(i)
