from node import Node

def tree_test(my_tree):
    print(my_tree)
    print(my_tree.show())
    print(f'Length : {my_tree.length()}')
    print(f'Height : {my_tree.height()}')

    print('In-order traversal    : ', ' -> '.join(L_int_to_str(inorder_traversal(my_tree))))
    print('Post-order traversal  : ', ' -> '.join(L_int_to_str(preorder_traversal(my_tree))))
    print('Pre-order traversal   : ', ' -> '.join(L_int_to_str(postorder_traversal(my_tree))))
    print('Parcours largeur      : ', ' -> '.join(L_int_to_str(breadth_first_search(my_tree))))

    print(dichotomy_search(my_tree, 5))

def L_int_to_str(list_):
    return [str(i) for i in list_]

# https://en.wikipedia.org/wiki/Tree_traversal#/media/File:Sorted_binary_tree_ALL_RGB.svg
def inorder_traversal(tree : Node):
    """ ... left -> root -> right ... (LNR)"""
    L = []
    if tree:
        L = inorder_traversal(tree.getLeft())
        L.append(tree.getKey())
        L += inorder_traversal(tree.getRight())
    return L

def preorder_traversal(tree : Node):
    """ ... root -> left -> right ... (NLR)"""
    L = []
    if tree:
        L.append(tree.getKey())
        L += preorder_traversal(tree.getLeft())
        L += preorder_traversal(tree.getRight())
    return L

def postorder_traversal(tree : Node):
    """ ... left -> right -> root ... (LRN)"""
    L = []
    if tree:
        L = postorder_traversal(tree.getLeft())
        L += postorder_traversal(tree.getRight())
        L.append(tree.getKey())
    return L

# https://en.wikipedia.org/wiki/Breadth-first_search
def breadth_first_search(tree : Node):
    """ layer_1 -> layer_2 -> ... -> layer_i """
    L = [tree] # will work as a FILE.
    result = []
    while L:
        child_left = L[0].getLeft()
        if child_left: L.append(child_left)
        child_right = L[0].getRight()
        if child_right: L.append(child_right)
        result.append(L.pop(0).getKey())
    return result

def dichotomy_search(tree : Node, k):
    """ the keys must be integers """
    if tree is None:
        return False
    value = int(tree.getKey())
    if value == k:
        return True
    if value > k:
        return dichotomy_search(tree.getLeft(), k)
    else:
        return dichotomy_search(tree.getRight(), k)