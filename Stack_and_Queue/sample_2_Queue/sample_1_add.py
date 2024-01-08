class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Queue:
    def __init__(self):
        self.front=None
        self.rear=None
    def enqueue(self,key):
        newNode=Node(key)
        if self.rear is None:
            self.front=newNode
        else:
            self.rear.next=newNode
        self.rear=newNode
    def dequeue(self):
        if self.front is None:
            print("empty")
        self.front=self.front.next
        if self.front is None:
            self.rear=None

    def display(self):
        if self.rear is None:
            print("empty")
            return
        temp=self.front
        while temp is not None:
            print(temp.data)
            temp=temp.next

list=Queue()
list.enqueue(10)
list.enqueue(20)
list.enqueue(40)
list.enqueue(90)
# list.dequeue()
list.display()