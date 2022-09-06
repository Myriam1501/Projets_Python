
# =============================================================================
# Exercice 4 – matrice
# On représente souvent une matrice sous forme de liste de listes.
# affecte 1 à la case de coordonnées (0, 2), soit 1ère ligne, 3ème colonne.
# Ecrire une fonction qui vérifie qu’une matrice est diagonale, c’est à dire :
# — elle est carrée (longueur et largeur sont égales)
# — Si i 6 = j alors la valeur dans la case (i, j) est nulle.
# La fonction retournera un booléen.
# =============================================================================


# Exemple de matrice :

A = [[2,3,4],[7,8,9]]


# On demande une fonction qui vérifie, cela sous-entend qu'on attend une 
# fonction qui retourne un booléen (True ou False).


def diagonale(M) :
    # On vérifie d'abord que M est bien carrée, c'est à dire que la 
        # longueur des lignes et des colonnes est égale.
    
    # M doit avoir au moins une ligne, sinon on retourne False tout de suite.
    if len(M)==0 : 
        return False
    # Ensuite si M n'a pas le même nombre d'éléments dans M et dans sa 
        # première ligne, on renvoie False.
    if len(M)!=len(M[1]) :
        return False
    
    # Si on arrive ici, c'est que la matrice est bien carrée.
        # (on aurait pu vérifier que toutes les éléments de M avaient la même 
        # longueur, mais on suppose que le paramètre M fourni à la fonction 
        # est une matrice, c'est donc inutile).
    
    # Il faut maintenant vérifier que toutes les cases M[i][j] avec i!=j 
        # contiennent des valeurs nulles.
    # Pour parcourir toutes les cases il faut deux boucles imbriquées
        # (c'est à dire l'une dans l'autre)
    
    # notons n le nombre de lignes/colonnes
    n = len(M)
    for i in range(n) :
        for j in range(n):
            if i!=j and M[i][j]!= 0 :
                return False
    return True


# Comme à l'exercice 1, dès qu'on trouve une propriété locale qui viole la 
    # propriété globale qu'on veut vérifier on peut retourner False.
# Et on retourne True si on a vérifié toutes les propriétés locales sans 
    # trouver de problème.


# Par ailleurs ici, on énumère non pas les éléments de la liste comme aux
    # exercices précédents (avec les for x in l) mais les indices d'où la 
    # syntaxe for i in range(n). On n'a pas le choix car la propriété qu'on
    # veut vérifier dépend du contenu des cases mais aussi des indices des 
    # cases.


B = [[12,0,0],[0,8,0],[1,0,4]]
C = [[12,0,0],[0,8,0],[0,0,4]]

print(diagonale(A)) # matrice pas carré
print(diagonale(B)) # matrice carrée mais pas diagonale
print(diagonale(C)) # matrice diagonale







