class Calculator:

    def sum(self, num1: float, num2: float) -> None:
        print(f"{num1} + {num2} = {num1 + num2}")

    def sub(self, num1: float, num2: float) -> None:
        print(f"{num1} - {num2} = {num1 - num2}")

    def div(self, num1: float, num2: float) -> None:
        try:
            print(f"{num1} / {num2} = {num1 / num2}")
        except ZeroDivisionError:
            print("cannot divide by 0")

    def mult(self, num1: float, num2: float) -> None:
        print(f"{num1} * {num2} = {num1 * num2}")

    def is_prime(self, num: int) -> None:
        for i in range(2, num):
            if num % i == 0:
                print(f"{num} is not prime, division found with {i}")
                return
        print(f"{num} is prime")


calculator: Calculator = Calculator()
calculator.sum(5, 5)
calculator.sub(5, 8)
calculator.div(5, 2)
calculator.div(5, 0)
calculator.mult(5, 4.5)
print()
calculator.is_prime(10)
calculator.is_prime(5)
calculator.is_prime(55)
calculator.is_prime(7)
