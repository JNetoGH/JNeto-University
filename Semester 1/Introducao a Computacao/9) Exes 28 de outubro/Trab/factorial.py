def fact(num: int) -> int:
    result = num
    for i in range(num-1, 1, -1):
        print(f"{result} * {i}")
        result *= i
    return result

print(f"result = {fact(int(input('factorial of: ')))}")