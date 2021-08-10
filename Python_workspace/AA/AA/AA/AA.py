import sys


sys.stdin = open("input.txt")





class BST:

    class Node:
        def __init__(self, data):
            self.data = data
            self.lChild = None
            self.rChild = None

    def __init__(self):
        self.root = None


    def makeNode(self, data):
        n = Node(data)
        print(n.data)
        print(n.data)
        n.data = data

        return n


    def add(self, data):
        if self.root == None:
            self.root = makeNode(data)
            return self.root



root = BST()
root.makeNode(10)

print(root.data)

