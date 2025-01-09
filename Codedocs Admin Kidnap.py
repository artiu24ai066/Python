T=int(input("Number of test cases:"))
N=int(input("Number of boxes:"))
X=int(input("Box in which the gold coin is placed:"))
S=int(input("Number of swaps to be performed:"))
print(N, X, S)

j=0
for i in range(T):
    while j<S:
        A=int(input("Box A:"))
        B=int(input("Box B:"))
        j+=1
    if A==X:
        X=B
    elif B==X:
        X=A
guess=int(input("Guess the box in which the gold coin is present:"))
if(guess==X):
    print("You Win!")
else:
    print("You Lose :<")
