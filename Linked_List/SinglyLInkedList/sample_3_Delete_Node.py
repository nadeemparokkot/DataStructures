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
    def deleteNode(self,key):
        temp=self.head
        prev=None
        if (temp.data==key):
            self.head=temp.next
            return
        while(temp is not None and temp.data != key):
            prev=temp
            temp=temp.next
        if temp is None:
            return
        if (temp==self.tail):
            self.tail=prev
            self.tail.next=None
            return
        prev.next=temp.next


    def deleteAfter(self, key):
        temp = self.head
        nextTo=None
        if temp.data==key and nextTo is None:
            self.head.next=temp.next.next
            return

        while temp is not None and temp.data != key:
            nextTo=temp.next.next  #(temp=10 anenki nextTo=40 akum)
            temp = temp.next

        if (nextTo==self.tail):
            temp.next=None
            self.tail=temp
            return
        temp.next=nextTo.next


    def deleteBehind(self,key):
        temp=self.head
        prev=None
        if temp.next is not None and temp.next.data == key:
            self.head=temp.next
            return
        while(temp.next is not None and temp.next.data != key):
            prev=temp
            temp=temp.next
        prev.next=temp.next


    def display(self):
        if self.head is None:
            print("Empty")
        temp=self.head
        while(temp is not None):
            print(temp.data)
            temp=temp.next
list=SinglyLL()
list.addNode(10)
list.addNode(20)
list.addNode(40)
list.addNode(90)
list.deleteNode(40)
list.deleteAfter(20)
# list.deleteBehind(90)
list.display()