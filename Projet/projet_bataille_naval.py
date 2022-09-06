N=10
COLONNES=[str(i) for i in range(N)]
LIGNES = [' '] + list(map(chr, range(97, 107)))
DICT_LIGNES_INT = {LIGNES[i]:i-1 for i in range(len(LIGNES))}
VIDE = '.'
EAU='o'
TOUCHE='x'
BATEAU='#'
DETRUIT='@'
NOMS=['Transporteur','Cuirassé','Croiseur','Sous-marin','Destructeur']
TAILLES=[5,4,3,3,2]

from random import choice
import random
import re

#1

def create_grid():
    L=[]
    for ligne in range(N):
        for colonne in range(N):
            Z=[VIDE]*N
        L.append(Z)
    return L

#2

def plot_grid(m):
    chaine="  "
    chaine+=" ".join(COLONNES)+"\n"
    for z in range(len(m)):
        chaine+=" ".join(LIGNES[z+1])+" "+" ".join(m[z])+"\n"

    return chaine


#3

def tir(pos,m,flotte):
    det=1
    b=()
    for i in range(len(m)):
        for j in range(len(m)):
            if pos==(i,j):
                if m[i][j]==DETRUIT or m[i][j]==EAU or m[i][j]==TOUCHE:
                    return False
                elif presence_bateau(pos,flotte)==True:
                    m[i][j]=TOUCHE
                    
                    print("Touché !")
                 
                    num = id_bateau_at_pos((i,j),flotte)
                    print(NOMS[num])
                    v = flotte[num]
                    v['cases touchées']+=1
                    for h in v['position']:
                        posx=h[0]
                        posy=h[1]
                        if m[posx][posy]!=TOUCHE:
                            det=0
                            plot_flotte_grid(m,flotte)
                        
                    if det==1:
                        noms=id_bateau_at_pos(pos,flotte)
                        print(flotte[noms]['nom'])
                        flotte.pop(noms)
                        plot_flotte_grid(m,flotte)
                    b=m[i][j]
                elif m[i][j]==VIDE:
                    print("MANQUER")
                    m[i][j]=EAU
                
    print(plot_grid(m))



                
    return True




#4

def random_position():
    x=random.randrange(0,N)
    y=random.randrange(0,N)
    return (x,y)


#5
'''
flotte=[]
Z=0
m= create_grid()
while Z!=3:
    plot_grid(m)
    pos=random_position()
    a=tir(pos,m,flotte)
    print(plot_grid(a))
    Z=Z+1

'''
    

#6 7
def pos_from_string(S):
    r=(r"^[a-j]\s[0-9]$")
    while re.search(r,S)==None:
        print("\n!!!!!ERREUR SUR LE FORMAT. LES POSITIONS DOIVENT ETRE DONNER DE MANIERE SUIVANTE : une lettre minuscule suivie d'un espace et d'un chiffre compris entre 0 et 9 \n")
        return False
    position=()
    colonne=int(S[2])
    for i in range(len(LIGNES)):
        if LIGNES[i]==S[0]:
            position=(i-1,colonne)
    x=position[0]
    y=position[1]
    return position

def qst8(m,position1):
    x=position1[0]
    y=position1[1]
    while m[x][y]!=VIDE:
        print(" \n !!!!!!LA POSITION DONNER A DEJA ETAIT ATTAQUER VEUILLER SAISIR UNE NOUVELLE POSITION : ")
        return False
        x=position1[0]
        y=position1[1]
        for i in range(len(LIGNES)):
            if LIGNES[i]==S[0]:
                position1=(i-1,colonne)
        x=position1[0]
        y=position1[1]
    return position1


#  LA FLOTTE

#1

def nouveau_bateau(flotte,nom,taille,pos,orientation):
#flotte=['nom :' nom, 'taille :' taille, 'cases touchées :' 0, 'position :' pos]
    d={}
    d['nom']=nom
    d['taille']=taille
    d['cases touchées']=0
    d['position']=set()
    x=pos[0]
    y=pos[1]        
    for i in range(taille):
        if orientation=='h':
            if y+i>9:
                print(" \n !!!!Taille du bateau trop grande veuillez modifiez la position \n")
                return False
            if presence_bateau((x,y+i),flotte)==True:
                print(" \n !!!!!Bateau se trouve a cette position veuillez modifiez la position \n")
                return False
        elif orientation=='v':
            if x+i>9:
                print(" \n !!!!!Taille du bateau trop grande veuillez modifiez la position \n")
                return False
            if presence_bateau((x+i,y),flotte)==True:
                print(" \n !!!!!Bateau se trouve a cette position veuillez modifiez la position \n")
                return False
        for cle,val in d.items():
            if orientation=='h':
                d['position'].add((x,y+i))
                
                
            if orientation=='v':
                
                d['position'].add((x+i,y))

    flotte.append(d)
    return True









def presence_bateau(pos,flotte):
    for i in flotte:     
        for elt in i['position']:
            if pos==elt :
                return True
    return False
                
    

                

  



def plot_flotte_grid(m,flotte):
    for i in range(len(m)):
        for j in range(len(m)):
            if presence_bateau((i,j),flotte)==False:
                if m[i][j]==TOUCHE:
                    m[i][j]=DETRUIT
            
            
                
    return m

#affiche bateau
def plot_grid_flotte(m,flotte):
    for i in range(len(m)):
        for j in range(len(m)):
            if presence_bateau((i,j),flotte)==True:
                    print("ok")
                    m[i][j]=BATEAU
            
            
            
                
    return m



def input_ajout_bateau(flotte,nom,taille,posi):
    orientation=input("DONNEZ UNE ORIENTATION h OU v : ")
    r=(r"^[a-j]\s[0-9]$")
    orie=(r"^[h|v]$")
    while re.search(orie,orientation)==None:
        print(" \n ERREUR SUR LE FORMAT, L'ORIENTATION DOIT ETRE DONNE PAR h OU v : \n ")
        orientation=input("DONNEZ DE NOUVEAU UNE ORIENTATION h OU v : ")
    if pos_from_string(posi)==False:
        print(" \n erreur sur le format entrer une nouvelle position \n ")
        return False
    posi=pos_from_string(posi)
    if nouveau_bateau(flotte,nom,taille,posi,orientation)==False:
        return False
    

           
def init_joueur(flotte):
    flotte=[]
    for i in range(len(NOMS)):
        print("Veuillez donnez la position du bateaux %str de taille %s : " %(NOMS[i],TAILLES[i]))
        posi=input("DONNEZ UNE POSITION SOUS LA FORME COMME a 9 : ")
        print(posi)
        while input_ajout_bateau(flotte,NOMS[i],TAILLES[i],posi)==False:
            posi=input("DONNEZ DE NOUVEAU UNE POSITION SOUS LA FORME a 9 : ")

    return (create_grid(),flotte)



    

#print(init_joueur())

def init_ia():
    o=['h','v']
    for i in range(len(NOMS)):
        
        posi=random_position()
        orientation=choice(o)
        while nouveau_bateau(flotteia,NOMS[i],TAILLES[i],posi,orientation)==False:
            posi=random_position()
        print("Veuillez donnez la position du bateaux %str de taille %s : " %(NOMS[i],TAILLES[i]))
        print(posi)
        print(orientation)
        

    return plot_grid(mia),flotteia

def init_iaaj():
    o=['h','v']
    for i in range(len(NOMS)):
        
        posi=random_position()
        orientation=choice(o)
        while nouveau_bateau(flotteij,NOMS[i],TAILLES[i],posi,orientation)==False:
            posi=random_position()
        print("Veuillez donnez la position du bateaux %str de taille %s : " %(NOMS[i],TAILLES[i]))
        print(posi)
        print(orientation)
        
    print(plot_grid(plot_flotte_grid(mij,flotteij)))
    return plot_grid(mij),flotteij    



def id_bateau_at_pos(pos,flotte):
    z=0
    if presence_bateau(pos,flotte)==False:
        return None
    else :
        for i in range(len(flotte)):
            for j in (flotte[i])['position']:
                if pos==j:
                    z=i
    return z
            






def tour_ia_random(m,flotte):
    posi=random_position()
    while tir(posi,m,flotte)==False:  
        posi=random_position()






def tour_joueur(nom,m,flotte):
    c=3
    while c==3:
        print("à votre tour ", nom, " !!!!")
        print(plot_grid(m))
        posi=input("DONNEZ UNE POSITION SOUS LA FORME COMME a 9 : ")
        if pos_from_string(posi)!=False:
            pos=pos_from_string(posi)
            if tir(pos,m,flotte)!=False:
                return (tir(pos,m,flotte))
                c=2
            else:
                print("position deja attaquer")
    







def tour_ia_better_random(m,flotte):
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j]==TOUCHE:
                if i<9 and m[i+1][j]==VIDE :
                    tir((m[i+1][j]),m,flotte)
                    return True
                elif i>0 and m[i-1][j]==VIDE:
                    tir((m[i-1][j]),m,flotte)
                    return True
                elif j<9 and m[i][j+1]==VIDE :
                    tir((m[i][j+1]),m,flotte)
                    return True
                elif j>0 and m[i][j-1]==VIDE:
                    tir((m[i][j-1]),m,flotte)
                    return True
        
    tour_ia_random(m,flotte)


                    

          

def test_fin_partie(nom,m,flotte,nb_tour):
    if flotte==[]:
        print(nom, "a perdu la bataile au bout de ", nb_tour , "tour")
        return True




def hide():
    i=0
    while i<25:
        print("\n")
        
        i=i+1
    return ""



m1=create_grid()
flotte1=[]
mia=create_grid()
flotteia=[]
flotte=[]
def joueur_vs_ia():
    nom=input("Entrez le nom du joueur : ")
    init_ia()
    print("Fin initialisation du ia")
    print(hide())
    (m1,flotte1)=init_joueur(flotte)
    tour=0
    while tour!=-1 :
        print("Tour Du IA")
        tour_ia_random(m1,flotte1)
        print(hide())
        print("A votre tour!!!!")
        tour_joueur("ordi",mia,flotteia)
        tour+=1
        if test_fin_partie(nom,mia,flotteia,tour)==True or test_fin_partie("ordi",m1,flotte1,tour)==True:
            tour=-1






def deux_joueurs():
    nom1=input("Entrez le nom du 1er joueur : ")
    nom2=input("Entrez le nom du 2eme joueur : ")
    flotte=[]
    print(plot_grid(create_grid()))
    (m1,flotte1)=init_joueur()
    flotte=[]
    print(hide())
    (m2,flotte2)=init_joueur()
    tour=0
    while tour!=-1 :
        print(hide())
        tour_joueur(nom1,m2,flotte2)
        a=input("appuyer sur entrer pour donner le tour au joueur suivant")
        print(hide())
        tour_joueur(nom2,m1,flotte1)
        tour+=1
        if test_fin_partie(nom1,m1,flotte1,tour)==True or test_fin_partie(nom2,m2,flotte2,tour)==True:
            
            tour=-1
        a=input("appuyer sur entrer pour donner le tour au joueur suivant")
nb_de_joueur=input("Entrez le nombre de joueur: ")

while nb_de_joueur!='1' and nb_de_joueur!='2':
    nb_de_joueur=input("LE NOMBRE DE JOUEUR SAISIE EST INCORRECTE VEUILLEZ SAISIR 1 ou 2 : ")
if nb_de_joueur=='2':
    print(deux_joueurs())
elif nb_de_joueur=='1':
    print(joueur_vs_ia())
