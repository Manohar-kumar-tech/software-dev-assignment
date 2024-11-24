# Problem - print number 1 to n, if number is divisible by 3 print "Fizz", if divisible by 5 print "Buzz", if divisible by both print "FizzBuzz"

def fizzBuzz(n):
    for i in range(1, n+1):
        if i % 3 ==0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
            
fizzBuzz(15)