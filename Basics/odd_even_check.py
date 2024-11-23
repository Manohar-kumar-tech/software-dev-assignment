def check(num):
    if num % 2 == 0:
        print(f"Number {num} is even")
    else:
        print(f"Number {num} is odd")
        

try:
    num = int(input("Enter a number to check Odd or Even: "))
    check(num)
except:
    print("Invalid input! Please try again...")