def division(num1, num2):
    return num1/num2

try:
    a = int(input("Enter First number to be divide: "))
    b = int(input("Enter second number to  divide: "))
    result = division(a, b)
except ZeroDivisionError:
    print("Number can not be divide by the zero! Please try again... ")
except ValueError:
    print("Pleas enter a valid number...")
else:
    print(f"The result of number {a} divide by {b} is {result}")
finally:
    print("Execution Completed. ")