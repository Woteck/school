from node import Node

# TESTS
def tree_test(my_tree):
    print(my_tree)
    print(my_tree.show())
    print(f'Length : {my_tree.length()}')
    print(f'Height : {my_tree.height()}')

    print('Parcours infixe   : ', ' -> '.join(L_int_to_str(my_tree.parcours_infixe())))
    print('Parcours postfixe : ', ' -> '.join(L_int_to_str(my_tree.parcours_postfixe())))
    print('Parcours prefixe  : ', ' -> '.join(L_int_to_str(my_tree.parcours_prefixe())))
    print('Parcours largeur  : ', ' -> '.join(L_int_to_str(my_tree.parcours_largeur())))

def L_int_to_str(list_):
    return [str(i) for i in list_]