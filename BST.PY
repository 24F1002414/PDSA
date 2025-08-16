# Binary search Tree
# Part -1
# Defining class

class Tree:
    #initialisation
    def __init__(self,initval = None):
        self.value = initval
        if self.value:
            self.left = Tree()
            self.right = Tree()
        else:
            self.left = None
            self.right = None
    
    #Method1 : check if empty or not
    def isempty(self):
        return self.value ==None
    
    #Method2 : check for leaf node
    def isleaf(self):
        return self.value !=None and self.left.isempty() and self.right.isempty()
    
    #Method 3: Inorder traversal(L,root,R)
    def inorder(self):
        if self.isempty():
            return []
        else:
            return self.left.inorder() + [self.value] + self.right.inorder()
        
    #Method 4 Display Tree as string
    def __str__(self):
        return str(self.inorder)
    
    #Method 5 Search a value in BST
    def find(self,v): 
        if self.isempty():
            return False
        if self.value ==v:
            return True
        if v<self.value:
            return self.left.find(v)
        if v > self.value:
            return self.right.find(v)
    
    # Find min value
    def minval(self):
        if self.left.isempty():
            return self.value
        else:
            return self.left.minval()
    
    # Find max value
    def maxval(self):
        if self.right.isempty():
            return self.value
        else:
            return self.right.maxval()
        
    #Insert operation on BST
    def insert(self,v):
        if self.isempty():
            self.value =v
            self.left = Tree()
            self.right = Tree()
        if self.value == v:
            return
        if v<self.value:
            self.left.insert(v)
        if v>self.value:
            self.right.insert(v)
            

T = Tree() 
bst = [9,8,7,6,5,4,3,2,1]
k=4
for i in bst:
    T.insert(i)

# print(f'The BST is {T.inorder()}')
# print(T.inorder())
# print("max value is", T.maxval())
# print("min value is", T.minval())
print("Is 4 present :", T.find(4))