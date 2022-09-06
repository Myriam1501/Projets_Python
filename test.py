from re import findall
from re import search
from re import sub
#l[i]=str(int(l[i])*2)==>'int' object has no attribute 'isnumberic'
#for x in s.split()[2]: #prend le mot placer a la 2eme position
#.isnumeric()) # True si la chaine est composer uniquement de nombre
#for ... ==> l.append(m) on met un break a la fin
#notion( join ect


# split
# prend une chaine de caractère et la découpe selon
# un motif passé en paramètre (valeur par défaut " ").
# ex : "aa jj ee".split() retourne ["aa","jj","ee"]

# join
# fait l'inverse = prend une liste de chaines et les 
# recolle avec un motif intermédiaire.
# ex : "abc".join(["aa","ee","jj"]) -> "aaabceeabcjj"
# Souvent on utilise " ".join(...) pour mettre des espaces.

# capitalize
# retourne une chaine où tous les caractères alphabétiques
# sont mis en minuscule, sauf le premier en majuscule


#EXO4
def chaine(s):
    if len(s)>100:
        l=[""]
        for x in s.split():
            if len(l[-1])+len(x)+1<=24:
                l[-1]+=x+""
            else:
                l.append(x+"")
        return l







# FIN DU TD6!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#pas oublier le from re import findall
# notion findall ect.
#==> 'el''ll''le''el''ll''le''el''ll''ll''el'
#e2 = findall(r"[leH]l","Quelle belle journée à El belllel ! ")
#['el', 'el', 'el', 'll', 'el']==> ne prent en compte qu'une fois la valeur





#l* ==> zéro l ou plus
#r"el?"==> 0 ou 1 fois donc on doit voir e avec ou sans l

#r"\S+"== split()
## \s≠ \S <=> Tous les caractères autres que blanc =tt les mots

# \d correspond aux chiffres

#[(com|fr)], signifie "com" ou "fr" (combinaison parenthèses et |)

#le ".", qui doit être protégé par un "\", pour demander un . dans la liste sinon il a un autre sens


# -> ici on utilise les parenthèses ,celles-ci servent à délimiter 
# ce qu'on appelle des groupes.

# ensuite \i (avec i un entier) fait référence au i-ième groupe.






        




















