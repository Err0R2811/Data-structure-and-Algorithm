def con_dup(nums,k):
    d={}
    for i in range(len(nums)):
        if nums[i] in d and abs(i-d[nums[i]])<=k:
            return True
        d[nums[i]]=i
    return False

nums=[1,2,3,1]
k=3
print(con_dup(nums,k))