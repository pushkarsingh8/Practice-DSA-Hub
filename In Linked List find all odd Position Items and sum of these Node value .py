#In Linked List find all odd Position Items and sum of these Node value :-
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
    
    def insert_head(self,value):
        new_node = Node(value)
        new_node.next = self.head
        #making a new Head
        self.head = new_node
        #increatment n
        self.n += 1
        
        
    def __len__(self):
        return self.n
    
    def sum_odd_nodes(self):
        curr = self.head
        result = 0
        counter = 0
        
        while curr!=None:
            
            if counter % 2 != 0:
                
                result += curr.data
            
            counter+=1
            curr = curr.next
        
        print(result)
        
        
        
l = linked_list()


l.insert_head(2)
l.insert_head(3)
l.insert_head(4)
l.insert_head(5)
l.insert_head(6)



l.sum_odd_nodes()
print(l)
        