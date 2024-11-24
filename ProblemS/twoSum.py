# Find the two number in an array that sum to a target value

#  input: [2,7, 11, 15], output: [0, 1] for target: 9

def twoSum(arr, target):
    seen = {}
    for i, num in enumerate(arr):
        diff = target - num
        if diff in seen:
            return [seen[diff]]
        seen[num] = i
    return []

arr = [11, 12,  13, 14, 15, 16, 17, 18, 19]

targrt = 24

print(twoSum(arr, targrt))