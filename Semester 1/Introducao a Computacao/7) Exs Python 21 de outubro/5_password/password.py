class Password:

    special_chars = ["#", "$", "@"]

    def __init__(self):
        self.isValid = False
        self.content = input("please insert a password: ")

        self.has_lower_case = False
        self.has_upper_case = False
        self.has_number = False
        self.has_special_char = False
        self.is_in_range = True if 6 < len(self.content) < 16 else False

        for char in self.content:
            if char in Password.special_chars:
                self.has_special_char = True
            elif char.isnumeric():
                self.has_number = True
            elif char.isascii():
                if char.islower():
                    self.has_lower_case = True
                elif char.isupper():
                    self.has_upper_case = True

        self.isValid = self.has_lower_case and self.has_upper_case and self.has_number and self.has_special_char and self.is_in_range

        if self.isValid:
            print("All Good!")
        else:
            print("something went wrong\n\nstatus")
            print(f"has_lower_case: {self.has_lower_case}")
            print(f"has_upper_case: {self.has_upper_case}")
            print(f"has_number: {self.has_number}")
            print(f"has_special_char: {self.has_special_char}")
            print(f"is_in_range (6<length<16): {self.is_in_range}")

# APPLICATION LOOP
flag = True
while flag:

    Password()

    while True:
        code = input("\nwanna make another password? [y/n]: ")
        if code.upper() == "N" or code.upper() == "NO":
            flag = False
            break
        elif code.upper() == "Y" or code.upper() == "YES":
            print("starting another round \n\n")
            break
        else:
            print("please insert y or n")