fileName = open("chap5/example.txt", "r")

#read()
# text = fileName.read()
# print("Using read() ",text)

#readline()
# text1 = fileName.readline()
# print("Using readline() ",text1)

#readlines()
text2 = fileName.readlines()
print("Using readlines() ",text2)


fileName.close()