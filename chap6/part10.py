# def printer(stringstuff):
#     stringrow = stringstuff
#     print(stringrow)

# stringrow = "Defined in the main level."
# printer(stringrow)

def printer(stringstuff):
    stringrow = "Defined in the subfunction."
    print(stringrow)

stringrow = "Defined in the main level."

printer(stringrow)

print(stringrow)