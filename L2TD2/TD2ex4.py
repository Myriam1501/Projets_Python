from random import randint # pour le stests en bas.


# Nombre d'occurence

# Dans tous les cas, on peut se dire qu'il va falloir parcourir 
# tous les éléments de la liste de départ, et à chaque fois faire
# une opération sur le dictionnaire.

## La solution qu'il faut absolument comprendre est la 4ème. ##


## Solution 1
# Si on connait la fonction count on peut faire :
def nbrocc3(l) :
    # on crée le dictionnaire d vide
    d = {}
    #pour chaque élément x de la liste l
    for x in l :
        # on ajoute au dictionnaire l'entrée avec clé x 
            # et valeur le nombre d'occurence.
        d[x]=l.count(x)
    # on n'oublie pas de retourner le dictionnaire (avec return !)
    return d


##Solution 2
# Une solution très proche, en compréhension de dictionnaire :
def nbrocc4(l) :
    return {i:l.count(i) for i in l}




## Solution 3
#  On va faire les choses "à la main"
# On parcourt une première fois la liste pour ajouter au dico les clés 
# qui correspondent aux éléments de la liste (avec 0 comme valeur).
# Puis on reparcourt la liste en incrémentant pour chaque élément x rencontré
# dans la liste la valeur associée à la clé x dans le dico.

def nbrocc2(l) :
    d={}
    for x in l :
        d[x]=0
    for x in l :
        d[x]+=1
    return d


## Solution 4
# Ici on parcourt la liste l. 
# Et pour chaque élément x rencontré, on met à jour le dico d :
#    - soit il contient déja une entrée avec cet élément x comme clé,
#            alors on incrémente (+1) la valeur associée
#    - soit il ne la contient pas alors on la crée avec comme valeur 1.


def nbrocc(l) :
    # création du dictionnaire vide
    d={}
    # pour chaque élément x de l
    for x in l :
        # si x est une clé de d,
        if x in d :
            # on incrémente la valeur qui lui est associée
            d[x]+=1
        else :
            # sinon on crée l'entrée x avec comme valeur 1
            d[x] = 1
    return d


# En fait on utilise le dictionnarie comme un ensemble de compteurs, associés
# aux éléments de la liste.


a = [1,2,3,4,2,4,3,5,3,1,63,2,4,3,2,54,3,4,5,3,2]
print (nbrocc(a))
print (nbrocc2(a))
print (nbrocc3(a))
print (nbrocc4(a))


# Autre test
l = [randint(-10,10) for _ in range(1000)]
print(nbrocc(l))
print(nbrocc2(l))
print(nbrocc3(l))
print(nbrocc4(l))
