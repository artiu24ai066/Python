n=[]
t=int(input("Enter number of cases:"))
for i in range(t):
    n.append(int(input("Enter any number:")))

for i in range(t):
    print(n[i])

count=0
for i in range(t):
    temp=n[i]
    while(temp!=0):
        q=temp%10
        if n[i]%q==0:
            count+=1
        temp=temp//10
    print("Count = ", count)
    count=0
