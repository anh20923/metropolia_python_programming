try:
    number = float(input("Give a number: "))
except Exception:
    print("The input was malformed.")
else:
    print("The input was suitable!")
