arr=[30,2,41,56,12,11,22,41]
n=len(arr)
for i in range(1,n):
    curr=arr[i]
    prev=i-1
    while prev>=0 and arr[prev]>curr:
        arr[prev+1]=arr[prev]
        prev-=1
    arr[prev+1]=curr
print(arr)