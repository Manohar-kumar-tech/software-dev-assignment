def large(list):
    max_item = list[0]
    for i in list:
        if max_item < i:
            max_item = i
        continue
    return max_item
    
    
l = [4, 8, 2, 11, 5, 16, 1, 20, 100, 200, 100, 500, 999]

result = large(l)
print(f"largest number in the list is {result}")