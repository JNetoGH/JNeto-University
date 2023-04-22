def fibo(num: int) -> None:
    curr = 0
    next = 1
    for i in range(1, num):
       if i == 1:
           print(0)
       sum = curr + next
       curr = next
       next = sum
       print(curr)

fibo(int(input("required num: ")))
