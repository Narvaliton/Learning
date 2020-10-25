"""Les classes"""

class Personne:
    """Classe définissant une personne caractérisée par :
    -son nom
    -son prénom
    -son âge
    -son lieu de résidence"""
    
    def __init__(self):
        self.nom = "Dupont"
        self.prenom = "Jean"
        self.age = 33
        self.lieu_residence = "Warmeriville"




class TableauNoir:
    """Classe définissant une surface sur laquelle on peut écrire,
    que l'on peut lire et effacer. L'attribut modifié
    est 'surface'"""

    def __init__(self):
        """Par défaut, notre surface est vide"""
        self.surface = ""
    def ecrire(self, message_a_ecrire):
        """Méthode permettant d'écrire sur la surface du tableau.
        Si la surface n'est pas vide, on saute une ligne avant de rajouter
        le message à écrire"""

        if self.surface != "":
            self.surface += "\n"
        self.surface += message_a_ecrire

    def effacer(self):
        """Cette méthode permet d'effacer la surface du tableau"""
        self.surface = ""


class Joueur:
    """Classe définissant un Joueur caractérisé par:
    -son pseudo
    -son nom
    -son prenom
    -son age"""


    def __init__(self):
        """Constructeur de l'objet Joueur"""
        self.pseudo = "Narvaliton"
        self.nom = "COLIN"
        self.prenom = "Maxime"
        self.age = 22

    def __del__(self):
        """Méthode spéciale de suppression"""
        print("L'objet a été supprimé")

    def __repr__(self):
        """Méthode spéciale définissant l'affichage de l'objet, utile pour le debuggage"""
        return "Le joueur {} s'appelle {} {} et a {} ans".format(self.pseudo, self.prenom, self.nom, self.age)

    def __str__(self):
        """Méthode spéciale définissant l'affichage de l'objet lorsqu'on cherche à l'afficher avec print()"""
        return """Vous avez utiliser la fonction print non ?
                Le joueur {} s'appelle {} {} et a {} ans""".format(self.pseudo, self.prenom, self.nom, self.age)

    def __getattr__(self, attr):
        """Methode spéciale appelée quand est entrée objet.attribut"""
        try:
            return self.attr
        except:
            print("Pas de tel attribut")

    def __setattr__(self, nomAttr, valeurAttr):
        """Méthode spéciale appelée quand on attribue une nouvelle valeur a un attribut d'un objet Joueur
                ex: objet.attr = nouvelleValeur"""
        object.__setattr__(self, nomAttr, valeurAttr) #Si l'on avait mit self.nomAttr alors la méthode se serait appeler elle même

    def __delattr__(self, attr):
        """Methode spéciale appelée quand on cherche a supprimer un attribut grâce à del self.attribut"""
        object.__delattr__(self, attr)
        
    
        
