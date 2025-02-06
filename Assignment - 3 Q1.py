def digital_root(n):
    while(n//10!=0):
        sum=0
        while(n!=0):
            remainder=n%10
            sum=sum+remainder
            n=n//10
        n=sum
    print("Digital root:", n)

n=int(input("Enter a number:"))
digital_root(n)
