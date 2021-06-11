import random
lst=[]
lst2=[]
num=0
a=0
for i in range(30):
    lst.append(random.randint(-100,100))
print(lst)
for i in range(30):
    if lst[i]==max(lst):
        num=i
print("Max element:", max(lst))
print("Index of a max element:", num)

for i in range(30):
    if (lst[i]%2)!=0:
        lst2.append(lst[i])
        a=1
if a==0:
    print("There are no odd numbers")
print("A list of odd numbers from the source list:\n",sorted(lst2,reverse=True))


