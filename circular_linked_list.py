class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
    
class Circular_Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def insert(self, data):
        node = Node(data, next = None)
        
        self.head = self.tail = node
    
    def insert_at_beg(self, data):
        node = Node(data, next = None)
        node.next = self.head
        self.head = node
        self.tail.next = self.head
        
    def insert_at_end(self, data):
        node = Node(data, next = None)
        itr = self.head
        while itr != self.tail:
            itr = itr.next
        self.tail.next = node
        self.tail = node
        self.tail.next = self.head
        
    def get_length(self):
        count = 0
        itr = self.head
        while itr.next == self.head:
            count = count + 1
            itr = itr.next
        return count
        
    def insert_at(self, data, index):
        node = Node(data, next = None)
        
        if index < 0:
            raise Exception("Out of range")
        
        if index == 0:
            node.next = self.head
            self.head = node
            self.tail.next = self.head
        if index == self.get_length() - 1:
            node = None(data, next = None)
            
            itr = self.head
            while itr:
                if itr.next == self.tail:
                    itr.next = node
                    node.next = self.tail
                    break
                itr = itr.next
        else:
            itr = self.head
            count = 0
            while itr:
                if count == index - 1:
                    node.next = itr.next
                    itr.next = node
                    break
                itr = itr.next
                count = count + 1
                
    def remove(self, data_to_remove):
        
        if data_to_remove == self.head.data:
                self.head = self.head.next
                self.tail.next = self.head
        if data_to_remove == self.tail.data:
            itr = self.head
            while itr.next != self.tail:
                
                itr = itr.next
            self.tail = itr
            self.tail.next = self.head
            
        else:
            itr = self.head
            while itr.next.data != data_to_remove:
                itr.next = itr.next.next
                break
            itr = itr.next
    
    def display(self):
        itr = self.head
        while itr.next != self.head:
            print(itr.data)
            itr = itr.next
        print(itr.data)
            
            
l = Circular_Linked_List()
l.insert(1)
l.insert_at_beg(2)
l.insert_at_beg(3)
l.insert_at_end(6)

l.insert_at(10, 2)
l.display()
print("new list")
l.remove(10)
l.display()
        
            