# TD 2 : FNC et SAT — énoncé fourni

> 📄 **Énoncé officiel** distribué en TD (Logique — Licence Informatique / Double Licence — 2026-2027).
> ✅ Correction : [TD2-correction.md](TD2-correction.md) · 📝 Mon travail : [mes-reponses-TD2.md](mes-reponses-TD2.md)
> 📚 Cours : [Ch. 4 Formes normales](../../01-Cours/01-Logique-propositionnelle/4-Formes-normales.md) · [Ch. 6 Modéliser avec SAT](../../01-Cours/02-SAT/6-Modeliser-avec-SAT.md) · [Ch. 7 SAT en Python](../../01-Cours/02-SAT/7-SAT-en-Python.md)

> ⚠️ Les feuilles de TD sont volontairement longues. Les exercices non faits en classe sont à faire pour préparer l'examen.

---

## Exercice 1 : Mise sous forme normale disjonctive

Mettre sous **FND** les formules suivantes :

- **Q 1.1** `((p ∨ q) ⇒ (r ∧ ¬s)) ∨ (t ∧ ¬u)`
- **Q 1.2** `((p ∨ ¬q) ∧ (r ∨ s)) ⇒ (t ∨ ¬u)`
- **Q 1.3** `¬((p ∨ ¬q) ∨ (r ⇒ s)) ∨ (q ⇔ t)`
- **Q 1.4** `¬((p ∨ q) ⇔ (r ∨ s)) ∨ ((t ∧ u) ⇒ (¬v ∨ w))`

## Exercice 2 : Mise sous forme normale conjonctive

Mettre sous **FNC** les formules suivantes :

- **Q 2.1** `¬(p ∧ (q ⇒ p))`
- **Q 2.2** `((p ∨ q) ⇒ r) ∨ ((p ⇒ r) ∧ (q ⇒ r))`
- **Q 2.3** `(p ∨ (q ⇒ r)) ⇒ ((p ∨ q) ⇒ r)`
- **Q 2.4** `((p ∨ q) ⇒ (r ∧ ¬s)) ∨ (t ∧ ¬u)`

---

## Exercice 3 : SAT — Organiser une fête

Nous savons que :

- Alice ne vient **que si** Bob vient aussi ;
- Charles et Diana ne peuvent pas être **tous les deux** présents ;
- **Si** Élise vient, Charles doit venir aussi ;
- **Au moins une** personne doit participer.

Définir les variables, transformer les règles en clauses SAT.
Dans quel cas existe-t-il une combinaison valide ? Donner une liste valide de participants.
Si on est sûr que Charles **et** Diana participent, qu'est-ce que cela change ?

---

## Exercice 4 : SAT — Problème des tours

Sur un échiquier `n × n`, placer `n` tours sans qu'aucune n'en attaque une autre (même ligne ou même colonne = attaque). Lignes et colonnes numérotées de 1 à `n`.

**Figure 1** — exemple de solution pour `n = 4` :

| | 1 | 2 | 3 | 4 |
|:-:|:-:|:-:|:-:|:-:|
| **1** | ♜ | | | |
| **2** | | | ♜ | |
| **3** | | ♜ | | |
| **4** | | | | ♜ |

- **Q 4.1** Donner la valuation des variables pour la solution de la Figure 1.
- **Q 4.2** Exprimer la contrainte : chaque **ligne** comporte **exactement une** tour.
- **Q 4.3** Exprimer la contrainte : chaque **colonne** comporte **exactement une** tour.

> **NB** : dans tous les exercices suivants, chaque contrainte doit être donnée **sous FNC**.
> Une fois un exercice terminé, l'implémenter en Python avec le fichier correspondant du portail pédagogique (voir [l'installation de python-sat](../../01-Cours/02-SAT/7-SAT-en-Python.md)). Les fichiers Python vont dans le dossier `code/`.

---

## Exercice 5 : Les chevaliers de la table ronde

Le roi Arthur veut placer les chevaliers autour de la table ronde sans que deux **rivaux** soient côte à côte.
`C` = ensemble des chevaliers, `R` = ensemble des paires de rivaux (rivalité **symétrique**).
Il y a `n` chevaliers et `n` places numérotées de 1 à `n`.

- **Q 5.1** Identifier les variables.
- **Q 5.2** Chaque chevalier occupe **au moins** un siège.
- **Q 5.3** Un chevalier occupe **au plus** un siège.
- **Q 5.4** Chaque place est occupée par **au moins** un chevalier.
- **Q 5.5** Deux chevaliers ne peuvent pas occuper la **même** place.
- **Q 5.6** La contrainte précédente est-elle nécessaire ? Pourquoi ?
- **Q 5.7** Deux rivaux ne sont pas assis **côte à côte**. Attention : les places `1` et `n` sont voisines.

Fichier Python : `table_ronde.py`

---

## Exercice 6 : Sudoku

Remplir chaque case avec un entier de 1 à 9 ; chaque entier apparaît **exactement une fois** par ligne, par colonne et par carré 3×3.

Variables : `x_{i,j,k}` avec `i, j, k ∈ [1, 9]`, vraie ssi **la case `(i, j)` contient `k`**.
Dans le code : `encode(i, j, k)`.
(Convention de l'énoncé pour les coordonnées : à vérifier dans `sudoku.py`.)

**Grille d'exemple** :

| | | | | | | | | |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| · | · | · | · | 2 | · | · | 1 | 7 |
| · | 3 | · | · | · | 7 | · | · | 8 |
| · | · | · | · | 9 | · | 6 | · | · |
| · | 8 | · | 9 | · | 2 | · | 6 | · |
| 4 | · | 6 | · | · | · | 3 | · | 2 |
| · | 2 | · | 6 | · | 3 | · | 7 | · |
| · | · | 7 | · | 6 | · | · | · | · |
| 8 | · | · | 7 | · | · | · | 5 | · |
| 2 | 5 | · | · | 3 | · | · | · | · |

- **Q 6.1** Chaque case contient **exactement un** chiffre → `phi1`, `phi2` dans `sudoku.py`.
- **Q 6.2** Chaque **ligne** et chaque **colonne** contient exactement une fois chaque chiffre → `phi3`, `phi4`.
- **Q 6.3** Contrainte des **carrés** → `phi5` (on peut définir `carre(i1, i2, j1, j2)`).
- **Q 6.4** Contrainte qui représente la **grille d'exemple** → `phi6`.
- **Q 6.5** Trouver une grille réputée extrêmement difficile et vérifier si le solveur la résout.

---

## Exercice 7 : Hidoku

Remplir une grille carrée de côté `n` avec les nombres de `1` à `n²` :

- chaque case contient un nombre entre 1 et `n²` ;
- chaque nombre apparaît **une et une seule fois** ;
- si `k` (avec `0 < k < n²`) est dans une case, `k + 1` est dans une case **voisine** (côté ou coin : 8 voisins possibles).

**Grille d'exemple (n = 7)** :

| | | | | | | |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| · | · | · | 45 | · | · | · |
| **49** | · | · | · | · | · | 37 |
| 30 | · | · | · | · | · | 12 |
| · | · | · | 16 | · | · | · |
| 19 | · | · | · | · | · | 40 |
| **1** | · | · | · | · | · | 7 |
| · | · | · | 4 | · | · | · |

**Solution** :

| | | | | | | |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| 48 | 47 | 46 | 45 | 34 | 35 | 36 |
| 49 | 31 | 44 | 33 | 14 | 13 | 37 |
| 30 | 28 | 32 | 43 | 15 | 38 | 12 |
| 29 | 18 | 27 | 16 | 42 | 11 | 39 |
| 19 | 2 | 17 | 26 | 10 | 41 | 40 |
| 1 | 20 | 3 | 24 | 25 | 9 | 7 |
| 21 | 22 | 23 | 4 | 5 | 6 | 8 |

On modélise le problème avec SAT pour une grille de côté `n ≥ 1` (formules **en FNC**).

- **Q 7.1** Quelles variables ? Préciser leur signification.
- **Q 7.2** Chaque case contient **au moins** un nombre entre 1 et `n²`.
- **Q 7.3** Chaque case contient **au plus** un nombre.
- **Q 7.4** Chaque nombre apparaît **au moins** une fois.
- **Q 7.5** Chaque nombre apparaît **au plus** une fois.
- **Q 7.6** On peut se passer de l'une des contraintes Q 7.4 / Q 7.5. Pourquoi ?
- **Q 7.7** Contrainte entre les cases de `k` et `k + 1`. Décomposer selon que la case de `k` est :
  1. un **coin** ;
  2. sur un **bord** (pas un coin) ;
  3. **ni coin ni bord**.
- **Q 7.8** Quelle contrainte ajouter pour une grille particulière ? Donner celle de la grille d'exemple.
