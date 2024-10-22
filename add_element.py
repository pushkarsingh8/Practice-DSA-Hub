class Node:
    def __init__(self,value):
        self.data = value
        self.next = None
        
class linked_list:
    def __init__(self):
        self.head = None
        self.n = 0
        
        
    def __str__(self):
        curr = self.head
        result = ''
        while curr!=None:
            result = result + str(curr.data) + '->'
            curr = curr.next
            
        return result [:-2]
    
    def add(self,value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            return new_node
        
        else:
            
            curr = self.head
            while curr.next!= None:
            
                curr = curr.next
            
            curr.next = new_node #add node in last of node


l = linked_list()
l.add(5)
l.add(6)
l.add(7)
l.add(8)
print(l)