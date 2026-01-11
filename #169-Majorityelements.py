def majele(nums):
    count=0
    candidate=None
    for num in nums:
        if count==0:
            candidate=num
        count+=1 if num==candidate else -1
    return candidate

print(majele([3,2,3]))
print(majele([2,2,1,1,1,2,2]))