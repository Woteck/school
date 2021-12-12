from noeud import Noeud

#     KEY          LEFT_VALUE         RIGHT_VALUE
#      =               =                   =
# ('valueRoot', ('valueLeft', ...), ('valueRight', ...))

# TREE DEFINITION

# LAYER 1
my_tree = Noeud('A')
my_tree.setLeft('B')
my_tree.setRight('F')

# LAYER 2
B = my_tree.getLeft()
B.setLeft('C')
B.setRight('D')

F = my_tree.getRight()
F.setLeft('G')
F.setRight('H')

# LAYER 3
C = B.getLeft()
C.setRight('E')

# LAYER 4
G = F.getLeft()
G.setLeft('I')

H = F.getRight()
H.setRight('J')

# TESTS
print(my_tree.length())
print(my_tree.height())

print('Parcours infixe   : ', ' -> '.join(my_tree.parcours_infixe()))
print('Parcours postfixe : ', ' -> '.join(my_tree.parcours_postfixe()))
print('Parcours prefixe  : ', ' -> '.join(my_tree.parcours_prefixe()))
print('Parcours largeur  : ', ' -> '.join(my_tree.parcours_largeur()))

G.insertRight('Z')
G.insertLeft('Y')
print(my_tree.show())

