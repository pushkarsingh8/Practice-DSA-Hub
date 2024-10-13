#Make a Linked List:-

class Node:
    #Making a Constructor for Make a node 
    def __init__(self,value):
        self.data = value
        self.next = None
        
    
    
a = Node(5)
b = Node(8)
c = Node(9)
a.next = b
b.next = c

print(id(a))