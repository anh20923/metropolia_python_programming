"""
def readfile(name):
    try:
        readfile = open(name, 'r')
        content = readfile.read()
        readfile.close()
        return content
    except IOError:
        return False
"""



# def readFile(name):
#     try: 
#         fileName = open("chap5/example.txt", "r")
#         content = fileName.readlines()
#         fileName.close()
#         return content
#     except IOError:
#         return False
    
# print(readFile("chap5/anotherfile.txt"))





# file = open("chap5/example.txt", "r")

# print(file.readline())  # đọc dòng 1

# print("vi tri hien tai:", file.tell())      # vị trí hiện tại

# file.seek(19)    

# print(file.readline())  

# file.close()





readfile = open('chap5/example.txt', 'r')

content = readfile.readline()

location = readfile.tell()

# print(content[:-1] + "; The pointer is now at", location)

# print("Return to character number 10:")

readfile.seek(10)

content = readfile.read()

print(content)
#!
# Second line!
# Last in line!

readfile.close()