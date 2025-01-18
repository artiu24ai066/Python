numbers=[]
for i in range(10001):
    numbers.append(i)

rem_0=[]
rem_1=[]
rem_2=[]
rem_3=[]
rem_4=[]

for i in range(10001):
    if i%5==0:
        rem_0.append(i)
    elif i%5==1:
        rem_1.append(i)
    elif i%5==2:
        rem_2.append(i)
    elif i%5==3:
        rem_3.append(i)
    else:
        rem_4.append(i)
print(rem_0)
print("\n")
print(rem_1)
print("\n")
print(rem_2)
print("\n")
print(rem_3)
print("\n")
print(rem_4)
