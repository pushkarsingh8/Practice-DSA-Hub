#Making a node in Linked List:-

class Node:
    def __init__(self,value):
        self.data = value
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.n = 0
        
        
    def __str__(self):
        
        curr = self.head
        result = ""
        while curr != None:

            result = result+ str(curr.data) +"->"
            #iteration
            curr = curr.next
        return result[:-2]
    
    
    def __len__(self):
        return self.n
            
        
        
    def insert_head(self,value):
        
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.n = self.n+1
        
    def append(self,value):
        new_node = Node(value)
        if self.head == None:
            self.head  = new_node
            self.n = self.n+1
            
        curr = self.head
        
        while curr.next != None:
            curr = curr.next
            
        curr.next = new_node
         
        
        



L = LinkedList()
L.insert_head(1)
L.insert_head(2)
L.insert_head(3)
L.insert_head(4)
L.append(4)


print(L)