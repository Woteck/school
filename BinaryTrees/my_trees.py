from node import Node

#     KEY          LEFT_VALUE         RIGHT_VALUE
#      =               =                   =
# ('valueRoot', ('valueLeft', ...), ('valueRight', ...))

# ALPHABET TREE DEFINITION
# LAYER 1
alphabet_tree = Node('A') # root
# LAYER 2
alphabet_tree.setLeft('B')
alphabet_tree.setRight('F')
# LAYER 3
B = alphabet_tree.getLeft()
B.setLeft('C')
B.setRight('D')
F = alphabet_tree.getRight()
F.setLeft('G')
F.setRight('H')
# LAYER 4
C = B.getLeft()
C.setRight('E')
# LAYER 5
G = F.getLeft()
G.setLeft('I')
H = F.getRight()
H.setRight('J')

# NUMBER TREE DEFINITION
# LAYER 1
number_tree = Node(15) # root
# LAYER 2
number_tree.setLeft(6)
number_tree.setRight(18)
# LAYER 3
n6 = number_tree.getLeft()
n6.setLeft(3)
n6.setRight(7)
n18 = number_tree.getRight()
n18.setLeft(17)
n18.setRight(20)
# LAYER 4
n3 = n6.getLeft()
n3.setLeft(2)
n3.setRight(4)
n7 = n6.getRight()
n7.setRight(13)
# LAYER 5
n13 = n7.getRight()
n13.setLeft(9)
