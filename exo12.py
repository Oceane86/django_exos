# Écrivez un jeu de pierre-papier-ciseaux où l'utilisateur joue contre l'ordinateur

import random

choix = ["pierre", "papier", "ciseaux"]

def resultat(utilisateur, ordinateur):
    return (
        "Égalité !" if utilisateur == ordinateur else
        "Vous avez gagné !" if (
            (utilisateur == "pierre" and ordinateur == "ciseaux") or
            (utilisateur == "papier" and ordinateur == "pierre") or
            (utilisateur == "ciseaux" and ordinateur == "papier")
        ) else
        "L'ordinateur a gagné !"
    )


while True:
    utilisateur = input("Choisissez pierre, papier ou ciseaux : ").lower()
    ordinateur = random.choice(choix)
    print(f"Vous avez choisi : {utilisateur}")
    print(f"L'ordinateur a choisi : {ordinateur}")
    print(resultat(utilisateur, ordinateur))
    if input("Voulez-vous rejouer ? (oui/non) ").lower() != "oui":
        break
