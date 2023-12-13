# Créez un programme qui génère un mot de passe aléatoire en fonction des préférences de l'utilisateur (longueur, caractères spéciaux, etc.)

import random
import string

longueur = int(input("Entrez la longueur du mot de passe : "))
inclure_speciaux = input("Inclure des caractères spéciaux ? (oui/non) ").lower() == "oui"

caracteres = string.ascii_letters + string.digits 
if inclure_speciaux:
    caracteres += string.punctuation

mot_de_passe = ''.join(random.choice(caracteres) for _ in range(longueur))

print(f"Mot de passe généré : {mot_de_passe}")