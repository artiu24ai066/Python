def fibo(a):
    for i in a:
        t1=0
        t2=1
        k=0
        if(i==t1 or t2==i):
            k=1
        else:
            while(i>t2):
                sum=t1+t2
                t1=t2
                t2=sum
                if(t2==i):
                    k=1
                    break
        if(k==1):
            print(f"Element {i} is fibo")
        else:
            print(f"Element {i} is not fibo")    

a=[]
terms=int(input(("Enter the number of terms:")))
for i in range(terms):
    n=int(input(("Enter your number:")))
    a.append(n)
fibo(a)
