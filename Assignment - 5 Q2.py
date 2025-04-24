def pieces(K):
    if(K%2==0):
        K=K//2
        K=K*K
        return K
    else:
        K=K//2
        K=K*(K+1)
        return K        

T=int(input("Enter the number of test cases:"))
for i in range(T):
    K=int(input("Enter the number of times you want to cut the chocolate:"))
    piece=pieces(K)
    print(piece)
