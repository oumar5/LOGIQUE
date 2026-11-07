# Ce TP nécessite l'installation du paquet python-sat. Le début de la feuille
# de TD explique comment procedeŕ pour cette installation.
from pysat.solvers import Minisat22

# Définition des variables utilisées

largeur = 7

# NB : on fait varier les valeurs des nombres possibles entre 1 et largeur^2.

nombres = range(largeur**2)

coord = range(largeur)

# Les variables propositionnelles sont associées à des triplets (i,j,k) où
# (i,j) repreśente une coordonnée dans la grille ((0,0) étant le coin en haut à
# gauche de la grille) et k est un nombre. La variable associée à (i,j,k) est
# vraie si et seulement si la case (i,j) de la grille contient le nombre k. On
# peut énumérer les variables dans la liste suivantes (qui n'est pas vraiment
# utile pour le TP).
variables = [(i,j,k) for i in coord for j in coord for k in nombres]

def encode(i,j,k):
    return 1 + k + (i + j * largeur) * largeur**2

def decode(n):
    m=n-1
    n1 = m // largeur ** 2
    return (n1 % largeur, n1 // largeur, m % largeur**2)


# Chaque case est occupée par au moins un nombre

phi1 = []

# Chaque case contient au plus un nombre

phi2 = []

# Chaque nombre apparaît au moins une fois dans la grille

phi3 = []

# Chaque nombre appraît au plus une fois dans la grille

phi4 = []

# Chaque nombre k est voisin du nombre k+1. Essayez de profiter des facilités
# d'écriture que python peut vous apporter.

phi5 = []

# Contrainte associée à la grille de l'énoncé. Attention aux indices utilisés.

phi6 = []

# Représenter à partir de formules SAT construite une formule SAT qui permette
# de résoudre le problème de l'énoncé :
# 1. commencez par utiliser toutes les contraintes
# 2. enlevez la contrainte phi4
# Que constatez vous ? Comment l'expliquer ?

psi = []


# Adaptez le code afin de pouvoir résoudre la grille suivante :
#
# |    |    | 60 |    | 68 | 67 | 64 |    |   1 |    |
# |    |    |    | 69 |    |    |    |    |     |  5 |
# |    |    |    | 42 | 55 |    |    |    |   4 |    |
# | 76 |    |    |    |    |    |    |    |     |  9 |
# | 77 |    |    | 38 |    |    | 49 | 12 |  10 |    |
# |    | 79 |    |    |    | 48 |    |    | 100 |    |
# | 80 |    |    |    | 35 |    |    |    |  15 |    |
# |    | 84 | 31 |    |    | 24 |    |    |  96 |    |
# | 86 | 85 |    | 27 | 92 |    |    |    |     | 18 |
# |    |    | 90 |    |    |    |    |    |     |    |


# Cette partie du programme lance le solveur SAT avec la conjonction des contraintes,
# c'est-à-dire la concaténation des listes les représentant.
with Minisat22(bootstrap_with=psi) as m:
    # si on trouve une solution
    if m.solve():
        model = [decode(v) for v in m.get_model() if v >0] # on récupère les
                                                           # variables qui sont
                                                           # vraies dans la solution
                                                           # trouvée
        # On affiche le résultat lisiblement
        r = [[0 for i in coord] for j in coord]
        for (i,j,k) in model:
            r[i][j] += k+1
        print("\n")
        for ligne in r:
            l = ""
            for nb in ligne:
                if nb < 10:
                    l += "| " +str(nb)
                else:
                    l += "|" +str(nb)
            l+="|"
            print(l)
    else:
        print("pas de solution")

