def vatCalculate(totalPrice):
    result = totalPrice + (totalPrice * (7/100))
    return result

numberInput = float(input("Please input a total price (THB): "))
print("Taotal vat is : ", vatCalculate(numberInput), "THB")