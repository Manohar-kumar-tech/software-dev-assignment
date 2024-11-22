def rmDup(list):
    unique_list = []
    for i in list:
        found = False
        for j in unique_list:
            if i == j:
                found = True
                continue
        if not found:
                unique_list.append(i)    
    return unique_list    
    
l = [4, 8, 2, 11, 5, 16, 1, 20, 100, 200, 100, 50, 999]

result = rmDup(l)
print(f"unique number in the list is {result}")