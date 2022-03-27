G = {}
G['a'] = ['b', 'c']
G['b'] = ['a', 'd', 'e']
G['c'] = ['a', 'd']
G['d'] = ['b', 'c', 'e']
G['e'] = ['b', 'd', 'f', 'g']
G['f'] = ['e', 'g']
G['g'] = ['e', 'f', 'h']
G['h'] = ['g']

def get_sommet_nb(graphe):
    return len(graphe)

def get_arete_nb(graphe):
    c = 0
    for sommets_adjacents in graphe.values():
        c += len(sommets_adjacents)
    return c//2

def get_sommet_degre(graphe, sommet):
    return len(graphe[sommet])

def get_sommet_degre_highest(graphe):
    ''' 
    first function
    return a tuple : (sommet, degre)
    '''
    return max([(sommet, get_sommet_degre(graphe, sommet)) for sommet in graphe.keys()], key=lambda tuple : tuple[1])

def get_sommet_degre_highest_2(graphe):
    ''' 
    same function
    return a tuple : (sommet, degre)
    '''
    liste_sommets = [(sommet, get_sommet_degre(graphe, sommet)) for sommet in graphe.keys()]
    return max(liste_sommets, key=lambda tuple : tuple[1])

def get_sommet_degre_highest_3(graphe):
    ''' 
    also the same function
    return a tuple : (sommet, degre)
    '''
    highest_sommet = ''
    highest_dgr    = 0
    for sommet in graphe:
        degre = get_sommet_degre(graphe, sommet)
        if degre > highest_dgr:
            highest_dgr = degre
            highest_sommet = sommet
    return (highest_sommet, highest_dgr)

def get_sommet_neighbors(graphe, sommet):
    return graphe[sommet]
