mon_dictionnaire = {}
mon_dictionnaire["pseudo"] = "Prolixe"
mon_dictionnaire["mot de passe"] = "*"
mon_dictionnaire["pseudo"] = "6pri1"

placard = {"chemise":3, "pantalon":6, "tee-shirt":7}
mon_set = {'pseudo', 'mot de passe'}#Ceci est un set
placard.pop("chemise")

#La fonction pop en plus de supprimer la clé et sa valeur, retourne celle-ci
var_suppr = mon_dictionnaire.pop("pseudo")
del mon_dictionnaire["mot de passe"]

#On parcourt le dictionnaire en affichant toutes les clés
for cle in placard.keys():
    print(cle)
#On parcourt le dicitonnaire en affichant toutes les valeurs
for value in placard.values():
    print(value)

#On parcourt le dictionnaire en affichant clés et valeurs en les formatants
for cle, value in placard.items():
    print("La clé est {} et a pour valeur {}".format(cle,value))

#La fonction suivante peut prendre des paramètres non nommés et d'autres nommés
def fonction_inconnue(*en_liste, **en_dictionnaire):
    liste = []
    liste = [*en_liste]
    dictionnaire = {}
    dictionnaire = {**en_dictionnaire}

    for key, value in dictionnaire.items():
        print("La variable {} a pour valeur {}".format(key, value))

#Equivaut à:
    for key, value in en_dictionnaire.items():
        print("La variable {} a pour valeur {}".format(key, value))


