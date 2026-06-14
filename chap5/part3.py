fileName = open("chap5/example.txt", "r")

# text = fileName.readlines()
# for i in text: 
#     print(i, end="")



text = fileName.readline()
text = text[:-1]
print(text)

fileName.close()

# handle = open("chap5/example.txt","r")
# filetext = handle.read()
# print(filetext)
# handle.close()