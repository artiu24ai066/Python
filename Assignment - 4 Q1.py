def min_operations_to_palindrome(s):
    n = len(s)
    operations = 0

    for i in range(n // 2):
        left_char = s[i]
        right_char = s[n - i - 1]
        
        if left_char != right_char:
            operations += abs(ord(left_char) - ord(right_char))
 
    return operations

T = int(input("Enter no. of test cases:"))
for _ in range(T):
    s = input("Enter a word:").strip()
    print(min_operations_to_palindrome(s))