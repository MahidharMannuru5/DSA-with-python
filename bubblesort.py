def bsort(arr):
    for i in range(len(arr)):
        for i in range(len(arr)-1):
            if arr[i+1]<arr[i]:
                arr[i+1],arr[i]=arr[i],arr[i+1]
    return arr

arr=[5,4,3,2,1]
ans=bsort(arr)
print(ans)
    
