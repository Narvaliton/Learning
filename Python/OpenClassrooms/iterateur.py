"""Les iterateurs"""

mchaine = "Test d'iterateur"
iterateur = iter(mchaine)
iterateur
print(next(iterateur))
print(next(iterateur))

class RevStr(str):
    def __iter__(self):
        return ItRevStr(self)

class ItRevStr:
    def __init__(self, chaine):
        self.chaine = chaine
        self.position = len(chaine)
    def __next__(self):
        if self.position == 0:
            raise StopIteration
        self.position -= 1
        return self.chaine[self.position]
    

"""LEs générateurs"""
def mon_generateur():
    """Va simplement renvoyer 1,2 et 3"""
    yield 1
    yield 2
    yield 3

def generateur_compte(a, b, rvrs=False):
    if rvrs == False:
        a +=1
        while a < b:
            yield a
            a += 1
    else:
        b-=1
        while b > a:
            yield b
            b -= 1

"""On peut interrompre une boucle à l'aide de la méthode close()"""
gen1 = generateur_compte(10,40)
for num in gen1:
    print(num)
    if(num == 20):
        gen1.close()

def intervalle(borne_inf, borne_sup):
    """Générateur parcourant la série des entiers entre borne_inf et borne_sup.
    Notre générateur doit pouvoir "sauter" une certaine plage de nombres
    en fonction d'une valeur qu'on lui donne pendant le parcours. La
    valeur qu'on lui passe est la nouvelle valeur de borne_inf.
    
    Note: borne_inf doit être inférieure à borne_sup"""
    borne_inf += 1
    while borne_inf < borne_sup:
        valeur_recue = (yield borne_inf)
        if valeur_recue is not None: # Notre générateur a reçu quelque chose
            borne_inf = valeur_recue
        borne_inf += 1
        
"""On peut envoyer une valeur a notre generateur grace à la méthode send()"""
generateur = intervalle(10, 25)
for nombre in generateur:
    if nombre == 15: # On saute à 20
        generateur.send(20)
    print(nombre, end=" ")



