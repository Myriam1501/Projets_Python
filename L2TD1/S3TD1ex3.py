
# Exercice 3
# Ecrire une fonction qui prend comme paramètre une liste de nombres et
# renvoie la liste de ses éléments compris entre -1 et 1.
# Par exemple si x = [0.2, −0.5, 2, −0.2, −1.3], elle renvoie [0.2, −0.5, −0.2]

# Ici, il va falloir à nouvau parcourir chaque élément de la liste
# donc utiliser une boucle for.
# Pour chaque élément, on teste si il est dans l'intervalle et si oui on 
# rajoute l'élément à une liste créée au préalable

def intervalle(l):
    # on crée une liste vide h
    h = []
    # pour chaque élément x de l
    for x in l :
        # si il appartient à l'intervalle
        if -1<x and x<1 :
            # on ajoute l'élément x à h
            h.append(x)
    # une fois tout cela terminé on retourne la liste h
    return h


# Notez que le return est à l'extérieur de la boucle (cela est indiqué par 
# son indentation. Pourquoi ? Testez en le décalant à l'intérieur du for,
# c'est à dire au niveau du if.
            
x = [0.2, -0.5, 2, -0.2, -1.3]
print(intervalle(x))


# Ai-je le droit d'appeler ma liste x ? cela pose-t-il un problème avec le x
# de la fonction? -> Oui j'ai le droit, non pas de problème.


# Si on veut voir le résultat de la fonction il faut obligatoirement mettre le 
# print autour de l'appel à la fonction intervalle. Pourquoi ?
