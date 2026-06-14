inputFileName = input("Give a file name: ")
writeText = input("Write something: ")

with open("chap5/"+inputFileName, "w") as file:
    file.write(writeText)
    print(f"Wrote {writeText} to the file {inputFileName}")