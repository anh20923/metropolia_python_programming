print("Words in an alphabetical order:")
with open("example.txt", "r") as file:
    for line in sorted(file):
        print(line, end="")
    