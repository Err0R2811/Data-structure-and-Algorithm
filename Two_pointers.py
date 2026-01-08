def two_pointers(arr,target):
    left = 0
    right=len(arr)-1
    while left<right:
        c_sum=arr[left]+arr[right]
        if c_sum==target:
            return [left,right]
        elif c_sum<target:
            left+=1
        else:
            right-=1
    return []

arr=[1,2,3,4,5,6]
target=10
print(two_pointers(arr,target))

    