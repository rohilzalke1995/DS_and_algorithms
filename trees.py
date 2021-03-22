class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
        
    def add_child(self, child):
        child.parent = self
        self.children.append(child)
        
    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level = level + 1
            p = p.parent
        return level
        
    def buildTree(self):
        spaces = ' ' * self.get_level() * 3
        print(spaces + self.data)
        if len(self.children)>0:
            for child in self.children:
                child.buildTree()
       
                          
def product_tree():
    root = TreeNode("Electronic")
    
    Laptop = TreeNode("laptop")
    Laptop.add_child(TreeNode("Lenevo"))
    Laptop.add_child(TreeNode("Mac"))
    Laptop.add_child(TreeNode("Dell"))
    
    Mobile = TreeNode("Mobile")
    Mobile.add_child(TreeNode("MI"))
    Mobile.add_child(TreeNode("Apple"))
    Mobile.add_child(TreeNode("Nokia"))
    
    TV = TreeNode("TV")
    TV.add_child(TreeNode("Samsung"))
    TV.add_child(TreeNode("Olida"))
    
    root.add_child(Laptop)
    root.add_child(Mobile)
    root.add_child(TV)
    
    return root
    
if __name__ == '__main__':
    root = product_tree()
    root.buildTree()
    