import tkinter as tk
import tkinter.messagebox
from objet import *
import random
from os import *

window = tk.Tk()
window.geometry("")
#Valeur par défault 
taille = 5
nb_bombes = 5
champ = []
boutons = []
gameover = False

#Couleur pour dans l'ordre : 0 (blanc), 1 (bleu), 2 (vert), 3 (rouge), 4 (bleu claire), 5 (marron)
colors = ['#FFFFFF','#0000FF', '#008200', '#FF0000', '#000084', '#840000']



def creer_echiquier(taille):
    """Créer une liste d'Objet Case qui représentera notre démineur
    
    Retourne la liste crée
    taille -- Taille des cotés de notre "échiquier"
    
    """
    liste_case = list(range(taille*taille))
    indice = 0
    axe_x = 1
    while axe_x <= taille:
        axe_y = 1
        while axe_y <= taille:
            liste_case[indice] = Case(axe_x,axe_y, 0,False)
            indice += 1
            axe_y += 1
        axe_x += 1    
    return liste_case


def poser_bombes(liste_case, nb_bombes, taille):
    """Change des cases vides en bombe et retourne la liste modifiée
    
    liste_case -- Liste d'objet Case sans bombe
    nb_bombes -- Nombre de case a modifier en bombe
    
    
    
    """
    liste = list(range(taille*taille))
    i = 0
    while i < nb_bombes:
        indice = random.choice(liste)
        liste.remove(indice)
        liste_case[indice].bombe = True
        i += 1
    return liste_case
    
    
def check_bombe(case, compteur):
        if case.bombe is True:
            compteur += 1 
        return compteur    
    

    
def check_all_bombes(liste_case, taille):
        for i,elt in enumerate(liste_case):
            compteur = 0
            if liste_case[i].bombe is False:
                #Cette condition verifie si la case verifiée est le coin superieur gauche
                if (i==0):
                    compteur = check_bombe(liste_case[i+1],compteur)
                    compteur = check_bombe(liste_case[i+taille],compteur)    
                    compteur = check_bombe(liste_case[i+taille+1],compteur)
                    
                #Cette condition verifie si la case verifiée est le coin superieur droit
                elif i == taille-1:
                    compteur = check_bombe(liste_case[i-1],compteur)
                    compteur = check_bombe(liste_case[i+taille-1],compteur)
                    compteur = check_bombe(liste_case[i+taille],compteur)
                    
                #Cette condition verifie si la case verifiée est le coin inférieur gauche
                elif i == taille*(taille-1):
                    compteur = check_bombe(liste_case[i-taille],compteur)
                    compteur = check_bombe(liste_case[i-taille+1],compteur)
                    compteur = check_bombe(liste_case[i+1],compteur)
                
                #Cette condition verifie si la case verifiée est le coin inférieur droit
                elif i==(len(liste_case)-1):
                    compteur = check_bombe(liste_case[i-1],compteur)
                    compteur = check_bombe(liste_case[i-taille],compteur)
                    compteur = check_bombe(liste_case[i-taille-1],compteur)
                
                #Cette condition verifie si la case verifiée est entre les coins superieurs de l'echiquier
                elif ((i > 0) and (i < (taille-1))):
                    compteur = check_bombe(liste_case[i-1],compteur)
                    compteur = check_bombe(liste_case[i+1],compteur)
                    compteur = check_bombe(liste_case[i+taille-1],compteur)
                    compteur = check_bombe(liste_case[i+taille],compteur)
                    compteur = check_bombe(liste_case[i+taille+1],compteur)
                    
                #Cette condition verifie si la case verifiée est entre les coins inferieurs de l'echiquier
                elif (i > taille*(taille-1)) and (i < len(liste_case)-1):
                    compteur = check_bombe(liste_case[i-1],compteur)
                    compteur = check_bombe(liste_case[i+1],compteur)
                    compteur = check_bombe(liste_case[i-taille-1],compteur)
                    compteur = check_bombe(liste_case[i-taille],compteur)
                    compteur = check_bombe(liste_case[i-taille+1],compteur)
                
                #Cette condition verifie si la case verifiée est entre les coins gauche de l'echiquier
                elif (i % taille == 0) and (i != 0) and (i != (taille*(taille-1))):
                    compteur = check_bombe(liste_case[i+1],compteur)
                    compteur = check_bombe(liste_case[i-taille],compteur)
                    compteur = check_bombe(liste_case[i-taille+1],compteur)
                    compteur = check_bombe(liste_case[i+taille],compteur)
                    compteur = check_bombe(liste_case[i+taille+1],compteur)
                
                #Cette condition verifie si la case verifiée est entre les coins droit de l'echiquier
                elif (((i+1) % taille) == 0) and (i != (taille - 1)) and (i != len(liste_case)-1):
                    compteur = check_bombe(liste_case[i-1],compteur)
                    compteur = check_bombe(liste_case[i-taille-1],compteur)
                    compteur = check_bombe(liste_case[i-taille],compteur)
                    compteur = check_bombe(liste_case[i+taille-1],compteur)
                    compteur = check_bombe(liste_case[i+taille],compteur)
                    
                #Toutes les cases n'étant pas sur un bord de l'echiquier
                else:
                    if (i < ((len(liste_case) - taille - 1))):
                        try:
                            compteur = check_bombe(liste_case[i-taille-1],compteur)
                            compteur = check_bombe(liste_case[i-taille],compteur)
                            compteur = check_bombe(liste_case[i-taille+1],compteur)
                            compteur = check_bombe(liste_case[i-1],compteur)
                            compteur = check_bombe(liste_case[i+1],compteur)
                            compteur = check_bombe(liste_case[i+taille-1],compteur)
                            compteur = check_bombe(liste_case[i+taille],compteur)
                            compteur = check_bombe(liste_case[i+taille+1],compteur)
                        except IndexError:
                            print("La case : " + str(i))
            liste_case[i].bombes_proche = compteur


def creerMenu():

    menubar = tk.Menu(window)
    menu_difficulte = tk.Menu(window, tearoff=0)
    menu_difficulte.add_command(label= "Facile : 5x5 et 5 bombes", command= lambda : changerTaille(5,5))
    menu_difficulte.add_command(label= "Moyen : 10x10 et 20 bombes", command= lambda : changerTaille(10,20))
    menu_difficulte.add_command(label= "Difficile : 20x20 et 100 bombes", command= lambda : changerTaille(20,100))
    menubar.add_cascade(label= "Difficultés", menu=menu_difficulte)
    menu_exit = tk.Menu(window, tearoff=0)
    menubar.add_command(label= "Quitt.", command= lambda: window.destroy())
    window.config(menu = menubar)
    
    
def miseEnPlace():
    global taille, nb_bombes, champ, boutons
    champ = []
    boutons = list(range(taille*taille))
    champ = creer_echiquier(taille)
    champ = poser_bombes(champ, nb_bombes, taille)
    check_all_bombes(champ, taille)
    for x in range(taille*taille):
            b = tk.Button(window, text=" ", width=2, command= lambda x=x : clique_g(x))
            b.grid(row=(x//taille), column=(x%taille), sticky=tk.N+tk.S+tk.W+tk.E)
            b.bind('<Button-3>', lambda e, x=x : cliqueDroit(x))
            boutons[x]= b
    b= tk.Button((window), text= " Recommencer ", command= recharger)
    b.grid(row=taille, column=0, columnspan=taille, sticky=tk.W+tk.E)
    boutons.append(b)
    
def clique_g(x):
    global boutons, champ, gameover, colors
    if boutons[x]["text"] != "?" and gameover is False:
        if champ[x].bombe is True:
            boutons[x]["text"] = "X"
            gameover = True
            for i, case in enumerate(champ):
                if case.bombe is True:
                    boutons[i]["text"] = "X"
                    boutons[x].config(bg= 'red', relief=tk.SUNKEN)
                    gameover = True
        elif champ[x].bombes_proche != 0:
            boutons[x]["text"] = str(champ[x].bombes_proche)
            boutons[x].config(disabledforeground = colors[champ[x].bombes_proche])
            boutons[x].config(relief=tk.SUNKEN)
            boutons[x]['state'] = 'disabled'
  

    checkVictoire()
    autoValidation(x)

def checkVictoire():
    global boutons, champ, nb_bombes
    case_valide = 0
    for indice, elt in enumerate(champ):
       if (champ[indice].bombe is False) and (boutons[indice]['state'] == 'disabled'):
           case_valide += 1
    if len(champ) == (case_valide + nb_bombes):
        tk.messagebox.showinfo("Terminé", "Vous avez gagné !")
    if gameover is True:
        tk.messagebox.showinfo("Terminé", "Vous avez perdu !")

def cliqueDroit(x):
    global boutons, champ
    if boutons[x]['state'] == 'normal':
        if boutons[x]["text"] != "?" :
            boutons[x]["text"] = "?"
        else:
            boutons[x]["text"] = " "
    
def autoValidation(x):
    global boutons, champ, taille
    if champ[x].bombes_proche == 0 and champ[x].bombe is False and boutons[x]['state'] == 'normal':
        boutons[x]["text"] = " "
        boutons[x].config(relief=tk.SUNKEN)
        boutons[x]['state'] = 'disabled'
        #Si x est la case en haut à gauche
        if x == 0:
            clique_g(1)
            clique_g(taille)
            clique_g(taille+1)
        #Si x est la case en haut à droite
        elif x == (taille-1):
            clique_g(x-1)
            clique_g(x+taille)
            clique_g(x+taille-1)
        #Si x est la case en bas à gauche
        elif x == (taille*(taille-1)):
            clique_g(x+1)
            clique_g(x-taille+1)
            clique_g(x-taille)
        #Si x est la case en bas à droite
        elif x == (len(champ)-1):
            clique_g(x-taille)
            clique_g(x-taille-1)
            clique_g(x-1)
        elif (x % taille == 0) and (x != 0) and (x != (taille*(taille-1))):
            clique_g(x-taille)
            clique_g(x-taille+1)
            clique_g(x+1)
            clique_g(x+taille)
            clique_g(x+taille+1)
        elif ((x+1)%taille == 0) and (x != len(champ)-1) and (x != (taille-1)):
            clique_g(x-taille-1)
            clique_g(x-taille)
            clique_g(x-1)
            clique_g(x+taille-1)
            clique_g(x+taille)
        elif (x in range(taille)) and (x != 0) and (x != taille-1):
            clique_g(x-1)
            clique_g(x+1)
            clique_g(x+taille-1)
            clique_g(x+taille)
            clique_g(x+taille+1)
        elif (x in range((len(champ)-taille+1),(len(champ)))):
            clique_g(x-taille-1)
            clique_g(x-taille)
            clique_g(x-taille+1)
            clique_g(x-1)
            clique_g(x+1)
        else:
            clique_g(x-taille-1)
            clique_g(x-taille)
            clique_g(x-taille+1)
            clique_g(x-1)
            clique_g(x+1)
            clique_g(x+taille-1)
            clique_g(x+taille)
            clique_g(x+taille+1)


def recharger():
    global taille, nb_bombes, champ, boutons, gameover
    gameover = False
    for widget in boutons:
        widget.destroy()
    gameover
    miseEnPlace()

def changerTaille(new_taille, new_nb_bombes):
    global taille, nb_bombes
    taille = new_taille
    nb_bombes = new_nb_bombes
    recharger()


    
creerMenu()
miseEnPlace()
window.mainloop()
