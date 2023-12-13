# Créez un convertisseur de devises qui convertit une somme en euros en une autre devise

def convertisseur(euros, taux_de_change):
    montant_converti = euros * taux_de_change
    return montant_converti


taux_livres =  0.86


euros = float(input("Entrez le montant en euros : "))

livres = convertisseur(euros, taux_livres)


print(f"{euros} euros sont équivalants à {livres} livres sterling.")
