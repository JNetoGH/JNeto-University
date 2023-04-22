def sum_tuples(t: tuple) -> None:
    s = 0
    for num in t:
        s += num
    print(f"sum = {s}")


sum_tuples((2, 5, 4))
