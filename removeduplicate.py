def removeDuplicates(head):
    temp1= head
    temp2 = head.next
    while temp2!=None:
        if temp1.data == temp2.data:
            temp2 = temp2.next
            temp1.next = temp2
        else:
            temp1 = temp2
            temp2 = temp2.next




class Node:
    def __init__(self,data= None):
        self.data = data
        self.next = None

def append(head,data):
    if head.data == None:
        head.data = data
    else:
        temp = head
        while temp.next!=None:
            temp = temp.next
        temp.next = Node(data)

def display(head):
    print('Output linkedlist:', end = ' ')
    temp = head
    while temp!=None:
        print(temp.data,end =' ')
        temp = temp.next

print('Enter linked list: ', end = ' ')
a = [int(i) for i in input().split(' ')]
head = Node()
for i in a:
    append(head,i)

removeDuplicates(head)
display(head)