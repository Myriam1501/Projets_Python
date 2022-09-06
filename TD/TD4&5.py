
#sans le Max
def l(s):
    l=[]
    d={}
    M=d[0]
    for x in s:
        if x not in d:
            d[x]=1
        else:
            d[x]+=1
    return d
    for x,y in d.items():
        return l


#EXO1

def parametre2(l1,l2):
    for x in l1:
        for y in l2:
            if not (x in l2 and  y in l1):
                return False
            

        
def parametre(l1,l2):
    if set(l1)==set(l2) and set(l2)==set(l1):
        return True
    else:
        return False



#EXO2
#avec le max
def f(s):
    l=[]
    d={}
    for x in s:
        if x not in d:
            d[x]=1
        else:
            d[x]+=1
    for x,y in d.items():
        if y==max(d.values()):
            l.append(x)
    return l 




