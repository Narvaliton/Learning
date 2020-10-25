import os

"""L'utilisateur rentre une année dont on veut verifier la bissextilité"""
annee = input("Quelle année voulez verifier ?\n")
annee = int(annee)

bissextile = False

if (annee % 400 == 0) or ((annee % 4 == 0) and (annee % 100 != 0)):
    bissextile = True

if bissextile == True:
    print("L'année " + str(annee) + " est bissextile")
else:
    print("L'année " + str(annee) + " n'est pas bissextile")

os.system("pause")
