arr=[30,2,41,56,12,11,22,41]
n=len(arr)
for i in range(n):
    min_in=i
    for j in range(i+1,n):
        if arr[j]<arr[min_in]:
            min_in=j
    arr[i],arr[min_in]=arr[min_in],arr[i]
print(arr)