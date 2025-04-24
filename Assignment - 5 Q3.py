def next_permutation(word):
    word = list(word)  
    n = len(word)
    i = n - 2
    while i >= 0 and word[i] >= word[i + 1]:
        i -= 1

    if i == -1:
        return "no answer" 

    j = n - 1
    while word[j] <= word[i]:
        j -= 1

    word[i], word[j] = word[j], word[i]

    word = word[:i+1] + word[i+1:][::-1]

    return "".join(word) 

t = int(input("Enter the number of test cases:"))  
for i in range(t):
    w = input("Enter a word:").strip()
    print(next_permutation(w))
