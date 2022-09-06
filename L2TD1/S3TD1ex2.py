
#Correction S3 TD1 Ex2

# Ecrire une fonction "positifs" qui prend comme paramètre une liste de nombres
# et renvoie True si tous les éléments de la liste sont positifs et False sinon.


# Ici on écrit une fonction, qui renvoie un booléen
# Il s'agit d'un type de données qui n'a que deux valeurs "True" et "False". 


# Pour aborder une telle question, il faut d'abord remarquer qu'on ne peut 
# répondre à la question qu'en parcourant toute la liste, on a donc besoin 
# d'une boucle (for).

# Ensuite, vous pouvez être tenté d'écrire la fonction ainsi,
# ATTENTION CELA NE FONCTIONNE PAS :

def positifsQUIESTFAUX(l) :
    for x in l :    
        if x>=0 :
            return True 
        else :
            return False

# le problème ci-dessus est que la fonction va s'arrêter dès le premier élément.
# si celui-ci est positif, elle retourne True, et False sinon. Cela ne répond 
# pas à la question.


# Une manière de résoudre le problème, si vous n'avez pas l'intuition de la 
# solution (donnée plus bas) est de se dire qu'il faut mettre un accumulateur, un 
# compteur, comme dans la question 1.
# On peut par exemple compter le nombre d'éléments négatifs. Et c'est seulement 
# après avoir parcouru toute la liste qu'on dira : si il y plus de 0 éléments
# négatifs, alors il faut retourner False, et True sinon. Cela donne :

def positifsPREMIEREVERSION(l) :
    acc = 0
    for x in l :    
        if x<0 :
            acc=acc+1
    if acc>0 :
        return False
    else : 
        return True

# Cela fonctionne, et répond à la question.
# Sinon la solution la plus classique est la suivante:


# On définit une fonction "positifs" qui prend un paramètre "l"
def positifs(l) :
    # x parcourt chaque élément de l
    for x in l :    
        # si x est négatif
        if x<0 :
            # on retourne False
            return False
    # si on a tout parcouru (sans retourner False), on retourne True
    return True

# Dans la fonction précédente l'algorithme repose sur l'idée qu'il faut tester
    # chaque élément de la liste. 
    # Dès qu'un élément est négatif, on peut retourner False, pas besoin 
    # d'aller plus loin.
    # Si aucun n'est négatif, on arrive au bout de la liste et 
    # la propriété est vérifiée : on peut retourenr True.


# Test
l = [12,3,54,23,-23]
h = [12,3,54,23,23]
print(positifs(l))
print(positifs(h))


# le fait de retourner un booléen permet d'utiliser la fonction dans un test :
if positifs(l) :
    print("Tous les entiers sont positifs.")
else :
    print("Au moins un entier est négatif.")


# ENCORE UNE AUTRE IDEE (proche de celle avec l'accumulateur)
# Une autre solution avec un drapeau : 
    # on utilise une varaible comme drapeau initialisé à True.
    # si on rencontre un négatif, on met le drapeau à False
    # Dans tous les cas on retourne la valeur du drapeau après avoir testé
    # chaque élément.

def positifs2(l):
    drapeau = True
    for x in l :    
        if x<0 :
            drapeau = False
    return drapeau


print(positifs2(l))
print(positifs2(h))
    
