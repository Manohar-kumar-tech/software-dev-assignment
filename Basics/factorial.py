def factorial(num):
    fact = 1
    if num < 0:
        print("Negative number does not have factorial.")
    elif num ==0 or num == 1:
        return 1
    else:
        for i in range (1, num +1):
            fact *= i
        return fact

num = int(input("Enter a Number to get factorial: "))
result = factorial(num)

print(f"The factorial of number {num} is {result}")