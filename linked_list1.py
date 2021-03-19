class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def display(self):
        if self.head is None:
            print("The linst is empty")
            return
        
        itr = self.head
        listr = ''
        while itr:
            listr = listr + str(itr.data) + '--->'
            itr = itr.next

        print(listr)
    
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return 
        
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)
        
    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
        
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count = count + 1
            itr = itr.next
        return count
        
    def remove_element(self, index):
        count = 0
        if index < 0: 
            raise Exception("Out of range")
        if index >= self.get_length():
            raise Exception("Out of range")
        if index == 0:
            self.head = self.head.next
            
        count = 0
        itr = self.head
        while itr:
            
            if count == index - 1:
                itr.next = itr.next.next
                break
            count = count+ 1    
            itr = itr.next
            
    def insert_at(self, index, data):
        if index<0:
            raise Exception("Out of range")
        if index >= self.get_length():
            raise Exception("Out of range")
        if index == 0:
            self.insert_at_beginning(data)
            
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count = count + 1
        


if __name__ == '__main__':
    l1 = LinkedList()
    l1.insert_at_beginning(5)
    l1.insert_at_beginning(10)
    l1.insert_at_beginning(30)
    l1.insert_at_end(100)
    
    l1.display()

    
    l2 = LinkedList()
    l2.insert_values([45, 78, 89, 90])
    l2.display( )
    l1.get_length()
    l2.remove_element(2)
    l2.display()
    l2.insert_at(2, 34)
    l2.display()
    