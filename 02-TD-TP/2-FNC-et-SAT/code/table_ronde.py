from pysat.solvers import Minisat22



chevaliers = ["Arthur", "Bédivère", "Bohort", "Caradoc Freichfras", "Claudin", "Cligès", "Érec", "Galaad", "Gareth", "Gauvain", "Girflet", "Hector des Mares", "Keu", "Gliglois", "Lancelot du Lac", "Léodagan", "Lionel", "Mordred","Perceval le Gallois", "Tristan","Yvain"]

# Notez que (a,b) est dans la liste 'rivalités' ssi (b,a) y est également

rivalités = [('Arthur', 'Bédivère'), ('Bédivère', 'Arthur'), ('Arthur', 'Bohort'), ('Bohort', 'Arthur'), ('Arthur', 'Cligès'), ('Cligès', 'Arthur'), ('Arthur', 'Gauvain'), ('Gauvain', 'Arthur'), ('Arthur', 'Girflet'), ('Girflet', 'Arthur'), ('Arthur', 'Keu'), ('Keu', 'Arthur'), ('Arthur', 'Gliglois'), ('Gliglois', 'Arthur'), ('Bédivère', 'Bohort'), ('Bohort', 'Bédivère'), ('Bédivère', 'Caradoc Freichfras'), ('Caradoc Freichfras', 'Bédivère'), ('Bédivère', 'Claudin'), ('Claudin', 'Bédivère'), ('Bédivère', 'Cligès'), ('Cligès', 'Bédivère'), ('Bédivère', 'Érec'), ('Érec', 'Bédivère'), ('Bédivère', 'Hector des Mares'), ('Hector des Mares', 'Bédivère'), ('Bédivère', 'Gliglois'), ('Gliglois', 'Bédivère'), ('Bédivère', 'Lancelot du Lac'), ('Lancelot du Lac', 'Bédivère'), ('Bédivère', 'Léodagan'), ('Léodagan', 'Bédivère'), ('Bohort', 'Caradoc Freichfras'), ('Caradoc Freichfras', 'Bohort'), ('Bohort', 'Claudin'), ('Claudin', 'Bohort'), ('Bohort', 'Gareth'), ('Gareth', 'Bohort'), ('Bohort', 'Gauvain'), ('Gauvain', 'Bohort'), ('Bohort', 'Lancelot du Lac'), ('Lancelot du Lac', 'Bohort'), ('Bohort', 'Lionel'), ('Lionel', 'Bohort'), ('Bohort', 'Perceval le Gallois'), ('Perceval le Gallois', 'Bohort'), ('Caradoc Freichfras', 'Érec'), ('Érec', 'Caradoc Freichfras'), ('Caradoc Freichfras', 'Gareth'), ('Gareth', 'Caradoc Freichfras'), ('Caradoc Freichfras', 'Gauvain'), ('Gauvain', 'Caradoc Freichfras'), ('Caradoc Freichfras', 'Girflet'), ('Girflet', 'Caradoc Freichfras'), ('Caradoc Freichfras', 'Gliglois'), ('Gliglois', 'Caradoc Freichfras'), ('Caradoc Freichfras', 'Léodagan'), ('Léodagan', 'Caradoc Freichfras'), ('Caradoc Freichfras', 'Lionel'), ('Lionel', 'Caradoc Freichfras'), ('Caradoc Freichfras', 'Perceval le Gallois'), ('Perceval le Gallois', 'Caradoc Freichfras'), ('Claudin', 'Érec'), ('Érec', 'Claudin'), ('Claudin', 'Galaad'), ('Galaad', 'Claudin'), ('Claudin', 'Gauvain'), ('Gauvain', 'Claudin'), ('Claudin', 'Hector des Mares'), ('Hector des Mares', 'Claudin'), ('Claudin', 'Keu'), ('Keu', 'Claudin'), ('Claudin', 'Gliglois'), ('Gliglois', 'Claudin'), ('Claudin', 'Mordred'), ('Mordred', 'Claudin'), ('Claudin', 'Tristan'), ('Tristan', 'Claudin'), ('Cligès', 'Galaad'), ('Galaad', 'Cligès'), ('Cligès', 'Girflet'), ('Girflet', 'Cligès'), ('Cligès', 'Hector des Mares'), ('Hector des Mares', 'Cligès'), ('Cligès', 'Keu'), ('Keu', 'Cligès'), ('Cligès', 'Gliglois'), ('Gliglois', 'Cligès'), ('Cligès', 'Lionel'), ('Lionel', 'Cligès'), ('Cligès', 'Tristan'), ('Tristan', 'Cligès'), ('Érec', 'Galaad'), ('Galaad', 'Érec'), ('Érec', 'Gauvain'), ('Gauvain', 'Érec'), ('Érec', 'Girflet'), ('Girflet', 'Érec'), ('Érec', 'Keu'), ('Keu', 'Érec'), ('Érec', 'Léodagan'), ('Léodagan', 'Érec'), ('Érec', 'Lionel'), ('Lionel', 'Érec'), ('Érec', 'Perceval le Gallois'), ('Perceval le Gallois', 'Érec'), ('Galaad', 'Gareth'), ('Gareth', 'Galaad'), ('Galaad', 'Hector des Mares'), ('Hector des Mares', 'Galaad'), ('Galaad', 'Keu'), ('Keu', 'Galaad'), ('Galaad', 'Mordred'), ('Mordred', 'Galaad'), ('Gareth', 'Gauvain'), ('Gauvain', 'Gareth'), ('Gareth', 'Girflet'), ('Girflet', 'Gareth'), ('Gareth', 'Hector des Mares'), ('Hector des Mares', 'Gareth'), ('Gareth', 'Keu'), ('Keu', 'Gareth'), ('Gareth', 'Léodagan'), ('Léodagan', 'Gareth'), ('Gareth', 'Lionel'), ('Lionel', 'Gareth'), ('Gareth', 'Mordred'), ('Mordred', 'Gareth'), ('Gareth', 'Tristan'), ('Tristan', 'Gareth'), ('Gauvain', 'Girflet'), ('Girflet', 'Gauvain'), ('Gauvain', 'Keu'), ('Keu', 'Gauvain'), ('Gauvain', 'Gliglois'), ('Gliglois', 'Gauvain'), ('Gauvain', 'Lancelot du Lac'), ('Lancelot du Lac', 'Gauvain'), ('Gauvain', 'Perceval le Gallois'), ('Perceval le Gallois', 'Gauvain'), ('Girflet', 'Lancelot du Lac'), ('Lancelot du Lac', 'Girflet'), ('Girflet', 'Léodagan'), ('Léodagan', 'Girflet'), ('Girflet', 'Mordred'), ('Mordred', 'Girflet'), ('Girflet', 'Tristan'), ('Tristan', 'Girflet'), ('Hector des Mares', 'Keu'), ('Keu', 'Hector des Mares'), ('Hector des Mares', 'Léodagan'), ('Léodagan', 'Hector des Mares'), ('Hector des Mares', 'Mordred'), ('Mordred', 'Hector des Mares'), ('Hector des Mares', 'Perceval le Gallois'), ('Perceval le Gallois', 'Hector des Mares'), ('Hector des Mares', 'Tristan'), ('Tristan', 'Hector des Mares'), ('Keu', 'Perceval le Gallois'), ('Perceval le Gallois', 'Keu'), ('Keu', 'Tristan'), ('Tristan', 'Keu'), ('Gliglois', 'Léodagan'), ('Léodagan', 'Gliglois'), ('Lancelot du Lac', 'Léodagan'), ('Léodagan', 'Lancelot du Lac'), ('Lancelot du Lac', 'Lionel'), ('Lionel', 'Lancelot du Lac'), ('Lancelot du Lac', 'Perceval le Gallois'), ('Perceval le Gallois', 'Lancelot du Lac'), ('Léodagan', 'Perceval le Gallois'), ('Perceval le Gallois', 'Léodagan'), ('Lionel', 'Tristan'), ('Tristan', 'Lionel')]

# Définition des variables, x_{c,i} où c est un chevalier et i est un numéro de
# siège.

nb_chevaliers = len(chevaliers)

sieges = range(nb_chevaliers)

variables = [(c,i) for c in chevaliers for i in sieges]

def encode(c,i):
    j= chevaliers.index(c)
    return 1 + j + i*nb_chevaliers

def decode(n):
    m=n-1
    return (chevaliers[m % nb_chevaliers], m// nb_chevaliers)

# Chaque chevalier doit occuper au moins un siege
phi1 = []

# Chaque chevalier occupe au plus un siege
phi2 = []

# Chaque siege est occupé par au moins un chevalier
phi3 = []

# Chaque siege est occupé par au plus un chevalier

phi4 = []

# Les voisins de chaque chevalier ne sont pas ses rivaux

phi5 = []

# À partir de formules SAT précédentes, construire un problème SAT psi qui représente le problème à résoudre (conjonction des contraintes,c'est-à-dire la concaténation des listes les représentant)
psi = []

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
        for (chevalier, siege) in model:
            print(chevalier, "->", siege+1)
    else:
        print("pas de solution")
