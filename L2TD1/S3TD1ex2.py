
#Correction S3 TD1 Ex2

# Ecrire une fonction "positifs" qui prend comme param�tre une liste de nombres
# et renvoie True si tous les �l�ments de la liste sont positifs et False sinon.


# Ici on �crit une fonction, qui renvoie un bool�en
# Il s'agit d'un type de donn�es qui n'a que deux valeurs "True" et "False". 


#�Pour aborder une telle question, il faut d'abord remarquer qu'on ne peut 
#�r�pondre � la question qu'en parcourant toute la liste, on a donc besoin 
#�d'une boucle (for).

#�Ensuite, vous pouvez �tre tent� d'�crire la fonction ainsi,
#�ATTENTION CELA NE FONCTIONNE PAS :

def positifsQUIESTFAUX(l) :
    for x in l :    
        if x>=0 :
            return True 
        else :
            return False

#�le probl�me ci-dessus est que la fonction va s'arr�ter d�s le premier �l�ment.
# si celui-ci est positif, elle retourne True, et False sinon. Cela ne r�pond 
#�pas � la question.


#�Une mani�re de r�soudre le probl�me, si vous n'avez pas l'intuition de la 
#�solution (donn�e plus bas) est de se dire qu'il faut mettre un accumulateur, un 
#�compteur, comme dans la question 1.
#�On peut par exemple compter le nombre d'�l�ments n�gatifs. Et c'est seulement 
# apr�s avoir parcouru toute la liste qu'on dira : si il y plus de 0 �l�ments
#�n�gatifs, alors il faut retourner False, et True sinon. Cela donne :

def positifsPREMIEREVERSION(l) :
    acc = 0
    for x in l :    
        if x<0 :
            acc=acc+1
    if acc>0 :
        return False
    else : 
        return True

#�Cela fonctionne, et r�pond � la question.
# Sinon la solution la plus classique est la suivante:


# On d�finit une fonction "positifs" qui prend un param�tre "l"
def positifs(l) :
    # x parcourt chaque �l�ment de l
    for x in l :    
        # si x est n�gatif
        if x<0 :
            # on retourne False
            return False
    # si on a tout parcouru (sans retourner False), on retourne True
    return True

# Dans la fonction pr�c�dente l'algorithme repose sur l'id�e qu'il faut tester
    # chaque �l�ment de la liste. 
    # D�s qu'un �l�ment est n�gatif, on peut retourner False, pas besoin 
    # d'aller plus loin.
    # Si aucun n'est n�gatif, on arrive au bout de la liste et 
    # la propri�t� est v�rifi�e : on peut retourenr True.


# Test
l = [12,3,54,23,-23]
h = [12,3,54,23,23]
print(positifs(l))
print(positifs(h))


# le fait de retourner un bool�en permet d'utiliser la fonction dans un test :
if positifs(l) :
    print("Tous les entiers sont positifs.")
else :
    print("Au moins un entier est n�gatif.")


# ENCORE UNE AUTRE IDEE (proche de celle avec l'accumulateur)
# Une autre solution avec un drapeau : 
    # on utilise une varaible comme drapeau initialis� � True.
    # si on rencontre un n�gatif, on met le drapeau � False
    # Dans tous les cas on retourne la valeur du drapeau apr�s avoir test�
    # chaque �l�ment.

def positifs2(l):
    drapeau = True
    for x in l :    
        if x<0 :
            drapeau = False
    return drapeau


print(positifs2(l))
print(positifs2(h))
    
