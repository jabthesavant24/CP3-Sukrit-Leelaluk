# temp = [[10,10],[20,10]]
# print(temp)

menuList = []

while True:
    menuName = input("Please Enter Menu : ")
    if (menuName.lower() == "exit"):
        break
    else:
        menuPrice = input("Price : ")
        menuList.append([menuName, menuPrice])

def showBill():
    print("----My Food----")
    sumTotal = 0
    for i in range(len(menuList)):
        print(menuList[i][0], ":", menuList[i][1], "THB")
        sumTotal += int(menuList[i][1])
    print("Total price : ", sumTotal, "THB" )
        
showBill()