def binarysearch(L,v):
    low =0 
    high = len(L)-1
    while low <= high:
        mid = (low+high)//2
        if L[mid]<v:
            low = mid+1
        elif L[mid]>v:
            high = mid-1
        else:
            return mid
    return False
 
L = [1,2,4,5,33,223,999]

print(binarysearch(L,100))
print(binarysearch(L,999))







def peak_unimodal(A):
    low,high = 0,len(A)-1
    while low<high:
        mid = (low+high)//2
        if A[mid]<A[mid+1]:
            low = mid+1
        else:
            high = mid
    return low