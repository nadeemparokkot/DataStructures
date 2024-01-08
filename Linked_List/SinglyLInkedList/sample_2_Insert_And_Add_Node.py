class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SinglyLL:
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
    def insertBegnning(self,key):
        newNode=Node(key)
        newNode.next=self.head.next
        self.head.next=newNode
        self.head=newNode
    def insertAfter(self,nextTo,key):
        newNode=Node(key)
        temp=self.head
        while(temp is not None and temp.data!=nextTo):
            temp=temp.next
        if (temp.next==self.tail):
            self.tail.next=newNode
            self.tail=newNode
            return
        newNode.next = temp.next
        temp.next=newNode

    def insertEnd(self,key):
        newNode=Node(key)
        self.tail.next=newNode
        self.tail=newNode
    def display(self):
        if self.head is None:
            print("List is Empty")
            return
        temp = self.head
        while (temp is not None):
            print(temp.data)
            print(temp.next)
            temp=temp.next
list=SinglyLL()
list.addNode(10)
list.addNode(20)
list.addNode(40)
list.addNode(90)
list.insertBegnning(1000)
list.insertAfter(20,100)
list.insertEnd(500)
list.display()