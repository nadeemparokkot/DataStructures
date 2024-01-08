class Node:
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.next=None

class DoublyLL:
    def __init__(self):
        self.head=None
        self.tail=None

    def addNode(self,key):
        newNode=Node(key)
        if self.head is None:
            self.head=newNode
        else:
            self.tail.next=newNode
            newNode.prev=self.tail
        self.tail=newNode

    def deleteNode(self,key):
        temp=self.head
        prev=None
        if temp is not None:
            if temp.data == key:  #case of head
                self.head=temp.next
                self.head.prev=None
                return
            while(temp.data != key):
                prev = temp
                temp=temp.next
            if temp==self.tail:
                self.tail=prev
                self.tail.next=None
                return
            prev.next=temp.next
    def deleteBehind(self,key):
        temp=self.head

        if temp is not None and temp.data==key:
            print("There have no values of behind the head")
            return
        while temp.next is not None and temp.next.data!=key:
            temp=temp.next
        if temp==self.head:
            self.head=temp.next
            self.head.prev=None
            return
        temp.prev.next=temp.next
        temp.next.prev=temp.prev

    def deleteAfter(self,key):
       temp=self.head
       if temp is not None and temp.data == key:
           temp.next=temp.next.next
           temp.next.prev=temp
           return
       while temp is not None and temp.data!=key:
            temp=temp.next
       if temp is None:
           return
       if temp.next==self.tail:
           self.tail=temp
           self.tail.next=None
           return

       if temp==self.tail:
           print("have no values after head")
           return
       temp.next=temp.next.next
       temp.next.prev=temp

    def display(self):
        if self.head is None:
            print("Empty....!!!!")
        temp=self.head
        while(temp is not None):
            print(temp.prev)
            print(temp.data)
            print(temp.next)
            temp=temp.next
list=DoublyLL()
list.addNode(10)
list.addNode(20)
list.addNode(50)
list.addNode(90)
list.deleteAfter(50)
list.display()
