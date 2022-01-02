from math import *

def moyenne_liste(tab):
    n = len(tab)
    res = 0
    for i in tab:
        res = res + i
    return res/n

def tri_ins(t): 
    for k in range(len(t)): 
        temp=t[k] 
        j=k 
        while j>0 and temp<t[j-1]: 
            t[j]=t[j-1] 
            j-=1 
        t[j]=temp
    return t

def mediane_liste(tab):
    t_tri = tri_ins(tab)
    n = len(t_tri)
    if n%2 == 0:
        return (t_tri[(n-1)/2] + t_tri[(n+1)/2])/2
    else:
        return t_tri[n/2]

def ecart_type_liste(tab):
    u = moyenne_liste(tab)
    res = 0
    for i in range(len(tab)):
        res += (tab[i] - u)**2
    return sqrt(res/(len(tab)))


