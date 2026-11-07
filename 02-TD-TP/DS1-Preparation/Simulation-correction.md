# Simulation d'examen — correction

> Correction de [Simulation-enonce-fourni.md](Simulation-enonce-fourni.md), rédigée pour réviser et **vérifiée par calcul** sur toutes les valuations.
> Corrige-toi **après** avoir fait le sujet en 2 h, sans aide.

---

## Exercice 1 : Tables de vérité

### Q 1.1 `¬(P ∧ Q) ∨ ((R → (P ∨ ¬Q)) ∧ ((¬R ∨ Q) ↔ (P → ¬Q)))`

Notations : `X = R → (P ∨ ¬Q)`, `Y = ¬R ∨ Q`, `Z = P → ¬Q`.

| P | Q | R | ¬(P ∧ Q) | X | Y | Z | Y ↔ Z | X ∧ (Y ↔ Z) | **résultat** |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| 0 | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | **1** |
| 0 | 0 | 1 | 1 | 1 | 0 | 1 | 0 | 0 | **1** |
| 0 | 1 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | **1** |
| 0 | 1 | 1 | 1 | 0 | 1 | 1 | 1 | 0 | **1** |
| 1 | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | **1** |
| 1 | 0 | 1 | 1 | 1 | 0 | 1 | 0 | 0 | **1** |
| 1 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | **0** |
| 1 | 1 | 1 | 0 | 1 | 1 | 0 | 0 | 0 | **0** |

> ⏱️ **Gain de temps** : c'est un `∨`. Dès que `¬(P ∧ Q) = 1` (6 lignes sur 8), le résultat vaut 1 sans calculer la droite. Il ne reste que les 2 lignes `P = Q = 1` à calculer. Le résultat est équivalent à `¬(P ∧ Q)`.

### Q 1.2 `((A ∧ ¬B) ∨ (¬C ∧ D)) ∧ ((¬A ∨ C) ∨ (B ∧ ¬D))`

Notations : `G = (A ∧ ¬B) ∨ (¬C ∧ D)` et `H = (¬A ∨ C) ∨ (B ∧ ¬D)`.

| A | B | C | D | A ∧ ¬B | ¬C ∧ D | **G** | ¬A ∨ C | B ∧ ¬D | **H** | **G ∧ H** |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | **0** |
| 0 | 0 | 0 | 1 | 0 | 1 | 1 | 1 | 0 | 1 | **1** |
| 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | **0** |
| 0 | 0 | 1 | 1 | 0 | 0 | 0 | 1 | 0 | 1 | **0** |
| 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | **0** |
| 0 | 1 | 0 | 1 | 0 | 1 | 1 | 1 | 0 | 1 | **1** |
| 0 | 1 | 1 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | **0** |
| 0 | 1 | 1 | 1 | 0 | 0 | 0 | 1 | 0 | 1 | **0** |
| 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | **0** |
| 1 | 0 | 0 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | **0** |
| 1 | 0 | 1 | 0 | 1 | 0 | 1 | 1 | 0 | 1 | **1** |
| 1 | 0 | 1 | 1 | 1 | 0 | 1 | 1 | 0 | 1 | **1** |
| 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | **0** |
| 1 | 1 | 0 | 1 | 0 | 1 | 1 | 0 | 0 | 0 | **0** |
| 1 | 1 | 1 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | **0** |
| 1 | 1 | 1 | 1 | 0 | 0 | 0 | 1 | 0 | 1 | **0** |

La formule est vraie pour exactement 4 valuations : `0001`, `0101`, `1010`, `1011`.

> ⏱️ **Gain de temps** : c'est un `∧`. Calcule d'abord `G` ; là où `G = 0` (10 lignes), le résultat est 0 sans calculer `H`.

---

## Exercice 2 : Mario

**Variables**

| Variable | Vraie ssi |
|---|---|
| `a` | Mario est architecte |
| `g` | Mario est géomètre |
| `d` | Mario est titulaire d'un diplôme universitaire |

**Formules**

1. `a ∨ g`
2. `a ⇒ d`
3. `¬d`

**Tout le monde peut-il dire vrai ?** On cherche une valuation qui rend vraies les trois formules :

- (3) donne `d = 0` ;
- (2) `a ⇒ d` avec `d = 0` impose `a = 0` (sinon `1 ⇒ 0 = 0`) ;
- (1) `a ∨ g` avec `a = 0` impose `g = 1`.

Vérification : `a ∨ g = 1` ✅, `a ⇒ d = 0 ⇒ 0 = 1` ✅, `¬d = 1` ✅.

**Oui, c'est possible, et dans ce cas Mario est géomètre** (et pas architecte). C'est la seule valuation qui satisfait les trois phrases.

---

## Exercice 3 : Les `n` reines

### Q 3.1 Valuation

`x_{1,4} = x_{2,2} = x_{3,5} = x_{4,3} = x_{5,1} = 1`, et les 20 autres variables valent 0.

### Q 3.2 Exactement une reine par ligne

- au moins une : `⋀_{i=1}^{n} ⋁_{j=1}^{n} x_{i,j}`
- au plus une : `⋀_{i=1}^{n} ⋀_{1≤j<k≤n} (¬x_{i,j} ∨ ¬x_{i,k})`

### Q 3.3 Exactement une reine par colonne

- au moins une : `⋀_{j=1}^{n} ⋁_{i=1}^{n} x_{i,j}`
- au plus une : `⋀_{j=1}^{n} ⋀_{1≤i<k≤n} (¬x_{i,j} ∨ ¬x_{k,j})`

### Q 3.4 Au plus une reine par diagonale

Deux cases différentes `(i, j)` et `(k, l)` sont sur la même diagonale :

- **décroissante** si `i − j = k − l` ;
- **croissante** si `i + j = k + l`.

```
⋀_{(i,j)≠(k,l), i−j=k−l} (¬x_{i,j} ∨ ¬x_{k,l})   ∧   ⋀_{(i,j)≠(k,l), i+j=k+l} (¬x_{i,j} ∨ ¬x_{k,l})
```

(on peut se limiter aux paires avec `i < k` pour ne pas écrire chaque clause deux fois).

> 💡 Ici on dit seulement « **au plus** une » : une diagonale peut être vide (il y a `2n − 1` diagonales de chaque type pour seulement `n` reines).

**Vérification sur la Figure 1** : différences `i − j` = −3, 0, −2, 1, 4 et sommes `i + j` = 5, 4, 8, 7, 6, toutes distinctes ✅.

### Q 3.5 « Au plus une reine par case » ?

**Non, ce n'est pas nécessaire.** Une variable `x_{i,j}` vaut soit 0, soit 1 : une case contient donc 0 ou 1 reine **par construction**. On ne peut pas représenter « deux reines sur la même case » avec ces variables. (C'est différent des pigeons ou du Sudoku, où une case peut recevoir plusieurs valeurs : `x_{i,j,k}` pour chaque `k`.)

---

## Exercice 4 : Formes normales

### Q 4.1 `a ⇔ ((b ∧ ¬a) ∨ c)`

On note `R = (b ∧ ¬a) ∨ c`.

```
a ⇔ R
≡ (a ⇒ R) ∧ (R ⇒ a)                          définition de ⇔
≡ (¬a ∨ R) ∧ (¬R ∨ a)                        définition de ⇒
```

**Partie gauche**
```
¬a ∨ (b ∧ ¬a) ∨ c
≡ ¬a ∨ c                                     absorption : ¬a ∨ (¬a ∧ b) ≡ ¬a
```

**Partie droite**
```
¬((b ∧ ¬a) ∨ c) ∨ a
≡ (¬(b ∧ ¬a) ∧ ¬c) ∨ a                       De Morgan
≡ ((¬b ∨ a) ∧ ¬c) ∨ a                        De Morgan + double négation
≡ (¬b ∨ a ∨ a) ∧ (¬c ∨ a)                    distributivité
≡ (a ∨ ¬b) ∧ (a ∨ ¬c)                        idempotence
```

✅ **FNC** : `(¬a ∨ c) ∧ (a ∨ ¬b) ∧ (a ∨ ¬c)`

**FND** : on distribue la FNC. On remarque que `(¬a ∨ c) ∧ (a ∨ ¬c)` est la définition de `a ⇔ c`, c'est-à-dire `(a ∧ c) ∨ (¬a ∧ ¬c)` :

```
((a ∧ c) ∨ (¬a ∧ ¬c)) ∧ (a ∨ ¬b)
≡ (a ∧ c ∧ a) ∨ (a ∧ c ∧ ¬b) ∨ (¬a ∧ ¬c ∧ a) ∨ (¬a ∧ ¬c ∧ ¬b)     distributivité
≡ (a ∧ c) ∨ (a ∧ c ∧ ¬b) ∨ ⊥ ∨ (¬a ∧ ¬b ∧ ¬c)                     idempotence, complémentation
≡ (a ∧ c) ∨ (¬a ∧ ¬b ∧ ¬c)                                        absorption, identité
```

✅ **FND** : `(a ∧ c) ∨ (¬a ∧ ¬b ∧ ¬c)`

**Vérification rapide** : avec `a = 1, c = 1`, la droite vaut `c = 1` ✅. Avec `a = 0, b = 0, c = 0`, la droite vaut 0 ✅. Avec `a = 0, b = 1, c = 0`, la droite vaut `b ∧ ¬a = 1` mais `a = 0`, donc faux, et la FND donne bien 0 ✅.

### Q 4.2 `((q ∧ (s ⇒ f)) ∨ (¬s ∧ g)) ⇒ (q ∨ (¬f ∧ ¬g))`

```
≡ ¬((q ∧ (¬s ∨ f)) ∨ (¬s ∧ g)) ∨ q ∨ (¬f ∧ ¬g)          définition de ⇒ (deux fois)
≡ (¬(q ∧ (¬s ∨ f)) ∧ ¬(¬s ∧ g)) ∨ q ∨ (¬f ∧ ¬g)         De Morgan
≡ ((¬q ∨ (s ∧ ¬f)) ∧ (s ∨ ¬g)) ∨ q ∨ (¬f ∧ ¬g)          De Morgan + double négation
≡ ((¬q ∨ s) ∧ (¬q ∨ ¬f) ∧ (s ∨ ¬g)) ∨ q ∨ (¬f ∧ ¬g)     distributivité
```

On distribue d'abord le `∨ q` sur les trois clauses :

```
≡ ((¬q ∨ s ∨ q) ∧ (¬q ∨ ¬f ∨ q) ∧ (s ∨ ¬g ∨ q)) ∨ (¬f ∧ ¬g)
≡ (⊤ ∧ ⊤ ∧ (q ∨ s ∨ ¬g)) ∨ (¬f ∧ ¬g)                     complémentation, zéro
≡ (q ∨ s ∨ ¬g) ∨ (¬f ∧ ¬g)                               identité
≡ (q ∨ s ∨ ¬g ∨ ¬f) ∧ (q ∨ s ∨ ¬g ∨ ¬g)                  distributivité
≡ (q ∨ s ∨ ¬f ∨ ¬g) ∧ (q ∨ s ∨ ¬g)                       idempotence
≡ q ∨ s ∨ ¬g                                             absorption
```

✅ **FNC** : `q ∨ s ∨ ¬g`

> 💡 La dernière étape est une **absorption** de clauses : si une clause `C` est présente, toute clause plus grande `C ∨ x` est inutile (`C ∧ (C ∨ x) ≡ C`).

**Vérification** : la clause n'est fausse que si `q = 0, s = 0, g = 1`. Alors l'hypothèse vaut `(0 ∧ …) ∨ (1 ∧ 1) = 1` et la conclusion `0 ∨ (¬f ∧ 0) = 0` : la formule vaut bien 0 ✅.
