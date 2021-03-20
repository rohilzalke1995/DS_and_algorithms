class Node:
    def __init__(self, data = None, prev = None, next = None):
        self.data = data
        self.prev = prev
        self.next = next
    
class DoubleLinkedList:
    def __init__(self):
        self.head = None
        
    def insert_at_begin(self, data):
        
        if self.head is None:
            self.head = Node(data, None, None)
            self.head.prev = None
            self.head.next = None
        else:
            node = Node(data, prev = None, next = None)
            node.next = self.head
            self.head.prev = node
            node.prev = None
            self.head = node
            
    def insert_at_end(self, data):
            node = Node(data, prev = None, next = None)
            itr = self.head
            while itr.next:
                
                itr = itr.next
            itr.next = node
            node.prev = itr.next
            node.next = None
    
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count = count + 1
            itr = itr.next
        return count
    
    def insert_at(self, data, index):
        node = Node(data, prev = None, next = None)
        count = 0
        itr = self.head
        while itr:
            if count == index -1:
                node.next = itr.next
                itr.next.prev = node
                itr.next = node
                node.prev = itr
                break
                
            itr = itr.next
            count = count + 1
            
    def remove(self, data_to_remove):
        itr = self.head
        while itr:
            if itr.data == data_to_remove:
                itr.next.prev = itr.prev
                itr.prev.next = itr.next
            itr = itr.next
        
    def display(self):
        if self.head is None:
            print("The list is empty")
        itr = self.head
        listr = ''
        while itr:
            listr = listr + str(itr.data) + '<--->'
            itr = itr.next
        print(listr)
        
l1 = DoubleLinkedList()
    
l1.insert_at_begin(6)
l1.insert_at_begin(16)
l1.insert_at_end(20)
l1.insert_at(40, 2)
l1.get_length()
l1.display()
l1.remove(40)
l1.display()
      
    