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
            return
            
        curr = self.head
        
        while curr.next != None:
            curr = curr.next
            
        curr.next = new_node
        
        self.n = self.n + 1
        
        
    def insert_after(self,after,value):
        
        new_node = Node(value)
        curr = self.head
     
        while curr != None:
            if curr.data == after:
                break
            curr = curr.next 
            
        if curr != None:
            new_node.next = curr.next  #make connection after 3 value store address in new node
            curr.next = new_node 
            self.n +=1
        
        else:
            return "Item Not Found" 
            
         
        
        



L = LinkedList()
L.insert_head(1)
L.insert_head(2)
L.insert_head(3)
L.insert_head(4)
L.append(4)

L.insert_after(1,50)



print(L)