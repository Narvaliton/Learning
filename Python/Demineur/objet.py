class Case:
    """Objet case permettant de définir l'état de chaque case de notre démineur"""
    
    def __init__(self, coord_x, coord_y, bombes_proche=0, bombe=False, neutraliser=False):
        """Constructeur de la classe Case
        
        Paramètres nommés:
        coord_x -- entier représentant sa position sur l'axe x
        coord-y -- entier représentant sa posotion sur l'axe y
        bombes_proche -- entier représentant le nombre de bombe sur les cases proches
        bombe -- Booléen indiquant si la case possède une bombe
        
        """
        
        self.x = coord_x
        self.y = coord_y
        self.bombes_proche = bombes_proche
        self.bombe = bombe
        self.neutraliser = neutraliser
        
    def __repr__(self):
        if self.bombe is False:
            chaine = "La case {},{} est vide".format(self.x,self.y)
        else:
            chaine = "La case {},{} contient une bombe".format(self.x,self.y)
        return chaine    
    
    
    def __str__(self):
        return repr(self)


        