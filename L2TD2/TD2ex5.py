
# égalité des éléments de deux listes

# Le bon choix est de passer par des ensembles :
# les ensembles associés aux deux listes sont égales 
# <=> elles ont les mêmes éléments.


def memeset(l1,l2) :
    return set(l1) == set(l2)

print(memeset([1,2,3],[1,2,4]))
print(memeset([1,2,3],[3,1,2]))



# Maintenant si on veut se compliquer la vie,
# on peut aussi tester diretement:

# vraiment à la main, avec des boucles :
def memeset3(l1,l2) :
    #Pour x dans l1
    for x in l1 :
        #Si x n est pas dans l2
        if x not in l2 :
            # retourner faux (sort de la fonction)
            return False
    # Idem dans l'autre sens
    for x in l2 :
        if x not in l1 :
            return False
    # si on arrive là on peut valider.
    return True

print(memeset3([1,2,3],[1,2,4]))
print(memeset3([1,2,3],[3,1,2]))



# On peut aussi utiliser le fait que la valeur booléenne d'une liste 
# vaut false ssi la liste est vide.
def memeset2(l1,l2) :
    return not ([x for x in l1 if x not in l2] or 
                [x for x in l2 if x not in l1])

print(memeset2([1,2,3],[1,2,4]))
print(memeset2([1,2,3],[3,1,2]))
 