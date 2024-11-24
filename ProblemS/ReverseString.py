# Problem - reverse a string without using buit-in function

# input = "Hello", output = "olloeH"

def reverse(input):
    result = ""
    for char in input:
        result = char + result
    return result

s = "Hello"

print(f"Revsers of '{s}' is : ", reverse(s))