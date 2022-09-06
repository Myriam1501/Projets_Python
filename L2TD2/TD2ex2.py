# Fusion de deux dictionnaires

# Avec un tel problème, il faut penser que :
# - on veut un nouveau dictionnaire. (donc on va en créer un)
# - il va falloir ajouter tous les éléments des deux dico dans le nouveau.
#   ce qui suppose a priori de les les parcourir.


# Donc une bonne solution peut être de :
# - créer un nouveau dico d 
# - parcourir (= boucle) les entrées (clé+valeur) du dico 1 et les ajouter à d
# - puis parcourir (= boucle) les entrées (clé+valeur) du dico 2 et les ajouter à d
# - retourner le nouveau dico


def fusion(d1,d2) :
    # création de d vide
    d = {}
    # pour chaque élément de d1 avec k, la clé et v l'élément,
    for k,v in d1.items() :
        #on insert la valeur v à la clé k dans d
        d[k]=v
    # idem, parcourt de d2 
    for k,v in d2.items() :
        # on insert la valeur v à la clé k dans d 
        # (on remplace la valeur si elle existait déja)
        d[k]=v
    # important : on retourne d.
    return d

a = {"aa":42,"ze":13}
b = {2 : 3, 5: 7,"aa":12}

c = fusion(a,b)
print(c)


# Que se passe-t-il si certaines clés sont présentes dans d1 ET d2
# En fait dans la deuxième boucle, le d[k]=v modifie la valeur
# associée à k si il y en avait dajà une.


# Autre solution avec des fonctionnalités plus avancées :
def fusionBis(d1,d2) :
    d = d1.copy()     # crée une copie de d1 et l'affecte à d
    d.update(d2)      # ajoute à d le contenu de d2
    return d

print(fusionBis(a,b))




# Question 2
def fusion3(d1,d2,d3) :
    d = fusion(d1,d2)
    return fusion(d,d3)

# On fait appelle à la fonction fusion définie précédemment.
# Que se passe-t-il si on remplace le return de fusion par un print ?
    # Tester. Pourquoi cela ne fonctionne-t-il pas ?
    
    
print(fusion3(a,b,{3:45,'ze':44}))


#Autre solution plus courte :
def fusion32(d1,d2,d3) :
    return fusion(fusion(d1,d2),d3)

# En prenant le temps, on comprend.
    
    
