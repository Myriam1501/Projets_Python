#exo1

def fusion2(d1,d2):
    c={key:value for d in (d1,d2) for key,value in d.items()}
    return c
def ensemble2listes(l1,l2):
    e=set(l1)
    e.update(l2)
    return e
def occ(l1):
    h=dict()
    for x in l:
        for x in h:
            if l1[x]==l1[y]:
                h[x]+=1
            else:
                h[x]=1
    return h

#avec le même nombre de valeur
def pareil2(l1,l2):
    if occ(l1)==occ(l2):
        return True
    else: return False

# seulement les mêmes element
def pareil(l1,l2):
    o=set(l1)
    d=set(l2)
    if o==d:
        return True
    else: return False


def ensemble2listes(l1,l2):
    e=set()
    for x in l1:
        e.set(x)
    for x in l2:
        e.set(x)
    return e
    
