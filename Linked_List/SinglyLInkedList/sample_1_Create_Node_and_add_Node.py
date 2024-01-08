class Node:   #Define a Node class
    def __init__(self,data):
        self.data=data
        self.next=None
#Create another class for to add nodes and link each indivdual nodes and define head and tail
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
#Create a Function display inside of SinglyLL for to print values
    def display(self):
        if self.head is None:
            print("Empty List")
            return
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next
# last create a object and call each funtion
list=SinglyLL()
list.display()
list.addNode(10)
list.addNode(20)
list.addNode(50)
list.addNode(60)
list.display()