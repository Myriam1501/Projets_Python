#EXO2

def positif(l):
    for x in l:
        if x>0:
            return True
        else:
            return False


#EXO3

def f(l):
    for x in l:
        if not -1<=x<=1:
            l.remove(x)
    return l
            
#EXO4

def mat1(M):
    i=M[0]
    j=M[1]
    if len(i)==len(j):
        if len(M)!=len(j):
            return False
    
        else:
            return True

    return "M est nulle"



#ou pour tout les matrice

def mat2(M):
    i=M[0]
    for j in M:
        if len(i)==len(j):
            if len(M)!=len(j):
                return False
    
            else:
                return True

        return "M est nulle"
                #Correction (autre posibilité)
def mat(M):
    for i in range(len(M)):
        if len(M)!=len(M[i]):
                return False
        for j in range(len(M[i])):
            if i!=j and M[i][j]!=0:
                return False
    return True
    
    

#EXO5

def permute(l,i,j):
    temp=l[i]
    l[j]=l[j]
    l[j]=temp
    return l
def tri(l):
    for i in range(len(l)):
        for j in range(len(l)):
            if l[i]<l[j]:
                permute(l,i,j)
    return l

#EXO6 
#question 1 #sans slicing
def palindrome(l):
    j=len(l)
    for i in range(len(l)):
        j-=1
        if l[i]!=l[j]:
            return("cette suite n'est pas un palindrome")
        else :
            return("l est un palindrome")
#avec

def palindrome2(l):
    m=len(l)//2
    if len(l)%2!=0:
        if l[0:m]!=l[len(l):m:-1]:
            return("cette suite n'est pas un palindrome")
        else :
            return("l est un palindrome")
    else:
        if l[0:m-1]!=l[len(l):m:-1]:
            return("cette suite n'est pas un palindrome")
        else :
            return("l est un palindrome")
# question 2

#EXO7
l=[-6,-1,2,5]
s=0
distance=0

        
