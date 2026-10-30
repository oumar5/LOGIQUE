# Partie 4 — Logique du premier ordre : énoncés proposés

> Exercices **que je t'ai préparés** sur les chapitres 15 à 17 (le TD officiel n'a pas encore eu lieu ; quand tu l'auras, ajoute-le dans ce dossier sous le nom `TDx-enonce-fourni.md`).
> ✅ La correction est dans un fichier à part : [corrections-proposes.md](corrections-proposes.md).
>
> Cours : [Ch. 15 Syntaxe](../../01-Cours/04-Logique-premier-ordre/15-Syntaxe-premier-ordre.md) · [Ch. 16 Sémantique](../../01-Cours/04-Logique-premier-ordre/16-Semantique-premier-ordre.md) · [Ch. 17 Modéliser](../../01-Cours/04-Logique-premier-ordre/17-Modeliser-premier-ordre.md)

---

## Partie A — Écrire des formules

### A1. Fonction ou prédicat ? ⭐

Pour chaque symbole, dis s'il vaut mieux en faire une **fonction** (qui donne un objet) ou un **prédicat** (vrai/faux), et donne son arité :

1. `age(x)` : l'âge de `x`
2. `EstMajeur(x)` : `x` a 18 ans ou plus
3. `mere(x)` : la mère de `x`
4. `Aime(x, y)` : `x` aime `y`
5. `capitale(p)` : la capitale du pays `p`

### A2. Variables libres et liées ⭐⭐

Donne les variables libres de chaque formule, et dis si elle est close :

1. `∀x (P(x) ⇒ Q(x, y))`
2. `(∃x P(x)) ∧ Q(x)`
3. `∀x ∃y R(x, y)`
4. `∃y (R(x, y) ∧ ∀x P(x))`

### A3. Arbre ⭐

Dessine l'arbre de `∀x (Chat(x) ⇒ ∃y (Souris(y) ∧ Chasse(x, y)))` et traduis la formule en français.

---

## Partie B — Vrai ou faux dans une structure

On prend la structure suivante :

- domaine `D = {1, 2, 3}` ;
- `Pair(x)` est vrai seulement pour `x = 2` ;
- `Inf(x, y)` est vrai quand `x < y`.

### B1. Évaluer ⭐⭐

Dis si chaque formule est vraie ou fausse dans cette structure, et justifie :

1. `∃x Pair(x)`
2. `∀x Pair(x)`
3. `∀x ∃y Inf(x, y)`
4. `∃x ∀y (x ≠ y ⇒ Inf(x, y))`
5. `∀x (Pair(x) ⇒ ∃y Inf(y, x))`

### B2. Nier ⭐

Écris la négation (en formule puis en français) en faisant « traverser » la négation :

1. « Tous les étudiants ont réussi » : `∀x (Etudiant(x) ⇒ Reussi(x))`
2. « Il existe un cours que personne n'a validé » : `∃c ∀x ¬Valide(x, c)`

### B3. L'ordre des quantificateurs ⭐⭐

Avec `Mere(x, y)` = « `x` est la mère de `y` », traduis en français, puis dis laquelle est vraie dans le monde réel :

1. `∀y ∃x Mere(x, y)`
2. `∃x ∀y Mere(x, y)`

### B4. Contre-exemple ⭐⭐⭐

Montre avec une petite structure que `∀x (P(x) ∨ Q(x))` et `(∀x P(x)) ∨ (∀x Q(x))` ne sont **pas** équivalentes.

---

## Partie C — Modéliser

Vocabulaire : `Etudiant(x)`, `Prof(x)`, `Cours(c)`, `Inscrit(x, c)`, `Valide(x, c)`, `EnRetard(x)`, `Passe(x)` (« `x` passe l'examen »), `Parent(x, y)`, `Homme(x)`, et l'égalité `=`.

### C1. Les motifs de base ⭐

1. « Tous les profs sont en retard. »
2. « Certains étudiants sont en retard. »
3. « Aucun prof n'est en retard. »
4. « Seuls les étudiants inscrits à au moins un cours passent l'examen. »

### C2. Trouver l'erreur ⭐⭐

Un étudiant a traduit « Il existe un étudiant en retard » par `∃x (Etudiant(x) ⇒ EnRetard(x))`. Pourquoi est-ce faux ? Donne un exemple de situation où sa formule est vraie alors que la phrase est fausse.

### C3. Plusieurs quantificateurs ⭐⭐

1. « Chaque cours a au moins un étudiant inscrit. »
2. « Un étudiant est inscrit à tous les cours. »
3. « Personne ne valide un cours sans y être inscrit. »

### C4. Compter ⭐⭐⭐

1. « Chaque cours a au moins deux étudiants inscrits. »
2. « Chacun a exactement une mère » (avec `Mere(x, y)`).

### C5. La famille ⭐⭐⭐

Définis par une formule (avec `x` et `z` libres) : « `x` est un **oncle** de `z` », c'est-à-dire un homme, frère d'un parent de `z` (on considère que deux personnes distinctes ayant un parent commun sont frère/sœur).
