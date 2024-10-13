#Make a Linked List:-

class Node:
    #Making a Constructor for Make a node 
    def __init__(self,value):
        self.data = value
        self.next = None
        
#These Objects   
a = Node(1)
b = Node(2)
c = Node(3)

#Making connection of each Nodes
a.next = b
b.next = c

result = ""
curr = a

while curr != None:
    result = result + str(curr.data) + "->"  
    curr = curr.next

print(result[:-2])    