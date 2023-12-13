# Créez un programme qui vérifie si un nombre est pair ou impair

nombre = input("Entrez un nombre:")

if int(nombre) % 2 == 0:
    print(f"Ce nombre {nombre} est pair.")
else:
    print(f"Ce nombre {nombre} n'est pas pair.")
