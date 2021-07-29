menuList = []
priceList = []
while True:
    menuName = input("Please Enter Menu : ")
    if (menuName.lower() == "exit"):
        break
    else:
        menuPrice = input("Price : ")
        menuList.append(menuName)
        priceList.append(menuPrice)

def showBill():
    print("----My Food----")
    sumTotal = 0
    for i in range(len(menuList)):
        print(menuList[i], ":",priceList[i], "THB")
        sumTotal += int(priceList[i])
    print("Total price:", sumTotal, "THB")

showBill()