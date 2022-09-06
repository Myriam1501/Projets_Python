#Â Cet exercice est optionnel

g = ({0,1,2,3},{(0,1),(2,1),(0,2),(2,3),(3,2),(3,3)})

h = ({0,1,2,3},{(0,1),(2,1),(0,2),(2,3),(3,2),(3,3),(1,0)})

g2 = ({0,1,2,3},{(0,1),(2,1),(0,2),(2,3),(3,2),(3,5)})
#g2 n'est pas un graphe

print(g)
print(g2)


# question 1
#Â V = g[0] et E = g[1]
#Â On peut vÃ©rifier pas Ã  pas, ou directement avec all.
#Â "all" construit un ensemble de boolÃ©ens, pour chaque 
#Â sommet qui apparait dans E, le boolÃ©en correspondant
# vaut True ssi ce sommet apparaÃ®t bient dans V.
def verif(g) :
    return all({x in g[0] for a in g[1] for x in a} )

print(verif(g))
print(verif(g2))

# question 2

def cycle(s,g) :
    return all([(s[i],s[i+1]) in g[1] for i in range(len(s)-1)]) and s[0]==s[-1]

print("cycles")
print(cycle([3],g))
print(cycle([2,3,2],g))
print(cycle([0,1,2],g))
print(cycle([3,2,1,3],g))
print(cycle([0,1,2,0],g))


# question 3
def dico(g) :
    return {s:{t for (u,t) in g[1] if u==s} for s in g[0]}

print(dico(g))


# question 4
def dico2(d) :
    return {s:{t for u in d[s] for t in d[u]} for s in d}

print(dico2(dico(g)))


# question 5
def accessibles(g) :
    d = dico(g)
    d2 = {}
    d3 = d
    while d2!=d3:
        d2 = dico2(d3)
        d3= {s:{t for t in d3[s]|d2[s]} for s in d}
    return(d3)

print("accessibles")
print(accessibles(g))
print(accessibles(h))






