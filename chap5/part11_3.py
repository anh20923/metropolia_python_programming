with open("chap5/strings.txt", "r", encoding='utf-8') as file:
    content = file.readlines()
    for eachLine in content:
        if (eachLine[:-1].isalnum() == True): print(eachLine[:-1] + " was ok.")
        else: print(eachLine[:-1] + " was invalid.")
        