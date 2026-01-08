def rotate(nums,k):
    n=len(nums)
    k%=n
    def reverse(nums,s,e):
        while s<e:
            nums[s],nums[e]=nums[e],nums[s]
            s+=1
            e-=1
    reverse(nums,0,n-1)
    reverse(nums,0,k-1)
    reverse(nums,k,n-1)

nums=[1,2,3,4,5,6,7]
k=3
rotate(nums,k)
print(nums)