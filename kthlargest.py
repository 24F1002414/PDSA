
def kthlargest(root):
    global count,res
    if root.right != None:
        find_kth_largest(root.right,k)
        count +=1
        if count == k:
            res = root.value
            return
        find_kth_largest(root.left,k) 
count =0 
res = -1

def find_kth_largest(root,k):
    kthlargest(root)
    return res