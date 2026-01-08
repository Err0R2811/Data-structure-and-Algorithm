#Prefix_sum

# def presum(arr):
#     arr1=[0]*len(arr)
#     arr1[0]=arr[0]
#     for i in range(1,len(arr)):
#         arr1[i]=arr[i-1]+arr[i]
#     return arr1

# arr=[1,2,3,4,5]

# print(presum(arr))

#sliding_window
"""
def slide_win(arr,k):
    w=0
    m=0
    for i in range(k):
        w+=arr[i]
    
    m=w

    for i in range(k,len(arr)):
        w=w-arr[i-1]+arr[i]
        m=max(w,m)
    return m

k=6
arr=[1,2,3,4,5,6,7,8,9,10]
print(slide_win(arr,k))
"""
"""
def presum(arr):
    arr1=[0]*len(arr)
    arr1[0]=arr[0]
    for i in range(1,len(arr)):
        arr1[i]=arr[i-1]+arr[i]
    return arr1

arr=[9,8,7,6,5,4,3,2,1]
print(presum(arr))
"""
# def slide_window(arr,k):
#     w=0
#     m=0
#     for i in range(k):
#         w+=arr[i]
#     m=w
#     for i in range(k,len(arr)):
#         w=w-arr[i-1]+arr[i]
#         m=max(w,m)
#     return m
# k=2
# arr=[1,2,3,4,5]
# print(slide_window(arr,k))