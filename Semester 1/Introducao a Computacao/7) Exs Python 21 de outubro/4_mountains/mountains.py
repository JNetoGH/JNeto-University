import os
from random import randint


class Mountain:
    def __init__(self, height):
        self.height = height

flag = True
while flag:
    mountains_list: list[Mountain] = []
    auto_generate = True
    while True:
        code = input("\nwanna auto generate mountains(1), or insert yours(2)? [1/2]: ")
        if code == "1":
            auto_generate = False
            print("PLEASE INSERT THE VALUES FOR AUTO GENERATION\n")
            break
        elif code == "2":
            print("PLEASE INSERT THE HEIGHTS YOURSELF AS REQUIRED\n")
            break
        else:
            print("please insert 1 or 2")

    if not auto_generate:
        while True:
            tot_mountains = 0
            min_height = 0
            max_height = 0
            input1 = input("tot of mountains: ")
            input2 = input("min_height: ")
            input3 = input("max_height: ")
            if input1.isnumeric() and input2.isnumeric() and input3.isnumeric():
                if int(input1) > 0 and int(input2):
                    tot_mountains = int(input1)
                    min_height = int(input2)
                    max_height = int(input3)
                    if min_height < max_height:
                        break
                    else:
                        print("min height needs to be smaller than max height!\n")
                else:
                    print("please insert a total o mountains and a min height bigger than 0\n")
            else:
                print("please insert only numbers!\n")

        for i in range(0, tot_mountains):
            mountains_list.append(Mountain(height=randint(min_height, max_height)))
    else:
        user_input = ""
        while True:
            print("Insert the mountain heights separated by comma ',' e.g. 15,20,30")
            user_input = input("input: ").split(",")
            any_errors = False
            for data in user_input:
                if data.isnumeric():
                    if int(data) <= 0:
                        print("HEIGHTS MUST BE BIGGER THAN 0!!!!\n")
                        any_errors = True
                else:
                    print("please insert only int numbers, WITH NO SPACES!!!!\n")
                    any_errors = True
            if not any_errors:
                break
        for data in user_input:
            mountains_list.append(Mountain(int(data)))

    smallest_mountain = mountains_list[0]
    biggest_mountain = mountains_list[0]
    print("\nMOUNTAINS HEIGHT: [", end=" | ")
    for mountain in mountains_list:
        if mountain.height < smallest_mountain.height:
            smallest_mountain = mountain
        elif mountain.height > biggest_mountain.height:
            biggest_mountain = mountain
        print(str(mountain.height), end=" | ")
    print("]")

    all_biggest_mountains = []
    all_smallest_mountains = []

    print("BIGGEST MOUNTAINS: ", end="")
    for i in range (0, len(mountains_list)):
        if mountains_list[i].height == biggest_mountain.height:
            print(f"[{i}]height={mountains_list[i].height}", end=" ")

    print("\nSMALLEST MOUNTAINS: ", end="")
    for i in range(0, len(mountains_list)):
        if mountains_list[i].height == smallest_mountain.height:
            print(f"[{i}]height={mountains_list[i].height}", end=" ")


    while True:
        code = input("\n\nwanna make another mountain list? [y/n]: ")
        if code.upper() == "N" or code.upper() == "NO":
            flag = False
            break
        elif code.upper() == "Y" or code.upper() == "YES":
            print("starting another round \n")
            break
        else:
            print("please insert y or n")