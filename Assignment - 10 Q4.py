import numpy as np

def format_array(arr, width=15, fillchar='_'):
    centered = np.array([s.center(width, fillchar) for s in arr])
    left_justified = np.array([s.ljust(width, fillchar) for s in arr])
    right_justified = np.array([s.rjust(width, fillchar) for s in arr])
    
    return centered, left_justified, right_justified

n = int(input("Enter number of elements: "))
user_input = [input(f"Enter string {i + 1}: ") for i in range(n)]
arr = np.array(user_input)

centered, left_justified, right_justified = format_array(arr)

print("\nCentered:\n", centered)
print("\nLeft Justified:\n", left_justified)
print("\nRight Justified:\n", right_justified)
