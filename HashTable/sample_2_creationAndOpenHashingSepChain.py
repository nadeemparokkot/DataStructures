#with
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None for i in range(self.size)]

    def hash_function(self, key):
        return hash(key) % self.size

    def add(self, key, value):
        index = self.hash_function(key)
        if self.table[index] is None:
            self.table[index] = Node(key, value)
        else:
            temp=self.table[index]
            while temp.next is not None:
                temp = temp.next
            temp.next = Node(key, value)


    def get(self, key):
        index = self.hash_function(key)
        temp = self.table[index]
        while temp is not None and temp.key != key:
            temp = temp.next
        if temp is None:
            return None
        else:
            return temp.value

    def display(self):
        print("Hash Table:")
        for index, item in enumerate(self.table):
            print(f"{index}:", end=" ")  # Print index

            # If item is None, indicate an empty slot
            if item is None:
                print("None")

            # Otherwise, traverse the linked list and print key-value pairs
            else:
                current = item
                while current is not None:
                    print(f"({current.key}, {current.value})", end=" -> ")
                    current = current.next
                print("None")  # Mark the end of the chain


t = HashTable(10)
t.add(10,"helo")
t.add(14,"hai")
t.add(20,'kooi')
t.add(18,"heyy")
t.add(28,"hoyy")
t.add(38,"hoyy")
t.display()
print(t.get(20))