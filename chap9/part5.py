class delievery:
    """Class defines a delievery package"""
    item = ""
    name = ""
    address = ""

def addnew():
    customer = input("Customer name:") #name
    place = input("Delievery address:") #address
    stuff = input("What is the package: ") # item

    packet = delievery()
    packet.item = stuff
    packet.name = customer
    packet.address = place
    return packet

def main():

    round = []
    total = int(input("How many packages?:"))

    for i in range(0, total):
        deliever = addnew()
        round.append(deliever)

    print("Drop-off places:")

    for i in range(0, total):
        print(round[i].name + ":" + round[i].address + ":" + round[i].item)

if __name__ == "__main__":
    main()