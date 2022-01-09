class Node:
    def __init__(self, key=None):
        self.key    = key
        self.childL = None
        self.childR = None

    def setKey(self, newKey):
        self.key = newKey
    
    def setLeft(self, key):
        self.childL = Node(key)
    
    def setRight(self, key):
        self.childR = Node(key)

    def insertLeft(self, key):
        if self.childL is None:
            self.setLeft(key)
        else:
            newNode = Node(key)
            newNode.L = self.childL()
            self.childL = newNode

    def insertRight(self, key):
        if self.childR is None:
            self.setRight(key)
        else:
            newNode = Node(key)
            newNode.R = self.childR()
            self.childR = newNode

    def getKey(self):
        return self.key

    def getLeft(self):
        return self.childL
    
    def getRight(self):
        return self.childR

    def show(self):
        if self != None:
            if self.getLeft() != None and self.getRight() != None:
                return (
                    self.getKey(), 
                    self.getLeft().show(), 
                    self.getRight().show()
                )
            elif self.getLeft() == None and self.getRight() != None:
                return (
                    self.getKey(), 
                    None, 
                    self.getRight().show()
                )
            elif self.getLeft() != None and self.getRight() == None:
                return (
                    self.getKey(), 
                    self.getLeft().show(), 
                    None
                )
            else:
                return (
                    self.getKey(), 
                    None, 
                    None
                )
    
    def length(self):
        if self:
            if self.getLeft() != None and self.getRight() != None:
                return 1 + self.getLeft().length() + self.getRight().length()
            elif self.getLeft() == None and self.getRight() != None:
                return 1 + self.getRight().length()
            elif self.getLeft() != None and self.getRight() == None:
                return 1 + self.getLeft().length()
            else:
                return 1
    
    def height(self):
        if self:
            if self.getLeft() != None and self.getRight() != None:
                return 1 + max(self.getLeft().height(), self.getRight().height())
            elif self.getLeft() == None and self.getRight() != None:
                return 1 + self.getRight().height() 
            elif self.getLeft() != None and self.getRight() == None:
                return 1 + self.getLeft().height() 
            else:
                return 1