num = int(input("Enter a Number to get factorial: "))


def factorial(num):
    fact = 1
    if num < 0:
        print("Negative number does not have factorial.")
    elif num ==0 or num == 1:
        print(F"factorial of number {num} is 0")
    else:
        for i in range (1, num +1):
            fact *= i
        return print(F"The facorail of number {num} is {fact}")


print(factorial(num))