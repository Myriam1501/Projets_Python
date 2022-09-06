
# exercice 3

# On pourrait utiliser la même idée que pour les fusiosn de dictionnaires 
    # = parcours des listes et constitution des ensembles au fur et à mesure.
    # cf Exercice 6.

# Ici on utilise set et update :

# Surtout attention aux fonctions qu'on utilise : add est là pour ajouter un 
# élément, update une liste d'éléments.


def ensemble2listes(l1,l2) :
    # création d'un ensemble contenant les éléments de l1
    e = set(l1)
    # rajout des éléments de l2
    e.update(l2)
    # on retourne l'ensemble créé.
    return e


print(ensemble2listes([1,2,3],[1,5]))


# Ici, il est plus simple d'utiliser les fonctionnalités avancées liées 
    # aux structures de données.

# Pour d'autres possibilités, voir l'exercie 6
