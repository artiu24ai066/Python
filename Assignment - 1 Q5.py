list=[]
for i in range(3):
    list.append(input("Enter student name:"))
print(list)
for i in range(3):
    list[i]=list[i][::-1]
for i in range(3):
    print(list[i])
