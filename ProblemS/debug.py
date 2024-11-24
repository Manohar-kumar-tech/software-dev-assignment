# Debugging -Process of finding and fixing problem in code. These problem can  be ...
    # 1. Syntax Error
    # 2. runtime Error 
    # 3. Logical Error 
    
# Process -
    # 1. Understand the problem - clearly define what is going wrong
    # 2. Reproduce the bug - Ensure the issue happens consistently
    # 3. Investigate - identify the source of the issue
    # 4. Fix - Apply the solution
    # 5. Test - verify the problem is resolved without introducing new bug
    
# Tools 
    # 1. print() - track variable and flow of program
    # 2. Braekpoint - In IDE use breakppoint
    # 3. Error message - always read and understand the error trackback or log
    
# e.g. 1
# def division(a, b):
#     # After reading error message 
#     if b == 0:
#         print("Division by zero can not be perform")
#         return None
        
#     return a/b

# print(division(10, 5))
# print(division(5, 0))


# e.g. 2
def calculate_area(length, width):
    return length * width

print(calculate_area(5, 10))
    