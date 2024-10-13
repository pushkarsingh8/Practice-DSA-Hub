#Make a Linked List:-

class Node:
    #Making a Constructor for Make a node 
    def __init__(self,value):
        self.data = value
        self.next = None
class Linked_List:      
    def __init__(self):
        head = None
        self.n = 0  
        
    def __str__(self):
        curr = a
        result = ""
        
        while curr != None:
            
            result = result + str(curr.data) + "->"
            curr = curr.next
        return result[:-2]     

        
#These Objects   
a = Node(1)
b = Node(2)
c = Node(3)

#Making connection of each Nodes
a.next = b
b.next = c

l = Linked_List()

print(l)