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
        return result[:-2] if result else 'Empty LL'
    
    
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
        
    def clear(self):
        self.head = None
        self.n = 0
        
        
    def delete_head(self):
        #delete a node to starting point
        if self.head == None:
            return 'Empty LL'
        self.head = self.head.next
        self.n-=1
        
        
    def pop(self):
        
        #check
        if self.head == None:
            return "empty LL"
        
        curr = self.head
            
        
        # if curr.next == none hai jo ki next node nhi hai so you delete a head 
        if curr.next == None:
            return self.delete_head()
            
        while curr.next.next != None:
            curr = curr.next
            
        #2nd last node in LL
        curr.next = None   
        self.n-=1
        
        
        
        
    def remove(self,value):
        curr = self.head
        
        if self.head == None:
            print( 'Empty LL')
            return
        
        
        if self.head.data == value:

            return self.delete_head()
        

        
        while curr.next != None:
            
            if curr.next.data == value:
                break
                    
            curr = curr.next
                
                
        if curr.next == None:
             print("Not found")
             
        else:
            curr.next = curr.next.next
            self.n = self.n-1
            
            
            
    def search(self,item):
        curr = self.head
        pos = 0
        
        while curr != None:
            if curr.data == item:
                return pos
            curr = curr.next
            pos = pos+1
            
        return "Not found"

        
            
         
        
        



L = LinkedList()

L.insert_head(10)
L.insert_after(10,9)
L.insert_after(9,8)
L.insert_after(8,5)

print(L.search(5)) 


print("Output",L)