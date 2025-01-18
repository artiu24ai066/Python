import random
random_list=[]
for i in range(100):
    random_list.append(random.randint(0,1))
max_zeroes=0
current_zeroes=0
for num in random_list:
    if num==0:
        current_zeroes+=1
    else:
        max_zeroes=max(max_zeroes, current_zeroes)
        current_zeroes=0

print("Random list:",random_list)
print("Longest run of zeroes:", max_zeroes)
