#without collition
#Hash function is division method
class Hashtable:
    def __init__(self,size):
        self.size = size
        self.table = [None]*self.size #[None for i in range(self.size)]
        print(self.table)
    def hash_fun(self, key):
        # Simple modulo hashing based on table size
        return key % self.size

    def add(self, key):
        index = self.hash_fun(key)
        self.table[index] = key

    def get(self,key):
        return key%self.size
    def display_pairs(self):
        print("Key-Value Pairs:")
        for index, item in enumerate(self.table):
            print(f"{index}: {item}")


list= Hashtable(10)
list.add(12)
list.add(23)
list.add(58)
list.add(69)
print(list.get(58))
list.display_pairs()
