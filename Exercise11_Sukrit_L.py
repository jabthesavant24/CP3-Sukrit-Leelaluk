print("------Create a pyramid------")
numberInput = int(input("Please input number : "))
blankSpace = numberInput
for i in range(numberInput):
    print((" "*(blankSpace-1-i))+((2*i)+1)*"*")