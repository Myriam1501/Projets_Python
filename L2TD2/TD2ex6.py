
# exercice 3

# On pourrait utiliser la même logique que pour les fusions de dictionnaires 
    # = parcours des listes et constitution des ensembles au fur et à mesure.


def ensemble2listes2(l1,l2) :
    # création d'un ensemble contenant les éléments de l1
    e = set(l1)
    # parcourt des éléments de l2 et ajout dans e
    for x in l1 :
        e.add(x)
    # parcourt des éléments de l2 et ajout dans e
    for x in l2 :
        e.add(x)
    # on retourne l'ensemble créé.
    return e


print(ensemble2listes2([1,2,3],[1,5]))

