import mysql.connector as mariadb
import sys
import re

###connexion MariaDB
connexion= mariadb.connect(
        user='myriam',
        host="localhost",
        password='',
        database='test',
        port=3306,
)
cursor=connexion.cursor()
###verifier que l'enrgistrement de la clé  demander à l'utilisateur n'est pas null 
a=input("SELECT Numprof=2 FROM professeur")
if(a==None):
    print("la cle primaire Numprof=1 est vide veiller modifier")
else:
    print("la cle priamire Numprof est vide")


#contraine cle primaire !=None
b=input("SELECT Numétudiant=1 FROM students;")
if(b==None):
    print("la cle primaire numpétudiant=1 est vide")
else:
    print("la cle primaire Numétudiant=1 n'est pas vide")
