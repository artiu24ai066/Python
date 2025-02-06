t=int(input("Enter the number of test cases:"))
a=[]
N=[]

for i in range(t):
    a.append(int(input(f"Enter the number of cycles of test case{i+1}:")))
for i in a:
    height=1
    for j in range(1, i+1):
        if(j%2==0):
            height+=1
        else:
            height*=2
    N.append(height)
    print(f"After {i} cycles height={height}")
print(N)
