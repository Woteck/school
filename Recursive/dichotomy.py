def dichoRecGood2(l : list, nb : int) -> bool:
    deb=0
    fin=len(l)-1

    def dichoR(l : list, deb : int, fin : int, nb : int ) -> bool:
        if fin < deb: 
            return False

        m=(deb+fin)//2

        if l[m] < nb:
            return dichoR(l, m+1, fin, nb)
        elif l[m] > nb:
            return dichoR(l, deb, m-1, nb)
        else:
            return True 
    
    return dichoR(l,deb,fin,nb)