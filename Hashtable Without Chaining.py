class Hashtable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]
        
    def get_hash(self, key):
        h = 0
        for char in key:
            h = h + ord(char)   
        return h % self.MAX
    
    def add(self, key, value):
        h = self.get_hash(key)
        self.arr[h] = value
        #print(self.arr)
        
    def get(self, key):
        h = self.get_hash(key)
        return self.arr[h]
    
    def remove_item(self, key):
        h = self.get_hash(key)
        self.arr[h] = None
    
    def __setitem__(self, key, value):
    #This is just a like def add but in this we can add a item as we add in dict
    #self.arr['march 6'] = 130
        h = self.get_hash(key)
        self.arr[h] = value
        
    def __getitem__(self, key):
    #This is just like def get, we can get the value of hash just like a dict
    # self.arr['march 6']  The ans we will get is 130
        h = self.get_hash(key)
        print(self.arr[h])
        
    def __delitem__(self, key):
    #Works the same way as def remove_item
    #Only need to do del self.arr[]
        h = self.get_hash(key)
        self.arr[h] = None
        

t = Hashtable()
t.add('march 5', 110)
t['march 7'] = 150
t['march 6'] = 130



t['march 7']
t['march 6']
t['march 5']











