class BinarySearchTree:
    
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
    def add_child(self, data):
        if self.data == data:
            return 
        if data < self.data:
            #insert the data in left subtree
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTree(data)

        if data > self.data:
            #insert the data in right sub tree
            if self.right:
                self.right.add_child(data)
                
            else:
                self.right = BinarySearchTree(data)
                
    def inorder_traverse(self):
        elements = []
        if self.left:
            elements = elements + self.left.inorder_traverse()
            
        elements.append(self.data)
        
        if self.right:
            elements = elements + self.right.inorder_traverse()
            
        return elements
    
    def preorder_traverse(self):
        elements = []
        elements.append(self.data)
        
        if self.left:
            elements = elements + self.left.preorder_traverse()
            
        if self.right:
            elements = elements + self.right.preorder_traverse()
        return elements
    
    
    def postorder_traversal(self):
        elements = []
        if self.left:
            elements = elements + self.left.postorder_traversal()
        if self.right:
            elements = elements + self.right.postorder_traversal()
        elements.append(self.data)
        
        return elements
        
    def search(self, v):
        if self.data == v:
            return True
        if v < self.data:
            #search in left subtree if it exist
            if self.left:
                return self.left.search(v)
            else:
                return False
        if v > self.data:
            if self.right:
                return self.right.search(v)
            
    def find_min(self):
        if self.left:
            return self.left.find_min()
        else:
            return self.data
        
    def find_max(self):
        if self.right:
            return self.right.find_max()
        else:
            return self.data
            
    def calculate_sum(self):
        left_sum = 0
        right_sum = 0
        if self.left: 
            left_sum = left_sum + self.left.calculate_sum()
            
        if self.right:
            right_sum = right_sum + self.right.calculate_sum()
            
        sum = self.data + left_sum + right_sum
        return sum
    
    def delete_node(self, val):
        if val < self.data:
            if self.left:
                self.left.delete_node(val)
            
        if val > self.data:
            if self.right:
                self.right.delete_node(val)
            
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.right
            
            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete_node(min_val)
        return self
            
            
def build_tree(elements):
    root = BinarySearchTree(elements[0])
    for i in range(1, len(elements)):
        root.add_child(elements[i])
    return root



    
ele = [2, 45, 23, 16, 8, 50]
tree = build_tree(ele)
    
print(tree.find_max())
print(tree.find_min())
print(tree.calculate_sum())
tree = tree.delete_node(2)
print(tree.preorder_traverse())