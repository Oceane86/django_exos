# Écrivez un programme Python qui affiche "Bonjour, Jules est souvent en retard, c'est pas bien !" à l'écran

message = f"""<!DOCTYPE html>
<html lang="fr">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Calendar</title>
    </head>
    <body>
       <p>Bonjour Jules est souvent en retard, c'est pas bien !</p>
        </hr>
    </body>
</html>
"""


f = open("message.html", "w")
f.write(message)
f.close()
