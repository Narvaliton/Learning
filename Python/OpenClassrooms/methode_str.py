from random import randrange
import os

"""Les méthodes de la classe str"""
nom = "Colin"
prenom = "Maxime"
age = "22"

#Utilisation de la fonction upper qui permet de passer une chaine de caractère en majuscule ( != lower() )
print("Tu t'appeles " + prenom + " " + nom.upper() + " et tu as " + age + " ans.")

#Formater une chaine de caractère
print("Tu t'appeles {1} {0} et tu as {2} ans.".format(nom.upper(), prenom, age))

#Parcours de chaine
chaine = "Hello world !"
print(chaine[0:5])
#Equivaut à:
print(chaine[:5])
print(chaine[6:11])
print(chaine[-1])

#On veut compter le nombre de fois ou la chaine de caractère "x" est présente dans la variable "chaine"
x = "l"
print(chaine.count(x))

#On remplace les occurences de la chaine "x" par la chaine de caractère "y" dans la variable "chaine"
y = "j"
newChaine = chaine.replace(x, y)
newChaine2 = chaine.replace(x,y,1)#On peut indiquer le nombre de fois qu'on remplace la chaine de caractère
print(newChaine)
print(newChaine2)
print(chaine)#La chaine originale n'est pas modifiée

#On cherche la première occurence d'une chaine de caractère dans une autre
occurence = chaine.find("l")
print(occurence)
#On peut limiter la recherche à une partie de la chaine en spécifiant les indices ou l'on veut commencer et/ou finir la recherche
occurence2 = chaine.find("l", 5, -1)
print(occurence2)


#On veut remplacer toutes les occurences dans une chaine de caractère par un caractère aléatoire
lettres = "abcdefghijklmnopqrstuvwxyzêéèàâôî"
chaine2 ="C'est fou le nombre de lettres qui se trouve dans cette chaine de caractère"
newChaine2 = ""
lettre = "4"
while lettre not in lettres or len(lettre) != 1:
    lettre = input("Choisissez une lettre de l'alphabet :\n").lower()

for i in range(0,len(chaine2)):
    if chaine2[i].lower() == lettre:
        newChaine2 += lettres[randrange(len(lettres))]
    else:
        newChaine2 += chaine2[i]

    

print(newChaine2)
os.system("pause")
