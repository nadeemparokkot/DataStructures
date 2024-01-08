class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def addNode(self,key):
        newNode=Node(key)
        if self.head is None:
            self.head=newNode
        else:
            self.tail.next=newNode
            newNode.prev=self.tail

        self.tail=newNode

    def display(self):
        if self.head is None:
            print("Empthy")
            return
        temp=self.head
        while(temp!=None):
            print(temp.prev)
            print(temp.data)
            print(temp.next)
            temp=temp.next

    def displayReverse(self):
        temp=self.tail
        while(temp!=None):
            print(temp.data)
            temp=temp.prev
list=DoublyLinkedList()
list.addNode(10)
list.addNode(20)
list.addNode(50)
list.display()
print()
print("display Reverse")
list.displayReverse()