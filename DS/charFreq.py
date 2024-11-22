def characterFrequiency(string):
    frequiency = {}
    
    for char in string:
        if char in frequiency:
            frequiency[char] += 1
        else:
            frequiency[char] = 1
    return frequiency

string = str(input("Enter your string to get frequency of cahracter: "))

result = characterFrequiency(string)

print(result)