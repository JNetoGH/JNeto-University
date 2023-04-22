file = open("../../../Users/JNeto/Downloads/lorem.txt")
content = file.readlines()
print("third line")
print(content[2])
print()

with open("../../../Users/JNeto/Downloads/lorem.txt") as f:
    [print(line) for line in f.readlines()]
