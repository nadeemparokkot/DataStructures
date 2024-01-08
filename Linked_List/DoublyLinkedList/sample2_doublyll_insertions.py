class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

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
    def insertBegining(self,key):
        newNode=Node(key)
        newNode.next=self.head
        self.head.prev=newNode
        self.head=newNode

    def insertAfter(self,nextTo,key):
        newNode=Node(key)
        temp=self.head

        while(temp is not None and temp.data != nextTo):
            temp=temp.next

        if temp is None:
            return

        if temp==self.tail:
            self.tail.next=newNode
            newNode.prev=self.tail
            self.tail=newNode
            return

        newNode.next=temp.next
        if temp.next is not None:#ithinte need illa because tail vannal case vere ann
         temp.next.prev=newNode
        temp.next=newNode
        newNode.prev=temp

    def insertBehind(self,prevTo,key):
        newNode=Node(key)
        temp = self.head

        while(temp is not None and temp.data!=prevTo):
            temp=temp.next
        if temp is None:
            return
        if temp==self.head:
            self.head.prev=newNode
            newNode.next=self.head
            self.head=newNode
            return
        newNode.next=temp
        temp.prev.next=newNode
        newNode.prev=temp.prev
        temp.prev=newNode
    def insertEnd(self,key):
        newNode=Node(key)
        self.tail.next=newNode
        newNode.prev=self.tail
        self.tail=newNode
    def display(self):
        if self.head is None:
            class color:
                BOLD = '\033[1m'
                END = '\033[0m'
            print(color.BOLD +"Empty......!!!\n!!! Add some valuess Babe !!!"+color.END)
            return
        temp=self.head
        while(temp!=None):
            print(temp.prev)
            print(temp.data)
            print(temp.next)
            temp=temp.next
list=DoublyLL()
list.addNode(10)
list.addNode(20)
list.addNode(50)
list.display()
list.insertAfter(50,200)
list.insertAfter(20,100)
list.insertBehind(10,5000)
list.insertBehind(20,1000)
list.insertBegining(1500)
list.insertEnd(2500)
print()
list.display()