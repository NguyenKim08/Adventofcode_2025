nb_depasse = 0      # nombre de fois où on passe par  0
x = 50              # position de départ

with open("test.txt", "r") as file:
    for line in file:
        line = line.strip()
        if not line:
            continue 

        lettre = line[0]           # la direction
        steps = int(line[1:])      # nombre de clics à faire

        # direction : +1 pour R, -1 pour L
        step = 1 if lettre == "R" else -1

        # on avance "steps" fois, clic par clic
        for _ in range(steps):
            x = (x + step) % 100   # on met à jour la position
            if x == 0:             # si l'aiguille pointe sur 0
                nb_depasse += 1    # on compte 1 passage

print(nb_depasse)
