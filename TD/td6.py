#td6
#exo 1
#p1:Bombe
#p2:l
    #e
#p3: 10 patates coutent 2 euros.
#BONJOUR TOUT LE MONDE
#False


from re import findall  
s = "Bonjour"
s += " tout le monde"
print(s[0]+s[-4:-6:-1]+"b"+ s[-1])
for x in s.split()[2]: #prend le mot placer a la 2eme position
    print(x)
p = "{} patates coutent {} euros."
print(p.format(10,2)) #remplace {} par la valeur entre parenthèse
print(s.upper()) #met tt en majuscule
print(s.isnumeric()) # True si la chaine est composer uniquement de nombre
#s[3]='a'
findall(r"\S*","voila une belle expr rat")
#renvoie tt ce qui n'a pas d'espace ==> ["voila","","une","","balle"]


#exo 2
#autre solution for x in s.split: ""+=m.capitalize()+""
s="l'objectif est de trouver dans un texte  non"
for x in s.split():
    print ("".join(x.capitalize()+" "))

#autre solution
def maj2(s):
    return "".join(m.capitalize()+" " for m in s.psplit())

#exo 3

def double(s):
    l=s.split()
    for i in range(len(l)):
        if l[i].isnumeric():
            l[i]=str(int(l[i])*2)
    return " ".join(l)

#exo4

def chaine(s):
    if len(s)>100:
        l=[""]
        for x in s.split():
            if len(l[-1])+len(x)+1)<=24:
                l[-1]+=x+""
            else:
                l.append(x+"")
        return l
#exo6
def d(s):
    l=[]
    for m in s.split():
        for c in m :
            if c.isnumeric():
                l.append(m)
                break
    return l
#\d ==> [0-9]
#findall(r"\S*\d\S*",s)
    
