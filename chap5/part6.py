# file = open("chap5/test.txt", "w")
# file.write("Hello")

# #append file
# file = open("chap5/test.txt", "a")
# file.write(" World")

# #read file after write
# file = open("chap5/test.txt", "r")
# print(file.read())
# file.close()

with open("chap5/test.txt", "w") as file:
    file.write("Hello")

with open("chap5/test.txt", "a") as file:
    file.write(" World")

with open("chap5/test.txt", "r") as file:
    print(file.read())