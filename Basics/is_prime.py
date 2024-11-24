import math

def is_prime(num):
    if num <=1:
        return False
    for i in range(2, int(math.sqrt(num)) +1):
        if num % i ==0:
            return False
    return True
    
    
try:
    num = int(input("Enter a number to check prime or not: "))
    if is_prime(num):
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number")
except:
    print("Invalid input! Try again please...")