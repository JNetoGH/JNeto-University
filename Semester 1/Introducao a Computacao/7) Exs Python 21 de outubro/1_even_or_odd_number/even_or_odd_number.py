while True:
    code = input("insert a number to check if it's (odd/even) or type quit: ").upper()
    if code == "QUIT":
        break
    elif not code.isnumeric():
        print("\33[91minvalid input, please insert a number\033[0m")
    elif int(code) == 0:
        print(f"{code} is \033[92meven\033[0m")
    elif int(code) % 2 == 0:
        print(f"{code} is \033[92meven\033[0m")
    elif int(code) % 2 != 0:
        print(f"{code} is \033[93modd\033[0m")

