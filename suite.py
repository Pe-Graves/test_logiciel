from math import *

def geometrique(tab):
    if len(tab) < 2:
        return False
    else:
        q_prec = tab[1] / tab[0]
        for i in range(1,len(tab)-1):
            q = tab[i+1] / tab[i]
            if(q != q_prec):
                return False
        return True

def arithmetique(tab):
    if len(tab) < 2:
        return False
    else:
        r_prec = tab[1] - tab[0]
        for i in range(1,len(tab)-1):
            r = tab[i+1] - tab[i]
            if(r != r_prec):
                return False
        return True

def geometrique_2(n,tab):
    if len(tab) < 2:
        return False
    else:
        q_prec = tab[0] / n
        for i in range(1,len(tab)-1):
            q = tab[i+1] / tab[i]
            if (q != q_prec):
                return False
        return True
            

def arithmetique_2(n,tab):
    if len(tab) < 2:
        return False
    else:
        r_prec = tab[0] - n
        for i in range(1,len(tab)-1):
            r = tab[i+1] - tab[i]
            if(r != r_prec):
                return False
        return True

