def calculator(distance,gas,mpg):
    price = gas*(distance/mpg)

    price = int(price)
    return price

def main():
    gasprice = float(input("How much is one gallon of gas?: "))
    tripdistance = int(input("How many miles will be driven?: "))
    averagempg = float(input("How many mpg does the car get?: "))

    total_sum = calculator(tripdistance,gasprice,averagempg)
    print("The trip will cost",total_sum,"euros.")

if __name__ == "__main__":
    main()


"""
01  def getlength(testme):
02      if len(testme) < 42:
03          return 0
04      else:
05          return 1
06
07  result = getlength("ohgodwhydoesthisstringhavetobesolongicanteverrememberthis")
08  if result == True:
09      print("This string is long enough.")
10  else:
11      print("This string is too short.")
"""