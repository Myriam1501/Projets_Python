
#### Question 1 : une fonction qui teste si une liste est un palindrome.
# -> On veut une fonction qui retourne True si la liste est un palindrome et false sinon.


# Quand on a un problème comme ça, comment l'aborde-t-on ?

# - Il n'y a pas de fonction qui fait directement ce qu'on veut. 
# - DONC on cherche à décomposer notre "gros" objectif, en "petits" objectifs qu'on sait résoudre.


### SOLUTION 1

## 1ère idée :
# - on inverse la liste 
# - puis on teste si la liste initiale et la liste inversée sont égales

def palindrome1(l) :
    m = l.copy()
    m.reverse()
    return l==m

### SOLUTION 2

# on peut aussi inverser la liste avec le slicing :
def palindrome2(l) :
    return l==l[::-1]

#notation générale l[a:b:c] extrait la liste entre a et b exclu par pas de c
# si c est négatif, on part de la fin.


# 2ème idée
# - On va comparer les éléments deux à deux :
#    - le premier et le dernier sont-ils égaux ?
#    - le deuxième et l'avant dernier ?
#    - ...
# - Si la réponse à chaque question est vrai, alors la liste est un palindrome. Sinon, non

# Comment mettre en oeuvre cette idée ?
# - comme il y a répétition d'opération, on va utiliser une boucle for.
# - quel type de boucle for ?
# A) for x in l , x parcourt les éléments de l
# B) for x in range(len(l)), x parcourt les positions des éléments de l

# Ici on a besoin de comparer un élément en position x avec un élément en position len(l)-x, donc on a besoin d'itérer sur les positions. # Donc on utilise une boucle de type B).



### SOLUTION 3 et 4 

# on a donc la structure suivante :
# def palindrome3(l) :
#    for x in range(len(l)) :
#        if l[x]==l[-x-1] :
#            qqchose
#        else :
#            qqchose

# La question qui se pose est comment faire pour retourner True si tous les tests sont bons et False si au moins un est mauvais.

# 1) Avec un "drapeau"
def palindrome3(l) :
    drapeau = True
    for x in range(len(l)) :
        if l[x]!=l[-x-1] :
            drapeau = False
# pas de else, parce qu'un drapeau mis à False ne peut pas revenir à True
    return drapeau


# 2) Avec un return False dès qu'on rencontre une différence.
# puis un return True si on arrive à la fin des tests (donc sans avoir rencontré de diférence.
def palindrome4(l) :
    for x in range(len(l)) :
        if l[x]!=l[-x-1] :
            return False
    return True

### SOLUTION 5
# En compréhension avec all

def palindrome5(l) :
    return all([l[x]==l[-x-1] for x in range(len(l))])

# expliquer tests
l1=[1,2,3,4]
l2=[1,2,3,4,3,2,1]
l3=[1,2,3,4,4,3,2,1]
l4=[1,2,3,4,2,1]
l5=[1,2,3,4,3,2,0]
# En testant avec les 5 exemples ci-dessus, on a déja des chances de se rendre compte si notre fonction a le comportement attendu ou non.


print("Question 1")
print(l1)
print(palindrome1(l1))
print(palindrome2(l1))
print(palindrome3(l1))
print(palindrome4(l1))
print(palindrome5(l1))

print(l2)
print(palindrome1(l2))
print(palindrome2(l2))
print(palindrome3(l2))
print(palindrome4(l2))
print(palindrome5(l2))

print(l3)
print(palindrome1(l3))
print(palindrome2(l3))
print(palindrome3(l3))
print(palindrome4(l3))
print(palindrome5(l3))

print(l4)
print(palindrome1(l4))
print(palindrome2(l4))
print(palindrome3(l4))
print(palindrome4(l4))
print(palindrome5(l4))

print(l5)
print(palindrome1(l5))
print(palindrome2(l5))
print(palindrome3(l5))
print(palindrome4(l5))
print(palindrome5(l5))



#### question 2 ensemble des palindromes inclus dans une liste.

# Il s'agit dénumérer toutes les sous-listes incluses dans la liste et de tester à chaque fois si oui ou non c'est un palindrome.


### Solution 1
# on énumère tous les début (i) et fin (j) possible pour une sous-liste.

# rappel l[i:j] est la sous-liste de premier élément i et dernier élément j-1.

def listepal(l) :
    m=[]     #on crée une liste m vide
    for i in range(len(l)) :
        for j in range(i,len(l)) :
            # on teste si l[i:j+1] est un palindr
            if palindrome1(l[i:j+1]) :
                # si oui on l'ajoute à m
                m.append(l[i:j+1])
    # on retourne m
    return m

### Solution 2
# la même idée en compréhension.
def listepal2(l) :
    return [l[i:j+1] for i in range(len(l)) for j in range(i,len(l)) if (l[i:j+1])==(l[i:j+1])[::-1]]

print("Question 2 et 3")
print(listepal([0,1,2,1,3,4,4]))
print(listepal2([0,1,2,1,3,4,4]))



#### Question 4 :

### Solution 1
# On appelle la fonction listepal de la question 2.
# On cherche dans la liste fournie par cette fonction quelle est la plus grande liste. 
# On retourne cette liste.

def plusgrdpal1(l) :
    m = listepal(l)
    a = []
    for x in m :
        if len(a)<len(x) :
            a = x
    return a

#Solution 1 bis. Cf cours pour comprendre key.
def plusgrdpal2(l) :
    return max(listepal(l),key = len)


### Solution 2
# on reprend la fonction de la question 2, en remplaçant append (à m) par "je ne garde que la plus grande liste" (dans a)
# pour une liste l d'éléments
def plusgrdpal3(l) :
    a=[]
    for i in range(len(l)) :
        for j in range(i,len(l)) :
            if palindrome1(l[i:j+1]) and len(l[i:j+1])>len(a) :
                a = l[i:j+1]
    return a


print("Question 4")

print(plusgrdpal1([0,1,2,1,3,4,4,3,1,2,3,5,5,5,3,2]))
print(plusgrdpal2([0,1,2,1,3,4,4,3,1,2,3,5,5,5,3,2]))
print(plusgrdpal3([0,1,2,1,3,4,4,3,1,2,3,5,5,5,3,2]))












