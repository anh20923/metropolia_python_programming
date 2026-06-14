addedtext = "Added line!\n This goes to writings.txt! \
which was created earlier.\n"

with open("chap5/example.txt", "a") as file:
    file.write(addedtext)

with open("chap5/example.txt", "r") as file:
    print(file.read())