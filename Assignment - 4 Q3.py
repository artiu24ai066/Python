alphabets="abcdefghijklmnopqrstuvwxyz"
s=input("Enter any sentence:")
for i in alphabets:
    k=1
    if i not in s.lower():
        k=0
        
if(k==1):
    print("PANGRAM")
else:
    print("Not a PANGRAM")