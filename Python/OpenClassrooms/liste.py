"""Les listes"""

ma_liste = ['a','b','d','e']
#On insere 'c' à l'indice 2
ma_liste.insert(2,'c')
#On ajoute 'f' à la fin de la liste
ma_liste.extend('f')

#On supprime une variable
a = "Noooon"
del a
try:
    print(a)
except NameError:
    print("La variable n'existe pas")

#On supprime un élément de la liste en spécifiant l'élément et non l'indice
ma_liste2 = ['orange','bleu','rouge','vert', 'vert']
print(ma_liste2)
ma_liste2.remove('bleu')#Si l'élément est présent en plusieurs fois, seul 1 exemplaire sera supprimé
print(ma_liste2)

#On veut créer une fonction qui supprime toutes les occurences dans une liste
def removeAll(listToClean, word):
    while word in listToClean:
        listToClean.remove(word)
    return listToClean

#On liste grace a la fonction enumerate le contenu d'une liste
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for nb, elt in enumerate(alphabet):
    print("La lettre {} est la {}e de l'alphabet".format(elt,nb))

#On "soude" les éléments d'une liste avec une chaine de caractère
ma_liste = ['Bonjour', 'à', 'tous']
print(" ".join(ma_liste))

def afficher_flottant(flt):
    if type(flt)is not float:
        raise TypeError("Le paramètre doit etre un flottant")

    chaine = str(flt).split(".")
    fltModif = chaine[0] + "," + chaine[1][0:3]
    #Peut s'écrire aussi
    partie_entiere, partie_flottante = str(flt).split(".")
    fltModif = ",".join([partie_entiere, partie_flottante[:3]])
    return fltModif

#On cherche à créer une fonction qui trie une liste de tuples
inventaire = [
        ("pommes", 22),
        ("melons", 4),
        ("poires", 18),
        ("fraises", 76),
        ("prunes", 51),
]
inventaire_trie = []
for fruit, nb in inventaire:
    inventaire_trie.append((nb, fruit))
inventaire_trie.sort(reverse=True)
print(inventaire_trie)
