class HashTable:
    def __init__(self,size):
        self.size=size
        self.table=[None]*size
        print(self.table)
    def has_fun(self,key):
        return key%self.size
    def add(self, key):
        index = self.has_fun(key)
        for i in range(self.size):
            new_index = (index + i) % self.size
            if self.table[new_index] is None:
                self.table[new_index] = key
                return
        print("Hash table is full!")
    def display(self):
        print("Key-value pairs")
        for k,v in enumerate(self.table):
            print(f"{k}:{v}")

list=HashTable(10)
list.add(12)
list.add(22)
list.add(38)
list.add(41)
list.add(48)
list.add(58)
list.add(59)
list.add(58)
list.add(58)


list.display()