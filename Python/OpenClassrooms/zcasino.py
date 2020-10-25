from random import randrange
from math import ceil
argent = 100

while argent > 0:
    pari = -1
    #On demande au joueur de parier sur une case de la roulette
    while pari < 0 or pari > 49:
        pari = input("Sur quel case voulez vous parier ? (Entre 0 et 49)\n")
        try:
            pari = int(pari)
        except ValueError:
            print("Vous n'avez pas saisi un entier")
            pari = -1
    montantPari = 0

    #On demande au joueur de miser
    while montantPari <= 0 or montantPari > argent:
        montantPari = input("Combien voulez vous parier ? Vous avez actuellement " + str(argent) + "\n")
        try:
            montantPari = int(montantPari)
        except ValueError:
            print("Vous n'avez pas saisi un entier")
            montantPari = 0

    #On fait tourner la roulette    
    case = randrange(50)
    print("La bille s'est arretée sur la case " + str(case))

    #On calcule les gains ou les pertes
    if(pari == case):
        argent += montantPari * 3
        print("Vous êtes tombé sur la bonne case, vous remportez " + str(montantPari*3))
    elif(pari % 2 == case % 2):
        mise = ceil(montantPari * 0.5)
        argent += mise
        print("La case est de la même couleur, vous remportez " + str(mise))
    else:
        argent -= montantPari
        print("Perdu !")
        
