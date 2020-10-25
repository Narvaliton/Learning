# -*- coding: utf-8 -*-

class Dict_Ord:
    """Dictonnaire ordonné, contrairement aux dictionnaires les clés et valeurs
    sont stockés dans 2 listes distinctes et peuvent donc être triés et manipulés"""

    def __init__(self, dictio = {}, **kwargs):
        """Constructeur du dictionnaire, peut être construit sans argument et sera donc vide ou
        prendre en paramètre :
        -    un dictionnaire: notre dictionnaire contiendra alors le contenu de ce dictionnaire
        -    des valeurs nommées qui seront nos couples clé/valeur"""

        self.cle = []
        self.valeur = []
        for key, value in dictio.items():
            self.cle.append(key)
            self.valeur.append(value)
        for key, value in kwargs.items():
            self.cle.append(key)
            self.valeur.append(value)

    def __repr__(self):
        """Représentation de notre dictionnaire dans l'interpreteur ou en utilisant
        la fonction repr."""
        
        affichage = "Voici le contenu de votre dictionnaire ordonné :\n"
        i = 0
        while i < len(self.cle):
            affichage +=("La clé est {} et à pour valeur {}\n".format(self.cle[i], self.valeur[i]))
            i += 1
        return affichage
    
    def __str__(self):
        """Fonction appelée quand on souhaite afficger notre dictionnaire grâce à la
        fonction print"""
        
        affichage = "Voici le contenu de votre dictionnaire ordonné :\n"
        i = 0
        while i < len(self.cle):
            affichage +=("La clé est {} et a pour valeur {}\n".format(self.cle[i], self.valeur[i]))
            i += 1
        return affichage

    def __delitem__(self, cle):
        """Méthode appelée quand on souhaite supprimer une clé et sa valeurs
        grâce à la méthode : del Dict_Ord[cle]"""
        
        indice = self.cle.index(cle)
        self.cle.pop(indice)
        self.valeur.pop(indice)

    def __getitem__(self, cle):
        """Méthode retournant la valeur lié à la clé choisie, Dict_Ord[cle]"""
        return self.valeur[self.cle.index(cle)]
        
    def __setitem__(self, cle, newValue):
        """Méthode modifiant la valeur d'une clé si la clé existe, sinon
        la crée"""
        
        if (cle in self.cle): 
            self.valeur[self.cle.index(cle)] = newValue
        else:
            self.cle.append(cle)
            self.valeur.append(newValue) 

    def __len__(self):
        """Méthode affichant le nombre de couple clé/valeur"""
        return len(self.cle)
    
    def sort(self, rvrs=False):
        """Méthode permettant de trier notre dictionnaire en fonction de ses clés
        Si rvrs = True, le dictionnaire est trié puis inversé grâce à la méthode reverse()"""
        
        liste_valeur_triee = []
        liste_cle_triee = sorted(self.cle)
        for cle in (liste_cle_triee):
            indice = self.cle.index(cle)
            liste_valeur_triee.append(self.valeur[indice])
        self.cle = liste_cle_triee
        self.valeur = liste_valeur_triee
        if rvrs == True:
            self.reverse()
            
    def reverse(self):
        """Methode inversant l'ordre de notre dictionnaire"""
        self.cle.reverse()
        self.valeur.reverse()

    def __iter__(self):
        """Methode de parcours du dictionnaire. On renvoit l'iterateur de la liste de clés"""
        return iter(self.cle)

    def keys(self):
        """Méthode retournant la liste de clés de notre dictionnaire"""
        return self.cle

    def values(self):
        """Méthode retournant la liste de valeurs de notre dictionnaire"""
        return self.valeur
    
    def items(self):
        """Méthode retournant une liste de couple clé/valeur"""
        
        i = 0
        dic_couple = []
        while i < len(self.cle):
            dic_couple.append((self.cle[i],self.valeur[i]))
            i += 1
        return dic_couple

     
    def __add__(self, dict2):
        """Méthode renvoyant un nouveau couple contenant les 2 dictionnaires passés en paramètre
        ex: dico1 + dico2"""
        if type(self) is type(dict2):
            raise TypeError(\
                "Impossible de concatener {} et {}".format(\
                type(self), type(dict2)))
        else:
            new = Dict_Ord()
            for key, value in self.items():
               new[key] = value
            
            for key, value in dict2.items():
                new[key] = value
            return new

        
