L=int(input("Enter first number:"))
R=int(input("Enter second number:"))
XOR=[]

for i in range(L, R+1):
    for j in range(L, R+1):
        XOR.append(i^j)
print(max(XOR))
