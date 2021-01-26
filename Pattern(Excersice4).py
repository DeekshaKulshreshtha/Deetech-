num1 = int(input("Enter the number of rows : "))
num2 = bool(int(input("Enter the second number : ")))
if(num2 == True):
    for i in range(num1):
        for j in range(i):
            print("*", end = "")
        print("\n")
else:
    for i in range(num1):
        for j in range(num1,0+i,-1):
            print("*", end = "")
        print("\n")
