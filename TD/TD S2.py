# td 4
def permute(L, i, j):
    L[i], L[j] = L[j], L[i]
    
    
def une_passe(L):
    for i in range(len(L)-1):
        if L[i] > L[i+1]:
            permute(L, i, i+1)
            
def tri_bulle(L):
    for i in range(len(L)-1):
        une_passe(L)

L = [1,3,4,2,8,6,7,1]

tri_bulle(L)
print(L)

#td5

#1
i. pour savoir si e est un majorant de l
ii. renvoie a la somme de la liste 
iii. l prendra la valeur entiere de j et sera une suite incluse dans m (liste de liste)
iv. affiche les élément de m
v. supprimer la structure de la matrice

#2
del td(L):
    for i in range(len(L)):
        for j in range(i+1, len(L)):
            if L(i)==L(j):
                return false
            else :
                return true

#3
del ti(M,max):
    return(til(pl(M)),max)

#4
def diag(M):
    d1 = []
    d2 = []
    for i in range(len(M)):
        d1.append(M[i][i])
        d2.append(M[i][len(M)-1-i])
    return d1,d2


#5
def inv(M):
    N = [[]]*len(M)
    for i in range(len(M)):
        for j in range(len(M)):
            N[j] = N[j]+[M[i][j]]
    return(N)

print(inv(M1))

    
#6

def cm(M):
    if len(M)==len:
        
    for i in range(len(M)):
        for j in range(i+1, len(M)):
            if L(i)!=L(j):

