# Écrivez un programme qui compte le nombre de voyelles dans une chaîne de caractères saisie par l'utilisateur

chaine = input("Entrez une chaîne de caractères : ")

nombre_voyelles = 0

voyelles = ['a','e','i','o','u','y','A','E','I','O','U','Y']


for caractere in chaine:
    if caractere in voyelles:
        nombre_voyelles += 1

print(f"Le nombre de voyelles est : {nombre_voyelles}")