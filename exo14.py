# Écrivez un jeu de pendu où l'utilisateur doit deviner un mot secret


import random

mots_secrets = ["python","crocodile", "florent", "richnou"]
mot_secret = random.choice(mots_secrets)
lettres_correctes = set()
max_essais = 7



while max_essais > 0:
    mot_affiche = ''.join([lettre if lettre in lettres_correctes else '' for lettre in mot_secret])
    print(f"Mot secret : {mot_affiche}")

    lettre_ok = input("Devinez une lettre : ").lower()

    if len(lettre_ok) != 1 or not lettre_ok.isalpha():
        print("Veuillez entrer une seule lettre valide.")
        continue

    if lettre_ok in lettres_correctes:
        print("Vous avez déjà deviné cette lettre.")
    elif lettre_ok in mot_secret:
        lettres_correctes.add(lettre_ok)
        print("Bonne devinette !")

        if set(mot_secret) <= lettres_correctes:
            print(f"Bravo ! Le mot secret était '{mot_secret}'. Vous avez gagné !")
            break
    else:
        max_essais -= 1
        print(f"Mauvaise devinette. Il vous reste {max_essais} essais.")
   