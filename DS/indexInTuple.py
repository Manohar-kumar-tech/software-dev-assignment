def findIndex(element, tuple):
    for i in range(len(tuple)):
        if tuple[i] == element:
            return i
    return -1
    

t = (1, 2, 10, 20, 30, 40)
target =30 

result = findIndex(target, t)
print(f"The give element fond at index {result}")
