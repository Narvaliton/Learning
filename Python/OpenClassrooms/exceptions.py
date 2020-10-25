"""Test du bloc try"""
def division(numerateur, denominateur):
    try:
        resultat = numerateur / denominateur
    except NameError:
        print("La variable numerateur ou denominateur n'a pas été définie.")
    except TypeError:
        print("La variable numerateur ou denominateur possède un type incompatible avec la division.")
    except ZeroDivisionError:
        print("La variable denominateur est égale à 0.")
    else:
        print("Le résultat obtenu est " + str(resultat))
    finally:
        print("Le code est terminé :)")
      
division(50, "test")
division(50,0)
division(50, 10)


"""Les asserts"""
annee = input("Saisissez une année supérieure à 0 :")
try:
    annee = int(annee) # Conversion de l'année
    assert annee > 0
except ValueError:
    print("Vous n'avez pas saisi un nombre.")
except AssertionError:
    print("L'année saisie est inférieure ou égale à 0.")
