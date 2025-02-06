word=input("Enter a word:")
final_word=""
for i, char in enumerate(word):
    if i%2!=0:
        final_word+=char.upper()
    else:
        final_word+=char.lower()

print(final_word)
