def tri_fusion(L):
      print(f'{len(L)} - {L}')

      if len(L) <= 2:
            return L
      
      tab1 = tri_fusion(L[:len(L)//2])
      tab2 = tri_fusion(L[len(L)//2:])

      if tab1[0] > tab1[1]:
            tab1[1], tab1[0] = tab1[0], tab1[1]
      if tab2[0] > tab2[1]:
            tab2[1], tab2[0] = tab2[0], tab2[1]
      
      return fusion(tab1, tab2)


def fusion(tab1, tab2):
      tab3 = []
      while tab1 and tab2:
            if tab1[0] < tab2[0]:
                  tab3.append(tab1[0])
                  tab1.pop(0)
            else:
                  tab3.append(tab2[0])
                  tab2.pop(0)
      while tab1:
            tab3.append(tab1[0])
            tab1.pop(0)
      while tab2:
            tab3.append(tab2[0])
            tab2.pop(0)
      return tab3

print(tri_fusion([4, 8, 7, 3, 2, 10, 55, 45]))