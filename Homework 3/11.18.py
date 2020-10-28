#Caleb Covington
#1606086
integers = input().split()
non_negative=[]
for num in integers:
    num=int(num)
    if num>=0:
        non_negative.append(num)
non_negative.sort()
for i in non_negative:
    print(i,end=" ")
