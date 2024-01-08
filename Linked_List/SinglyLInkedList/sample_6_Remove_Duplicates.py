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
    def removeDuplicates(self):
        if self.head is None:
            return
        values=set()
        temp=self.head
        prev=None
        while temp is not None:
            if temp.data in values:
                prev.next=temp.next
            else:
                values.add(temp.data)
                prev=temp
            temp=temp.next

    def display(self):
        if (self.head is None):
            print("List is Empty")
            return
        temp = self.head
        while(temp is not None):
            print(temp.data)
            temp=temp.next

list=SinglyLL()
list.addNode(10)
list.addNode(20)
list.addNode(20)
list.addNode(40)
list.addNode(10)
list.addNode(90)
list.removeDuplicates()
list.display()