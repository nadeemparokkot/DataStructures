def quickSort(array,left,right):
    if left<right:
        partition_pos=partition(array,left,right)
        quickSort(array,left,partition_pos-1)
        quickSort(array,partition_pos+1,right)

def partition(array,left,right):
    i=left
    j=right-1
    pivot=array[right]

    while i<j:
        while i<right and array[i]<pivot:
            i+=1
        while j>left and array[j]>=pivot:
            j-=1
        if i<j:
            array[i],array[j]=array[j],array[i]
    if array[i]>pivot:
        array[i],array[right]=array[right],array[i]
    return i
array=[2,4,16,11,21,25,32,62,41]
# array=[22,11,88,66,55,77,33,44]
quickSort(array,0,len(array)-1)
print(array)