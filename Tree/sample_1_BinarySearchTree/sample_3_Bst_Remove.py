class Node:
    def __init__(self,data):
        self.left=None
        self.data=data
        self.right=None
class BinarySearch:
    def __init__(self):
        self.root=None

    def insert(self,key):
        newNode=Node(key)
        if self.root is None:
            self.root=newNode
            return
        temp=self.root
        while temp is not None:
            if key<temp.data:
                if temp.left is None:
                    temp.left=newNode
                    return
                else:
                    temp=temp.left
            else:
                if temp.right is None:
                    temp.right=newNode
                    return
                else:
                    temp=temp.right
    def delete(self, key):
        self.root = self.helperDelete(self.root, key)
    def helperDelete(self, root, key):
        if root is None:
            return root

        if key < root.data:
            root.left = self.helperDelete(root.left, key)
        elif key > root.data:
            root.right = self.helperDelete(root.right, key)
        else:
            # Node with only one child or no child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            # Node with two children
            root.data = self.getMinvalue(root.right)
            root.right = self.helperDelete(root.right, root.data)

        return root

    def getMinvalue(self, root):
        while root.left is not None:
            root = root.left
        return root.data
    def inOrder(self):
        self.inOrderHelper(self.root)
    def inOrderHelper(self,node):
        if node is not None:
            self.inOrderHelper(node.left)
            print(node.data)
            self.inOrderHelper(node.right)
list=BinarySearch()
list.insert(10)
list.insert(8)
list.insert(6)
list.insert(9)
list.insert(12)
list.insert(11)
list.insert(15)
list.inOrder()
print("After delete")
list.delete(10)
list.inOrder()