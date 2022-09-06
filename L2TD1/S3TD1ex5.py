
# =============================================================================
# Exercice 5
# Ecrire :
# 1. une fonction qui permute les éléments en position i et j dans une liste L
# 2. une fonction de tri.
# 3. Pour le tri, on implémentera l’algorithme de tri-bulle : parcourir la 
# liste à trier en permutant les deux valeurs consécutives si elles ne sont 
# pas correctement ordonnées de manière croissante. Répéter cette opération 
# autant de fois qu’il y a d’éléments dans la liste.
# =============================================================================


## Question 1

# En Pyhton on peut permuter les deux valeurs directement en utilisant des 
# couples :
def permute(l,i,j) :
    l[i],l[j] = l[j],l[i]

# DEUX REMARQUES :

# remarque 1 :
# Que se passe-t-il si on essaye de permuter les valeurs en faisant :
    # l[i] = l[j] puis
    # l[j] = l[i] ?
# En fait il faudrait utiliser une valeur tampon :
    # b = l[i] puis 
    # l[i] = l[j] 
    # l[j] = b
# Mais en Python il est plus simple d'utiliser directement :
    #l[i],l[j] = l[j],l[i]
# Dans ce cas, rappelons-nous que lors d'une affectation, Python commence par
    # évaluer la valeur de ce qui est à droite du = (ici le couple des deux 
    # valeurs), et ENSUITE les affecte dans la (ou ici les) variables à
    # gauche. C'est pour cela qu'il n'y a pas besoin de variable tampon ici.

# remarque 2 :
# Tetons notre fonction :
a = [1,2,3,6,3]
print(a)
permute(a,1,4)
print(a)

# Il faut bien voir que les modifications faites à la liste à l'intérieur de 
# la fonction existent aussi à l'extérieur. C'est parce qu'il s'agit d'une
# liste, et d'affectations aux éléments d'une liste

# Si vous testez le code suivant :

# def incr(x) :
#     x=x+1
# b = 3
# print(b)
# incr(b)
# print(b)

# b n'est pas modifié à l'extérieur de la fonction.
# On en reparlera, mais retenze que lorsqu'on passe une fonction à une liste,
# on lui donne la possibilité de la modifier.



## Question 2

def tribulle(l) :
    for i in range(len(l)) :
        for j in range(len(l)-1) :
            if l[i]>l[j] :
                permute(l, i, j)
               
# Sur le principe du tri, vous pouvez regarder :
# https://fr.wikipedia.org/wiki/Tri_%C3%A0_bulles
                
# Notez qu'il n'y a pas de valeur de retour, pas de return dans la fonction.
# Cf remarque 2 de la question 1, la liste passée en paramètre est modifiée.
                
tribulle(a)
print(a)


# On per


