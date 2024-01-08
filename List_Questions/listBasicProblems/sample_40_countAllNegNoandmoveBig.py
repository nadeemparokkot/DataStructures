# 43. Write a program to count all negative numbers and move to beginning of a given array and find average of non-negative numbers
neg=[]
pos=[]
lst=[5,14,-8,21,-4,-7,9,15,-16,18]
c=0
for i in lst:
    if i<0:
        c+=1
        neg.append(i)
    else:
        pos.append(i)
lst=neg+pos
avg=sum(pos)/len(pos)
print(lst)
print(c)
print(avg)