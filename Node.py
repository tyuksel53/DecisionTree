class BinaryTree():

    def __init__(self,rootid):
      self.left = None
      self.right = None
      self.rootid = rootid
      self.Lines = []
      self.f = 0
      self.split = 0

    def getLeftChild(self):
        return self.left
    def getRightChild(self):
        return self.right
    def setNodeLines(self,value):
        self.Lines.append(value)
    def setNodef(self,value):
        self.f = value
    def setNodeSplit(self,value):
        self.split = value
    def getNodeValue(self):
        return self.rootid ," - ",self.f," - ",self.split

    def insertRight(self,newNode):
        if self.right == None:
            self.right = BinaryTree(newNode)
        else:
            tree = BinaryTree(newNode)
            tree.right = self.right
            self.right = tree
        
    def insertLeft(self,newNode):
        if self.left == None:
            self.left = BinaryTree(newNode)
        else:
            tree = BinaryTree(newNode)
            self.left = tree
            tree.left = self.left

def testTree():
    myTree = BinaryTree("Maud")
    myTree.insertLeft("Bob")
    myTree.insertRight("Tony")
    myTree.insertRight("Steven")
    printTree(myTree)