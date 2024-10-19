#Find a mximum value and replace them in new value:-
class Node:
    
    def __init__(self,value):
        self.data =  value
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
        self.n = 0
        
    def __len__(self):
        return self.n
        
    def __str__(self):
        curr = self.head
        result = ""
        while curr!=None:
            result = result + str(curr.data) + "->"
            curr = curr.next
        return result[:-2] if result else 'Empty LL'
        
                        
    def insert_head(self,value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        
        self.n +=1
        
    
    def replace_max(self,value):
        curr = self.head
        max = curr
        
        while curr!=None:
            if curr.data > max.data:
                max = curr
            curr = curr.next
        max.data = value
                        
                





l = LinkedList()
l.insert_head(5)
l.insert_head(15)
l.insert_head(50)
l.insert_head(52)
l.insert_head(8)
l.replace_max(12)

print(l)


