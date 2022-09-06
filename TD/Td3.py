

def maxmin(l):
    M=l[0]
    m=l[0]
    for i in l:
        if i>M :
            M=i
        if i<m :
            m=i
    t=(M,m)

    return t,type(t)
    

def tripletoclassic(t):
    n,m,d=t
    M=[[0]*m for i in range(n)]
    for a,b in d.keys():
        M[a][b]=d[(a,b)]
    return M

def triple(mat):
     #les diention de la matrice
    j=mat[0]
    m=len(mat[0])
    n=len(mat)
    #le dictionnaire
    d={}
    for i in n:
        for c in range(m):
            if  mat[i][c]!= 0 :
                d[(i,c)]=mat[i][c]
    t=(n,m,d)
    return t

def somme(t1,t2):
    d={}
    n1,m1,d1=t1
    n2,m2,d2=t2
    if n1==n2 and m1==m2:
        somme=0
        for i in  d1:
            if i not in d2:
                d[i]=d1[i]
        for i in d2 and d1[i]+d2[i]!=0:
            if i in d1:
                d[i]=d1[i]+d2[i]
            else:
                d[i]=d1[i]
     return(t1[0],t1[1],d)

def sunclassic(M1,M2):
    t1,t2=tripletoclassic(t1),tripletoclassic(t2)


