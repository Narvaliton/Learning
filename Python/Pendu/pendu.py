from donnees import *
from fonctions import *
import os

#Changement de dossier cible
os.chdir("E:\Python\Pendu")
#Import des saves
scores = import_scores("scores.txt")

print("Bienvenu sur Pendu2000, le nouveau jeu EA \nQuel est votre pseudo ?")
nom_j = input()
if scores.__contains__(nom_j) == False:
    scores[nom_j] = 0
    score = 0
    print("Oh je ne vous connais pas " + nom_j + "\nVous commencerez avec un score de 0")
else:
    score = int(scores[nom_j])
    print("Vous êtes de retour " + nom_j + ". Reprenons votre score qui était de " + str(score))



#La partie commence
while continue_partie == True:
    mot_choisi = tirer_mot().lower()
    nb_lettre = len(mot_choisi)
    print("Votre mot a été tiré, il est composé de " + str(nb_lettre) + " lettres")
    mot_inconnu = creer_mot_inconnu(nb_lettre)
    while nb_essai > 0 and (gagner == False):
        print(mot_inconnu + "\n Quel lettre choisissez vous ? Vie restante : " + str(nb_essai)) 
        lettre_choisi = input()
        if check_mot_inconnu(lettre_choisi, mot_choisi, mot_inconnu) != -1:
            mot_inconnu = check_mot_inconnu(lettre_choisi, mot_choisi, mot_inconnu)
            gagner = win_ou_pas(mot_inconnu)
        else:
            nb_essai -= 1
            print("Perdu essaye à nouveau !")
    if gagner == True:
        score += nb_essai
        print("Bravo vous avez réussi, votre mot était : "+ mot_choisi + "\n Votre score est de : " + str(score))
        scores[nom_j] = score
        export_scores("scores.txt", scores)
    else:
        print("Vous avez perdu :( !")
    
    from donnees import reponse    
#La partie est terminée        
    print("Voulez vous continuer à jouer ? y/n")   
    while reponse != "y" and reponse != "n":
        reponse = input()
        if reponse == "n":
            continue_partie = False
        elif reponse == "y": 
            from donnees import nb_essai
            from donnees import gagner

            
            
    
os.system("pause")
