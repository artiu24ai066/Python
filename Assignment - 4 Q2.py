t=int(input("Enter the number of test cases:"))
import math
for i in range(t):
    count=0
    A=int(input("Enter first number:"))
    B=int(input("Enter second number:"))
    for i in range(A, B+1):
        root=math.sqrt(i)
        if(int(root)**2==i):
            count+=1
    print("Number of square integers:", count)