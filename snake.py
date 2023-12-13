# Créer un jeu Snake en utilisant en Python. Je rajoute des contraintes : 
# vitesse : Le jeu doit permettre aux joueurs de choisir entre trois niveaux de vitesse différents (facile, moyen, difficile) qui influenceront la vitesse de déplacement du serpent. Vous devrez mettre en place une gestion de la vitesse du jeu en fonction du niveau choisi
# taille du serpent : Le serpent devra grandir progressivement à chaque fois qu'il mangera
# collision : Si le serpent entre en collision avec lui-même ou avec les bords de l'écran, le joueur doit également perdre la partie
# score : Le jeu doit suivre et afficher le score du joueur, qui augmente chaque fois que le serpent mange une proie
# contrôles : Vous devez mettre en place des contrôles pour permettre au joueur de diriger le serpent (ex:les flèches du clavier)


import pygame
import random

# Initialisation de Pygame
pygame.init()

# Couleurs du jeu
BLANC = (255, 255, 255)
VERT = (0, 255, 0)
HERSHEYS = (154, 132, 120)

# Paramètres 
largeur, hauteur = 640, 480
taille_case = 20
vitesse_initiale = 10
difficultes = {"Facile": 10, "Moyen": 15, "Difficile": 25}

ecran = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Snake")

# Afficher le score
def afficher_score(score):
    font = pygame.font.Font(None, 36)
    texte = font.render(f"Score: {score}", True, BLANC)
    ecran.blit(texte, (10, 10))

# Fonction principale
def jouer(difficulte):
    serpent = [(largeur // 2, hauteur // 2)]
    direction = (1, 0)
    proie = (random.randint(0, largeur // taille_case - 1) * taille_case,
             random.randint(0, hauteur // taille_case - 1) * taille_case)
    score = 0
    vitesse = difficultes[difficulte]

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != (0, 1):
                    direction = (0, -1)
                elif event.key == pygame.K_DOWN and direction != (0, -1):
                    direction = (0, 1)
                elif event.key == pygame.K_LEFT and direction != (1, 0):
                    direction = (-1, 0)
                elif event.key == pygame.K_RIGHT and direction != (-1, 0):
                    direction = (1, 0)

        serpent.insert(0, (serpent[0][0] + direction[0] * taille_case, serpent[0][1] + direction[1] * taille_case))

        # Collisions
        if serpent[0] == proie:
            proie = (random.randint(0, largeur // taille_case - 1) * taille_case,
                     random.randint(0, hauteur // taille_case - 1) * taille_case)
            score += 1
        else:
            serpent.pop()

        if (serpent[0] in serpent[1:] or
            serpent[0][0] < 0 or serpent[0][0] >= largeur or
            serpent[0][1] < 0 or serpent[0][1] >= hauteur):
            return score

        ecran.fill(HERSHEYS)
        for segment in serpent:
            pygame.draw.rect(ecran, VERT, (segment[0], segment[1], taille_case, taille_case))
        pygame.draw.rect(ecran, BLANC, (proie[0], proie[1], taille_case, taille_case))
        afficher_score(score)
        pygame.display.update()

        clock.tick(vitesse)

# Difficulté du jeu
def menu():
    font = pygame.font.Font(None, 48)
    choix = None
    while choix is None:
        ecran.fill(HERSHEYS)
        texte_facile = font.render("Facile", True, BLANC)
        texte_moyen = font.render("Moyen", True, BLANC)
        texte_difficile = font.render("Difficile", True, BLANC)
        ecran.blit(texte_facile, (200, 100))
        ecran.blit(texte_moyen, (200, 200))
        ecran.blit(texte_difficile, (200, 300))
        
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if 200 <= x <= 200 + texte_facile.get_width() and 100 <= y <= 100 + texte_facile.get_height():
                    choix = "Facile"
                elif 200 <= x <= 200 + texte_moyen.get_width() and 200 <= y <= 200 + texte_moyen.get_height():
                    choix = "Moyen"
                elif 200 <= x <= 200 + texte_difficile.get_width() and 300 <= y <= 300 + texte_difficile.get_height():
                    choix = "Difficile"

    return choix

# Boucle principale du jeu
while True:
    difficulte = menu()
    score_final = jouer(difficulte)

    font = pygame.font.Font(None, 48)
    texte_fin = font.render(f"Score final: {score_final}", True, BLANC)
    ecran.fill(HERSHEYS)
    ecran.blit(texte_fin, (200, 200))
    pygame.display.update()

    pygame.time.delay(4000)  
    # Affiche le score final 
