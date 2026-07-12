# #E.g1
# class Animal:
#     def eat(self):
#         print("Eating...")


# class Dog(Animal):
#     def bark(self):
#         print("Woof!")

# dog = Dog()
# dog.eat()     # Kế thừa từ Animal
# dog.bark()    # Method của Dog



#e.g2
class Customer:
    name = "John Johnsson"
    total = 1000
    paymenttype = "Masterexpress"
    number = "1234-5678-9012345"

    def printout(self):
        print("Name:", self.name)
        print("Total:", self.total)
        print("Payment type:", self.paymenttype)
        print("Card/Bill number:", self.number)
        


class Regular(Customer):
    bonuscard = "ABCD-1234"
    bonusaccount = 0

    def bonusdata(self):
        print("This client has", self.bonusaccount, "bonus points.")



Dave = Regular()
Dave.name = "Dave Davidsson"
Dave.printout()
Dave.bonusdata()