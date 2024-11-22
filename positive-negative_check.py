
def check(num):
    if num > 0:
        print(F"{num} is a positive number.")
    elif num <0:
        print(F"{num} is a negative Number.")
    else:
        print(F"{num} is zero")

try:
    num = int(input("Enter a number to check: "))
    check(num)
except:
    print("Invalid input! Please try again")
    exit()
