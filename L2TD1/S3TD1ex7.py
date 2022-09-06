#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from random import randint
from matplotlib import pyplot as plt


## On écrit d'abord une fonction qui recherche le fromage le plus proche.
def plusproche(l,pos) :
    # je construis le tableau dist = qui contient les distances :
    # dist [i] = distance entre l[i] et pos
    dist = []
    for i in range(len(l)) : # range(len(l)) = 0,1,2,3,...len(l)-1
        dist.append(abs(l[i]-pos))
    # je cherche l'indice du minimum dans dist
    m = 0
    for i in range(len(l)) :
        if dist[i]<dist[m] :
            m=i
    # je retourne la valeur de l correspondant à ce minimum.
    return l[m]

# ou python-style (exactement équivalent) :
def plusproche2(l,pos) :
    return min(l,key=lambda x :abs(x-pos))

print(plusproche([1,4,9,12,3],7))
print(plusproche2([1,4,9,12,3],7))


## Puis la fonction qui fait le job
def souris1(l) :
    #situation de départ :
    pos = 0
    chemin = [0]
    dist = 0
    # tant qu'il reste du fromage :
    while (l!=[]) :
        # je cherche le fromage le plus proche
        nextpos = plusproche(l,pos)
        dist += abs(nextpos-pos) # j'ajoute la distance à ce fromage dans dist
        pos = nextpos # je mets à jour ma position
        chemin.append(pos) # je rajoute ma nouvelle position au chemin
        l.remove(pos) #j'enlève le fromage de la liste
    return chemin,dist

# une solution proche
def souris2(l) :
    chemin = [0]
    dist = 0
    while (l!=[]) :
        chemin.append(plusproche(l,chemin[-1]))
        l.remove(chemin[-1]) 
        dist+=abs(chemin[-1]-chemin[-2])
    return chemin,dist

print(souris([-1,3,5,-10]))

# pour tester on tire au hasard un ensemble de 100 positions dont on ne garde 
# que les différentes 
s=set()
for x in range(100) :
    s.add(randint(-1000,1000))
l = list(s)
l.sort()
print(l)
plt.plot(range(len()))
print(souris(l))
