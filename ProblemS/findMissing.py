# Problem - A array contain number 1 to n, but one number is mssing. find out which one is

def findMissing(arr, n):
    total = n * (n+1) / 2
    actual_sum = sum(arr)
    return total - actual_sum
a = [1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12]
n = 12
print("Missing Number is: ", findMissing(a, n))