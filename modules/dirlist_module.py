import os

# utilise la fonction os.listdir pour consulter le repertoire courant et retourne en string le resultat

def run(**args) :
    print("[*] consultation du repertoire courant")
    retour=os.listdir(".")

    return str(retour)



