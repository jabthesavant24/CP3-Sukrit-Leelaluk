print("------Welcome to ishop!!!------")
print("Please input Username & Password")
usernameInput = input("Username : ")
passwordInput = input("Password : ")
if (usernameInput == "admin") and (passwordInput == "admin"):
    print("Success!!")
    print("------Welcome to ishop!!!------")
    print("Please selected your products")
    price1 = 99
    price2 = 55
    price3 = 40
    price4 = 30
    print("1: iPhone ", price1, "$")
    print("2: iPad ", price2, "$")
    print("3: iPod ", price3, "$")
    print("4: Samsung ", price4, "$")
    userSelected = int(input("Please input a number of product : "))
    if userSelected == 1:
        amount = int(input("Please input amount : "))
        print("Total : ", price1*amount, "$")
    elif userSelected == 2:
        amount = int(input("Please input amount : "))
        print("Total : ", price2*amount, "$")
    elif userSelected == 3:
        amount = int(input("Please input amount : "))
        print("Total : ", price3*amount, "$")
    elif userSelected == 4:
        amount = int(input("Please input amount : "))
        print("Total : ", price4*amount, "$")
    else:
        print("Error")
        print("Goodbye!!")
else:
    print("Error")
    print("Goodbye!!")