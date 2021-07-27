def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "1234":
        return showMenu()
    while (usernameInput != "admin") or (passwordInput != "1234"):
        usernameInput = input("Username : ")
        passwordInput = input("Password : ")
        if usernameInput == "admin" and passwordInput == "1234":
            return showMenu()

def showMenu():
    print("--------iShop--------")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    menuSelect()

def menuSelect():
    userSelected = int(input(">>"))
    if userSelected == 1:
        totalPrice = float(input("Please input a total price : "))
        return vatCalculate(totalPrice)
    elif userSelected == 2:
        return priceCalculate()
    else:
        return print("Error Good Bye!!")

def vatCalculate(totalPrice):
    vat = 7
    result = totalPrice + (totalPrice * (vat/100))
    return print(result)

def priceCalculate():
    price1 = float(input("First Product Price : "))
    price2 = float(input("Second Product Price : "))
    return vatCalculate(price1+price2)

login()