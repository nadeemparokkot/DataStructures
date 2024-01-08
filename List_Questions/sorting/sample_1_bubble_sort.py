arr=[30,2,41,56,12,11,22,41]
print("unsorted list1 is",arr)
for j in range(len(arr)-1):
    for i in range(len(arr)-1):#or for i in range(len(arr)-j-1):
        if arr[i]>arr[i+1]:
            arr[i],arr[i+1]=arr[i+1],arr[i]
            print(arr)
        else:
            print(arr)
    print( )
print("sorted list iis",arr)