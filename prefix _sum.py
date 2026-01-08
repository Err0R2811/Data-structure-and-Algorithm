def pre_sum(arr):
    arr1=[0]*len(arr)
    arr1[0]=arr[0]
    for i in range(1,len(arr)):
        arr1[i]=arr1[i-1]+arr[i]
    return arr1

arr=[1,2,3,4,5]
print(pre_sum(arr))



