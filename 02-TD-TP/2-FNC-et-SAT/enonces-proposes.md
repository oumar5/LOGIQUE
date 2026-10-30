# Partie 2 — FNC et SAT : énoncés proposés

> Exercices **que je t'ai préparés** en plus du TD2, sur les chapitres 5 à 10. Ils vont du plus simple au plus difficile.
> ✅ La correction est dans un fichier à part : [corrections-proposes.md](corrections-proposes.md).
>
> Cours : [Ch. 5 SAT](../../01-Cours/02-SAT/5-Probleme-SAT.md) · [Ch. 6 Modéliser](../../01-Cours/02-SAT/6-Modeliser-avec-SAT.md) · [Ch. 7 Python](../../01-Cours/02-SAT/7-SAT-en-Python.md) · [Ch. 8 Tseitin](../../01-Cours/02-SAT/8-Tseitin.md) · [Ch. 9 DPLL](../../01-Cours/02-SAT/9-DPLL.md) · [Ch. 10 Opérateurs](../../01-Cours/02-SAT/10-Operateurs-en-programmation.md)

---

## Partie A — Modéliser avec SAT

### A1. Les motifs ⭐

Écris en clauses (FNC) :

1. « Si `a`, alors `b` ou `c`. »
2. « `a` si et seulement si `b`. »
3. « Au plus un parmi `a`, `b`, `c`. »
4. « **Au moins deux** parmi `a`, `b`, `c`. »
5. Combien de clauses faut-il pour « au plus un » parmi 10 variables ?

### A2. Les tâches de la colocation ⭐⭐

Ana, Ben et Clara se partagent 3 tâches : vaisselle, courses, ménage.

- chaque tâche est faite par **exactement une** personne ;
- chaque personne fait **au moins une** tâche ;
- Ben ne fait **pas** la vaisselle ;
- si Ana fait le ménage, alors Clara fait la vaisselle.

1. Choisis les variables (avec leur phrase « … vraie ssi … »).
2. Écris toutes les clauses.
3. Donne une répartition qui marche.

### A3. Le planning des examens ⭐⭐

Quatre examens : Logique (L), Algo (A), Archi (R), Anglais (E). Deux créneaux : matin (1) et après-midi (2).
Certains examens ont des étudiants en commun et **ne peuvent pas** être au même créneau : L–A, A–R, L–E.

1. Choisis les variables et écris les clauses.
2. Trouve un planning.
3. On ajoute le conflit L–R. Existe-t-il encore un planning ? Pourquoi ?

### A4. Trop de pigeons ⭐⭐

3 pigeons, 2 nids : chaque pigeon a un nid, chaque nid a au plus un pigeon.

1. Écris toutes les clauses (sans la règle « un pigeon a au plus un nid »).
2. Explique pourquoi c'est insatisfiable.

---

## Partie B — Python et DIMACS

### B1. Format DIMACS ⭐

Écris `(x₁ ∨ ¬x₂) ∧ (x₂ ∨ x₃) ∧ ¬x₁` au format DIMACS, puis trouve une solution à la main.

### B2. Lire la réponse du solveur ⭐

On encode 2 pigeons et 2 nids par `p₁,₁ → 1`, `p₁,₂ → 2`, `p₂,₁ → 3`, `p₂,₂ → 4`.
Le solveur répond `SAT 1 -2 -3 4`. Où est chaque pigeon ?

### B3. Du code vers la formule ⭐⭐

Quelle formule (et quelle phrase en français) correspond à ce code ?

```python
[[-encode(i, j), -encode(i, k)] for i in L for j in C for k in C if j < k]
```

### B4. De la formule vers le code ⭐⭐

Écris en Python les clauses de l'exercice A3 (examens), avec `examens = ["L", "A", "R", "E"]`, `creneaux = [1, 2]` et `conflits = [("L", "A"), ("A", "R"), ("L", "E")]`.

---

## Partie C — Tseitin

### C1. Une petite formule ⭐

Applique Tseitin à `¬a ∨ b` (nomme `y` le nœud `¬a` et `x` la racine).

### C2. Avec une implication ⭐⭐

Applique Tseitin à `(a ∧ b) ⇒ c` (nomme `y` le nœud `a ∧ b` et `x` la racine).

### C3. Retrouver le catalogue ⭐⭐

Retrouve les clauses de `x ⇔ (x₁ ∨ x₂)` en coupant le `⇔` en deux implications.

### C4. Compter ⭐

Une formule contient 10 connecteurs binaires et 5 négations. Au maximum, combien de clauses donne Tseitin ?

---

## Partie D — DPLL

Pour chaque exercice : présente un tableau (étape, règle, choix, résultat) et dessine l'arbre de recherche.

### D1. ⭐

`(a ∨ b) ∧ (¬a ∨ c) ∧ ¬c ∧ (b ∨ d)`

### D2. ⭐⭐

`(a ∨ b) ∧ (¬a ∨ b) ∧ (a ∨ ¬b) ∧ (¬a ∨ ¬b)`

### D3. ⭐⭐⭐

`(p ∨ q ∨ r) ∧ (¬p ∨ q) ∧ (¬q ∨ r) ∧ (¬r ∨ ¬p) ∧ (s ∨ ¬t)`

---

## Partie E — Les opérateurs dans les programmes

### E1. ⭐

Que valent `⊥⊥ || 1`, `1 || ⊥⊥`, `0 && ⊥⊥` et `⊥⊥ && 0` avec les opérateurs séquentiels à gauche ?

### E2. ⭐

Pourquoi `x != 0 and 10 / x > 1` ne plante jamais, alors que `10 / x > 1 and x != 0` plante quand `x = 0` ?

### E3. ⭐⭐

Ce code plante parfois. Pourquoi ? Corrige-le.

```python
def commence_par_5(liste):
    return liste[0] == 5 and len(liste) > 0
```
