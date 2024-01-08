class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SinglyLl:
    def __init__(self):
        self.head=None
        self.tail=None
    def addNode(self,key):
        newNode=Node(key)
        if self.head is None:
            self.head=newNode
        else:
            self.tail.next=newNode
        self.tail=newNode
    def display(self):
        if self.head is None:
            print("Empty....")
        temp = self.head
        while(temp is not None):
            print(temp.data)
            temp=temp.next

    def searchNode(self, key):
        pos = 1
        temp = self.head
        # Loop until node with key is found or end of list is reached
        while temp is not None and temp.data != key:
            pos += 1
            temp = temp.next

        # Check if key was found
        if temp is not None:
            return pos
        else:
            return -1
list=SinglyLl()
list.addNode(10)
list.addNode(20)
list.addNode(40)
list.addNode(70)
list.display()
# Search for node with value 40
position = list.searchNode(40)

# Check search result
if position == -1:
    print("Key not found")
else:
    print(f"Key found at position {position}")