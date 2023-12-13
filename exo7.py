# Écrivez un programme pour calculer la factorielle d'un nombre entier

nombre = int(input("Entrez un nombre:"))

if nombre < 0:
    print("La factorielle n'est définie que pour les nombres entiers positifs")
elif nombre == 0:
    print("La factorielle de 0 est 1.")
else:
    resultat = 1
    for i in range(1, nombre + 1):
        resultat *= i
    print(f"La factorielle de {nombre} est {resultat}.")
