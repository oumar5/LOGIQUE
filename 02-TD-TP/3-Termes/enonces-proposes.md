# Partie 3 — Termes : énoncés proposés

> Exercices **que je t'ai préparés** sur les chapitres 11 à 14 (le TD officiel n'a pas encore eu lieu ; quand tu l'auras, ajoute-le dans ce dossier sous le nom `TDx-enonce-fourni.md`).
> ✅ La correction est dans un fichier à part : [corrections-proposes.md](corrections-proposes.md).
>
> Cours : [Ch. 11 Termes](../../01-Cours/03-Termes/11-Termes.md) · [Ch. 12 F-algèbres](../../01-Cours/03-Termes/12-Semantique-F-algebres.md) · [Ch. 13 Substitution](../../01-Cours/03-Termes/13-Substitution.md) · [Ch. 14 Unification](../../01-Cours/03-Termes/14-Unification.md)

Sauf mention contraire, la signature est `F = { zero/0, succ/1, plus/2 }`, et `a`, `b`, `c` désignent des constantes.

---

## Partie A — Écrire des termes

### A1. Terme ou pas ? ⭐

Lesquelles de ces expressions sont des termes sur `F` ? Justifie.

1. `plus(zero)`
2. `succ(succ(x))`
3. `plus(x, y, z)`
4. `succ`
5. `x`

### A2. Arbre et mesures ⭐

Pour `t = plus(succ(x), plus(y, x))` : dessine l'arbre, puis donne `Var(t)`, la taille et la hauteur. Est-il clos ?

### A3. Les listes ⭐

Avec la signature `{ nil/0, cons/2, a/0, b/0 }` (`cons(e, l)` ajoute `e` en tête de la liste `l`) :

1. Écris le terme qui représente la liste `[a, b, a]`.
2. Dessine son arbre.

### A4. Une fonction récursive ⭐⭐

Définis cas par cas la fonction `long(l)` qui donne la longueur d'une liste écrite avec `nil` et `cons`. Calcule `long(cons(a, cons(b, nil)))`.

---

## Partie B — Donner un sens aux termes

### B1. Deux algèbres ⭐

Calcule la valeur de `plus(succ(x), succ(succ(zero)))` :

1. dans l'algèbre ℕ avec `x = 3` ;
2. dans l'algèbre Parité avec `x = impair`.

Les deux résultats sont-ils cohérents ?

### B2. Une algèbre qui compte ⭐⭐

Sur la signature des listes `{ nil/0, cons/2, a/0, b/0 }`, on prend le domaine `ℕ` et :
`nil = 0`, `cons(e, l) = 1 + l`, `a = 7`, `b = 42`.

Que vaut `cons(a, cons(b, nil))` dans cette algèbre ? Que calcule cette algèbre en général ?

### B3. Pas commutatif ⭐⭐

Trouve une algèbre (sur la signature `F`) et des valeurs de `x` et `y` telles que `plus(x, y)` et `plus(y, x)` n'ont **pas** la même valeur.

### B4. Les booléens sont une algèbre ⭐⭐

Signature `{ vrai/0, faux/0, non/1, et/2 }`, domaine `{0, 1}`, avec le sens habituel. Que vaut `et(non(x), vrai)` pour `x = 0` ? Pour `x = 1` ? Quel lien avec le chapitre 2 ?

---

## Partie C — Substitution

### C1. Appliquer ⭐

Calcule `tσ` pour `t = f(x, g(y, x))` et `σ = { x ↦ a, y ↦ h(x) }`.

### C2. Instance ou pas ? ⭐

1. `f(g(a), b)` est-il une instance de `f(x, y)` ? Si oui, avec quelle substitution ?
2. `f(g(a), b)` est-il une instance de `f(x, x)` ?
3. `f(a, a)` est-il une instance de `f(x, x)` ?

### C3. Composer ⭐⭐

`σ = { x ↦ g(y) }` et `τ = { y ↦ b, x ↦ c }`.

1. Calcule `στ` (d'abord `σ`, puis `τ`).
2. Vérifie ton résultat sur `t = h(x, y)`.
3. Calcule `τσ`. Est-ce la même chose ?

---

## Partie D — Unification

Pour chaque paire, applique l'algorithme (en nommant les règles) : donne le mgu, ou explique pourquoi l'unification échoue.

### D1. ⭐

`f(x, b)` et `f(a, y)`

### D2. ⭐

`g(x, h(x))` et `g(a, h(y))`

### D3. ⭐⭐

`f(x, x)` et `f(a, b)`

### D4. ⭐⭐

`f(x, g(x))` et `f(g(y), y)`

### D5. Les types en programmation ⭐⭐

Une fonction attend un argument de type `paire(int, liste(α))`. On lui donne une valeur de type `paire(β, liste(bool))`. `α` et `β` sont des variables de type. Quels types le compilateur va-t-il déduire pour `α` et `β` ?

### D6. Comme en Prolog ⭐⭐

On connaît le fait `pere(ahmed, habiba)`. On pose la question `pere(X, habiba)` : quelle réponse ? Et pour la question `pere(X, sara)` ?
