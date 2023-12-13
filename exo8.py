# Créez un jeu de devinette où l'ordinateur choisit un nombre aléatoire et l'utilisateur doit deviner ce nombre

import random 

nombre_mystere = random.randint(1,100)
nombre_essais = 0


print("Trouve le chiffre auquel je pense")

while True:
    nombre = int(input("Devinez le nombre :"))
    nombre_essais += 1

    if nombre == nombre_mystere:
        print(f"Bravo ! Vous avez deviné le bon nombre {nombre_mystere}")
        break
    elif nombre < nombre_mystere:
        print("Mon chiffre est plus grand")
    else:
        print("Mon chiffre est Plus petit")

