systemMenu = {"Chicken":45, "Pork":40, "Meat":50, "Shrimp":45}
menuList = []

while True:
    menuName = input("Please Enter Menu : ")
    if (menuName.lower() == "exit"):
        break
    else:
        menuList.append([menuName, systemMenu[menuName]])

def showBill():
    print("----My Food----")
    sumPrice = 0
    for i in range(len(menuList)):
        print(menuList[i][0], ":", menuList[i][1], "THB")
        sumPrice += menuList[i][1]
    print("Total Price : ", sumPrice, "THB")
        
showBill()