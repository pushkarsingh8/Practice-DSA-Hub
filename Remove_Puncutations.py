#Remove Puncutation in Linked List:-

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
        
        
    def add(self,value):
        new_node = Node(value)
        
        if self.head == None:
            new_node = self.head
            return new_node
        else:
            curr = self.head
            while curr!=None:
                curr = curr.next
                
            curr.next = new_node
            self.n+=1
            


    def remove_punc(self):
        curr = self.head
        
        while curr != None:
            if curr.data == '*' or curr.data == '/':
                curr.data = ' '
                if curr.next.data == '*' or curr.next.data == '/' :
                    curr.next.next.data = curr.next.next.data.upper()
                    curr.next = curr.next.next
            curr = curr.next
            
            
            
l = LinkedList()

l.add(5)
print(l)