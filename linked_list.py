#creating Node class
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

#creating Llist class
class Llist:
    def __init__(self):
        self.head = None
    # function to travel list 
    def traversal(self):
        if self.head == None:
            print('List is empty')
        else:
            a = self.head
            while a != None:
                print(a.data, end= '  ')
                a = a.next 
   
n1 = Node(8)
l1 = Llist()
l1.head = n1
n2 = Node(24)
n1.next = n2
n3 = Node(10)
n2.next =n3
n4 = Node(40)
n3.next = n4
l1.traversal()
