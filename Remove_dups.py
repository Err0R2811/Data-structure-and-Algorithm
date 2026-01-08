def rem_dups(arr):
    i=0
    j=1
    while j<len(arr):
        if arr[i]==arr[j]:
            j+=1
        elif arr[i]!=arr[j]:
            i+=1
            arr[i]=arr[j]
            j+=1
    return arr[:i+1]

arr=[1,1,2,2,3,3,4,4,5,5,6,6]
print(rem_dups(arr))