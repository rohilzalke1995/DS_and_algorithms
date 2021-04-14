class Hashtable:
    def __init__(self):
        self.MAX = 100
        self.arr = [[] for i in range(self.MAX)]
        
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
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                #self.arr[h][idx] = (key, value)
                found = True
                    
                break
        if found == True:
            self.arr[h].append((key, value))
        if not found:
            self.arr[h].append((key, value))
        print(self.arr)
    def __getitem__(self, key):
    #This is just like def get, we can get the value of hash just like a dict
    # self.arr['march 6']  The ans we will get is 130
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                print(element[1])
        
    def __delitem__(self, key):
    #Works the same way as def remove_item
    #Only need to do del self.arr[]
        h = self.get_hash(key)
        self.arr[h] = None
        
t = Hashtable()
t['march 10'] = 120
t['march 10'] = 200
t['march 6'] = 120
t['march 15'] = 1
t['march 15'] = 2
t['march 15']