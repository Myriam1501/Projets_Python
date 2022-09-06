#TD2,S2 exo2
#1
n=int(input("entrer un n premiers entiers positifs"))
som=0
if n>=0:
    for i in range(n+1):
        print(i)
        som=som+i
        print(n,som)
    print("la somme des n premiers entiers positifs vaut : ",som)
else :
    n=int(input("entrer un n premiers entiers positifs"))

#2
    
n=int(input("entrer un n premiers entiers positifs n:"))
m=int(input("entrer un n premiers entiers positifs m:"))
som=0
if n>=0:
    for i in range(n,m+1):
        print(i)
        som=som+i
        i+1
        print(n,som)
    print("la somme des m-1 premiers entiers positifs vaut : ",som)
else :
    n=int(input("entrer un n premiers entiers positifs n:"))
    m=int(input("entrer un n premiers entiers positifs m:"))

#Exo3
    #1
n=0
for i in range(1,101):
    u=1-(-2)**i
    n=n+1
    print("pour n = %d, u=%d"%(n,u))

#td 5
#1
i. 
n!
ii.
un nombre pair
iii. renvois le n eme element de la suite u(n)
iv. nombre d'élémente de la liste
v. met les element a l'envers (inverse la liste)
#2
def p(n,i):
        if (i == 0):
                return 1
        else :
                return n*p(n, i-1)


#3
def insere(e, L, i):

        if (i==0) :
                return [e]+L
        else :
                return L([0])+insere(e,L[1:],i-1)

ou>>>L[0,1]

#td8

def paire(*N):
    nb = 0
    for n in N:
        if n%2 == 0:
            nb += 1
    return nb
