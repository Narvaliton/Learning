import re
import os
import pickle
from donnees import *
from random import *
#os.chdir("C:/Users/Max/Desktop/Programmation/Python/Pendu")
    
    
    #Ouverture du fichier et split de la string obtenu
    #grace à re.split qui renvois une liste découpée par les séparateurs
    #indiqués
    #    Les séparateurs sont séparés par |
    
def import_scores(monfichier):
    with open(monfichier,"rb") as dico_f:
        pickler = pickle.Unpickler(dico_f)
        try:
            scores = pickler.load()
        except:
            scores ={}
    return scores            
        
def export_scores(monfichier, scores):
    with open(monfichier,"wb") as dico_f:
            pickler = pickle.Pickler(dico_f)
            pickler.dump(scores)

       
#Retourne une chaine de caractère, tirée au hasard dans la liste liste_de_mot
def tirer_mot():
    return liste_de_mot[randrange(34)]
    
    
    
#Crée une chaine de caractère composée uniquement de "-" mesurant la longueur de l'entier passer en paramètre
def creer_mot_inconnu(longueur):
    i = 0
    mot_inconnu = ""
    while i < longueur:
        mot_inconnu = mot_inconnu + "-"
        i += 1
    return mot_inconnu
    
    
def win_ou_pas(mot_inconnu):
    if mot_inconnu.count("-") == 0:
        return True
    else:
        return False
    
#Cherche si la lettre est présente dans le mot à trouver. Si c'est le cas, renvoit une chaine str du mot "censuré" avec la lettre trouvée visible
#Sinon renvois -1    
def check_mot_inconnu(lettre, mot, mot_inconnu):

    if (lettre.lower() in mot.lower()) == True and (lettre.lower() not in mot_inconnu):
        for m in re.finditer(lettre, mot):
            if (m.start()) == mot.__len__() + 1:
                mot_inconnu = mot_inconnu[:m.start()] + lettre 
            elif (m.start()) == 0:
                mot_inconnu = lettre + mot_inconnu[1:mot.__len__()] 
            else:
                mot_inconnu = mot_inconnu[:m.start()] + lettre + mot_inconnu[m.start() + 1:]
        return mot_inconnu
    return -1