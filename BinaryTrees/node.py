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
        newNode = Node(key)
        newNode.L = self.childL()
        self.childL = newNode

    def insertRight(self, key):
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
        if self != None:
            if self.getLeft() != None and self.getRight() != None:
                return 1 + self.getLeft().length() + self.getRight().length()
            elif self.getLeft() == None and self.getRight() != None:
                return 1 + self.getRight().length()
            elif self.getLeft() != None and self.getRight() == None:
                return 1 + self.getLeft().length()
            else:
                return 1
    
    def height(self):
        if self != None:
            if self.getLeft() != None and self.getRight() != None:
                return 1 + max(self.getLeft().height(), self.getRight().height())
            elif self.getLeft() == None and self.getRight() != None:
                return 1 + self.getRight().height() 
            elif self.getLeft() != None and self.getRight() == None:
                return 1 + self.getLeft().height() 
            else:
                return 1

    def parcours_infixe(self, L=[]):
        if self != None:
            left = self.getLeft()
            if left:
                left.parcours_infixe()
            right = self.getRight()
            L.append(self.getKey())
            if right:
                right.parcours_infixe()
        return L

    def parcours_postfixe(self, L=[]):
        if self != None:
            left = self.getLeft()
            if left:
                left.parcours_postfixe()
            right = self.getRight()
            if right:
                right.parcours_postfixe()
            L.append(self.getKey())
        return L

    def parcours_prefixe(self, L=[]):
        if self != None:
            L.append(self.getKey())
            left = self.getLeft()
            if left:
                left.parcours_prefixe()
            right = self.getRight()
            if right:
                right.parcours_prefixe()
        return L
    
    def parcours_largeur(self):
        L = [self] # FILE, i don't use deque from collections, idk
        result = []
        while L:
            left = L[0].getLeft()
            if left:
                L.append(left)
            right = L[0].getRight()
            if right:
                L.append(right)
            result.append(L.pop(0).getKey())
        return result

    def dichotomy(self, s):
        node = self

        def d(s, node):
            if node is None:
                return False
                
            root = int(node.getKey())
            if root == s:
                return True
            elif root > s:
                return d(s, node.getLeft())
            elif root < s:
                return d(s, node.getRight())
        
        return d(s, node)