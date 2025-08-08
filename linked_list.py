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
    # insert at start
    def insert_at_start(self,data):
        nb = Node(data)
        nb.next = self.head
        self.head = nb
    
    #insert at end 
    def insert_at_end(self,data):
        ne = Node(data)
        a = self.head
        while a.next is not None:
            a = a.next
        a.next = ne
    
    # insert at nth node
    def insert_at_n(self,data,position):
        nib = Node(data)
        a = self.head
        for i in range (1,position-1):
            a = a.next 
        nib.next = a.next
        a.next = nib
    def delete_at_start(self):
        a = self.head
        self.head = a.next
        a.next = None
    def delete_at_end(self):
        prev = self.head
        a = prev.next
        while a.next is not None:
            a = a.next
            prev= prev.next
        prev.next = None
    def delete_at_n(self,position):
        prev = self.head
        a = prev.next
        for i in range(1,position-1):
            a = a.next
            prev = prev.next
        prev.next = a.next
        a.next = None



n1 = Node(8)
l1 = Llist()
l1.head = n1
n2 = Node(24)
n1.next = n2
n3 = Node(10)
n2.next =n3
n4 = Node(40)
n3.next = n4
# l1.insert_at_end(200)
l1.insert_at_n(45,3)
# l1.delete_at_start()
# l1.delete_at_end()
# l1.delete_at_n(3)
l1.traversal()


