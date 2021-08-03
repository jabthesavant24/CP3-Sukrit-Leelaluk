class Customer:
    name = ""
    lastName = ""
    age = 0

    def addCart(self):
        print("Added to ", self.name, self.lastName, "'s cart")

customer1 = Customer()
customer1.name = "Kittikorn"
customer1.lastName = "Prasetsak"
customer1.addCart()

customer2 = Customer()
customer2.name = "Trithep"
customer2.lastName = "Ratanapipop"
customer2.addCart()

customer3 = Customer()
customer3.name = "Kanokwan"
customer3.lastName = "Muttamara"
customer3.addCart()

customer4 = Customer()
customer4.name = "Tony"
customer4.lastName = "Woodsome"
customer4.addCart()