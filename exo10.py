# Créez une calculatrice simple qui permet d'effectuer des opérations d'addition, de soustraction, de multiplication et de division.

def calculatrice(number1, number2, operation):
    if operation == "+":
        return number1+ number2
    elif operation == "-":
        return number1 - number2
    elif operation == "":
        return number1 * number2
    elif operation == "/":
        if number2 == 0:
            return "La division par zéro n'est pas autorisée."
        return number1 / number2
    else:
        return "Opération invalide."


nombre1 = float(input("Entrez un nombre : "))
nombre2 = float(input("Entrez un deuxième nombre : "))


operation = input("Entrez l'opération (+, -, *, /) : ")


resultat = calculatrice(nombre1, nombre2, operation)


print(f"Le résultat de {nombre1} {operation} {nombre2} est égal à : {resultat}")
