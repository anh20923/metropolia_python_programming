inputFileName = input("Give the file name: ")
try:
    with open(inputFileName, "r") as file:
        content = file.read()
        content = float(content)
        result = content/1000
except FileNotFoundError:
    print("There seems to be no file with that name.")
except(TypeError, ValueError):
    print("The file contents were unsuitable.")
except Exception:
    print("There was a problem with the program.")
else:
    print(f"The result was {result}")
