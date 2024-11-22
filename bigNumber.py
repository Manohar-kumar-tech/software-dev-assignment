def isBig(num1, num2, num3):
    if num1 > num2:
        if num1 > num3:
            return num1
        else:
            return num3
    elif num2 > num1:
        if num2 > num3:
            return num2
        else:
            return num3
        
try:
    num1 = int(input("Enter First numbers : "))
    num2 = int(input("Enter Second numbers : "))
    num3 = int(input("Enter third numbers : "))
    result = isBig(num1, num2, num3)
    print(f"The largest number is {result}")
except:
    print("Invalid input! Please try again...")