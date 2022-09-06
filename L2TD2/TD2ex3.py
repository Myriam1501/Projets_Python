
# exercice 3

# On pourrait utiliser la m�me id�e que pour les fusiosn de dictionnaires 
    # = parcours des listes et constitution des ensembles au fur et � mesure.
    # cf Exercice 6.

# Ici on utilise set et update :

#�Surtout attention aux fonctions qu'on utilise : add est l� pour ajouter un 
#��l�ment, update une liste d'�l�ments.


def ensemble2listes(l1,l2) :
    # cr�ation d'un ensemble contenant les �l�ments de l1
    e = set(l1)
    # rajout des �l�ments de l2
    e.update(l2)
    # on retourne l'ensemble cr��.
    return e


print(ensemble2listes([1,2,3],[1,5]))


# Ici, il est plus simple d'utiliser les fonctionnalit�s avanc�es li�es 
    # aux structures de donn�es.

#�Pour d'autres possibilit�s, voir l'exercie 6
