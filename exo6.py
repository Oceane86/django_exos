# Demandez à l'utilisateur de saisir un nombre, puis vérifiez s'il est positif, négatif ou nul


nombre = input("Entrez un nombre:")

if int(nombre) > 0:
    print(f"Ce nombre {nombre} est positif.")

elif int(nombre) < 0:
    print(f"Ce nombre {nombre} est négatif.")
else:
    print(f"Ce nombre {nombre} est égal à 0.")
