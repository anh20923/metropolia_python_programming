class Cart:
    """This class manages the shopping cart."""

    shoppingcart = []

    def addstuff(self):
        item = input("What will be added?: ")
        self.shoppingcart.append(item)

    def checkout(self):
        print("Following objects were added:")
        for i in range(len(self.shoppingcart)):
            print(self.shoppingcart[i], end=" ")


def main():
    customer = Cart()

    while True:
        selection = input("Add more or go to checkout?: ")

        if selection == "checkout":
            customer.checkout()
            break
        else:
            customer.addstuff()


if __name__ == "__main__":
    main()