class Personne:
    """Classe représentant une personne"""
    def __init__(self, nom):
        """Constructeur de notre classe"""
        self.nom = nom
        self.prenom = "Martin"
    def __str__(self):
        """Méthode appelée lors d'une conversion de l'objet en chaîne"""
        return "{0} {1}".format(self.prenom, self.nom)

class AgentSpecial(Personne):
    """Classe définissant un agent spécial.
    Elle hérite de la classe Personne"""
    
    def __init__(self, nom, matricule):
        """Un agent se définit par son nom et son matricule"""
        # On appelle explicitement le constructeur de Personne :
        Personne.__init__(self, nom)
        self.matricule = matricule
    def __str__(self):
        """Méthode appelée lors d'une conversion de l'objet en chaîne"""
        return "Agent {0}, matricule {1}".format(self.nom, self.matricule)

agent = AgentSpecial("Fischer", "0402-998")

"""On veut afficher l'objet grâce a la méthode __str__"""
print(agent)
"""Cependant si l'on veut utiliser la méthode spéciale __str__ de la classe Personne il faut le préciser"""
print(Personne.__str__(agent))

"""On veut verifier qu'une classe est une sous classe d'une autre"""
print(issubclass(AgentSpecial, Personne))
print(issubclass(Personne, AgentSpecial))

"""On veut verifier qu'un objet est issu d'une classe ou d'une de ses classes filles"""
print(isinstance(agent, Personne))
print(isinstance(agent, AgentSpecial))



"""On peut faire heriter une classe de plusieurs classes !"""
class Mammifere:
    """Classe représentant un animal"""
    def __init__(self):
        self.vertebre = True

    def __str__(self):
        return "Les animaux sont tous des vertébrés !"
    
class Chien:
    """Classe représentant un chien"""
    def __init__(self):
        self.poil = True

    def __str__(self):
        return "Tout les chiens ont des poils"
    
class Teckel(Mammifere,Chien):
    """Classe représentant un teckel"""
    def __init__(self):
        self.corps_de_saucisse = True

    def __str__(self):
        return "Sont rigolos ces petites saucisses !"

google = Teckel()
print(google)
print(Mammifere.__str__(google))
print(Chien.__str__(google))

"""Lors de la recherche de méthode, python va déjà chercher dans la classe fille puis dans la première classe Mère (Mammifere ici) puis dans la seconde Classe Mère (Chien)  etc..."""


#Les exceptions sont des classes hiérarchisées !!!


