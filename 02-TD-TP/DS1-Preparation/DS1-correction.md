# Préparation au DS1 — correction

> Correction de [DS1-enonce-fourni.md](DS1-enonce-fourni.md), rédigée pour réviser. Toutes les tables, solutions et FNC ont été **vérifiées par calcul** (comparaison de toutes les valuations).
> Ce n'est pas une correction officielle : compare avec celle de l'enseignante si elle est donnée.

---

## Exercice 1 : Tables de vérité

**Méthode** ([ch. 2](../../01-Cours/01-Logique-propositionnelle/2-Semantique.md)) : une colonne par sous-formule, des plus petites aux plus grandes ; les valuations en comptant en binaire. Rappel : `⇒` ne vaut 0 que pour `1 ⇒ 0` ; `⇔` vaut 1 quand les deux côtés sont égaux.

### Q 1.1 `(a ⇔ b) ⇒ (a ∧ b)`

| a | b | a ⇔ b | a ∧ b | **résultat** |
|:-:|:-:|:-:|:-:|:-:|
| 0 | 0 | 1 | 0 | **0** |
| 0 | 1 | 0 | 0 | **1** |
| 1 | 0 | 0 | 0 | **1** |
| 1 | 1 | 1 | 1 | **1** |

💡 La colonne est celle de `a ∨ b` : la formule est **équivalente à `a ∨ b`**.

### Q 1.2 `(¬c ∧ b) ∨ (b ⇒ (a ∧ c))`

| a | b | c | ¬c ∧ b | a ∧ c | b ⇒ (a ∧ c) | **résultat** |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| 0 | 0 | 0 | 0 | 0 | 1 | **1** |
| 0 | 0 | 1 | 0 | 0 | 1 | **1** |
| 0 | 1 | 0 | 1 | 0 | 0 | **1** |
| 0 | 1 | 1 | 0 | 0 | 0 | **0** |
| 1 | 0 | 0 | 0 | 0 | 1 | **1** |
| 1 | 0 | 1 | 0 | 1 | 1 | **1** |
| 1 | 1 | 0 | 1 | 0 | 0 | **1** |
| 1 | 1 | 1 | 0 | 1 | 1 | **1** |

💡 Une seule ligne à 0 (`a = 0, b = 1, c = 1`) : la FNC est la clause **`a ∨ ¬b ∨ ¬c`**.

### Q 1.3 `(¬a ∨ ¬b ∨ c) ∧ ((a ∨ c) ⇒ (b ∧ ¬c))`

| a | b | c | ¬a ∨ ¬b ∨ c | a ∨ c | b ∧ ¬c | (a ∨ c) ⇒ (b ∧ ¬c) | **résultat** |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| 0 | 0 | 0 | 1 | 0 | 0 | 1 | **1** |
| 0 | 0 | 1 | 1 | 1 | 0 | 0 | **0** |
| 0 | 1 | 0 | 1 | 0 | 1 | 1 | **1** |
| 0 | 1 | 1 | 1 | 1 | 0 | 0 | **0** |
| 1 | 0 | 0 | 1 | 1 | 0 | 0 | **0** |
| 1 | 0 | 1 | 1 | 1 | 0 | 0 | **0** |
| 1 | 1 | 0 | 0 | 1 | 1 | 1 | **0** |
| 1 | 1 | 1 | 1 | 1 | 0 | 0 | **0** |

💡 Vraie seulement quand `a = 0` et `c = 0` : la formule est **équivalente à `¬a ∧ ¬c`**.

### Q 1.4 `((a ∨ ¬b) ⇒ (b ∧ c)) ⇔ ((¬a ∧ c) ∨ (b ∧ a))`

On note `G` la partie gauche et `D` la partie droite.

| a | b | c | a ∨ ¬b | b ∧ c | **G** | ¬a ∧ c | b ∧ a | **D** | **G ⇔ D** |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | **1** |
| 0 | 0 | 1 | 1 | 0 | 0 | 1 | 0 | 1 | **0** |
| 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | **0** |
| 0 | 1 | 1 | 0 | 1 | 1 | 1 | 0 | 1 | **1** |
| 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | **1** |
| 1 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | **1** |
| 1 | 1 | 0 | 1 | 0 | 0 | 0 | 1 | 1 | **0** |
| 1 | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 1 | **1** |

### Q 1.5 `((a ∨ b) ⇒ c) ⇔ (¬a ∧ (b ∨ c))`

| a | b | c | a ∨ b | **G** = (a ∨ b) ⇒ c | b ∨ c | **D** = ¬a ∧ (b ∨ c) | **G ⇔ D** |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| 0 | 0 | 0 | 0 | 1 | 0 | 0 | **0** |
| 0 | 0 | 1 | 0 | 1 | 1 | 1 | **1** |
| 0 | 1 | 0 | 1 | 0 | 1 | 1 | **0** |
| 0 | 1 | 1 | 1 | 1 | 1 | 1 | **1** |
| 1 | 0 | 0 | 1 | 0 | 0 | 0 | **1** |
| 1 | 0 | 1 | 1 | 1 | 1 | 0 | **0** |
| 1 | 1 | 0 | 1 | 0 | 1 | 0 | **1** |
| 1 | 1 | 1 | 1 | 1 | 1 | 0 | **0** |

### Q 1.6 `(x ∧ y) ⇒ ((z ∨ ¬x) ∧ (y ∨ ¬z ∨ x))`

On note `K = (z ∨ ¬x) ∧ (y ∨ ¬z ∨ x)`.

| x | y | z | x ∧ y | z ∨ ¬x | y ∨ ¬z ∨ x | K | **résultat** |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| 0 | 0 | 0 | 0 | 1 | 1 | 1 | **1** |
| 0 | 0 | 1 | 0 | 1 | 0 | 0 | **1** |
| 0 | 1 | 0 | 0 | 1 | 1 | 1 | **1** |
| 0 | 1 | 1 | 0 | 1 | 1 | 1 | **1** |
| 1 | 0 | 0 | 0 | 0 | 1 | 0 | **1** |
| 1 | 0 | 1 | 0 | 1 | 1 | 1 | **1** |
| 1 | 1 | 0 | 1 | 0 | 1 | 0 | **0** |
| 1 | 1 | 1 | 1 | 1 | 1 | 1 | **1** |

💡 Dès que `x ∧ y` vaut 0, l'implication vaut 1 sans regarder la droite : seules les 2 dernières lignes demandent un vrai calcul. La formule est équivalente à **`¬x ∨ ¬y ∨ z`**.

> ⏱️ **Astuce DS** : repère d'abord les lignes où le résultat est **forcé** (hypothèse fausse pour `⇒`, un facteur nul pour `∧`…). Ça va beaucoup plus vite.

---

## Exercice 2 : les voyages d'Assia

### Q 2.1 Variables

| Variable | Vraie ssi |
|---|---|
| `c` | Assia a visité la **Colombie** |
| `k` | Assia a visité le **Kenya** |
| `m` | Assia a visité la **Malaisie** |

### Q 2.2 Formules

| # | Phrase | Formule |
|---|---|---|
| 1 | au moins un des trois pays | `c ∨ k ∨ m` |
| 2 | si Colombie ou pas Kenya, alors Malaisie | `(c ∨ ¬k) ⇒ m` |
| 3 | si Kenya et Malaisie, alors pas Colombie | `(k ∧ m) ⇒ ¬c` |
| 4 | si Malaisie, alors **exactement un** autre pays parmi Kenya et Colombie | `m ⇒ ((k ∨ c) ∧ ¬(k ∧ c))` |
| 5 | si pas Colombie, alors pas Kenya | `¬c ⇒ ¬k` |

> 💡 « Un seul et un seul parmi `k` et `c` » est un **ou exclusif** : `(k ∨ c) ∧ ¬(k ∧ c)`, qu'on peut aussi écrire `¬(k ⇔ c)`.

### Q 2.3 Solution

On raisonne par cas sur `c`.

- **Si `c = 0`** : par (5), `k = 0`. Par (1), il faut alors `m = 1`. Mais (4) exige exactement un pays parmi Kenya et Colombie, or les deux sont à 0. **Contradiction.**
- **Donc `c = 1`.** Par (2), `c ∨ ¬k` est vrai, donc `m = 1`. Par (4), exactement un parmi `k` et `c` : comme `c = 1`, `k = 0`.
- **Vérification** : (1) ✅, (2) ✅, (3) `k ∧ m = 0` donc ✅, (4) ✅, (5) `¬c = 0` donc ✅.

**Assia a visité la Colombie et la Malaisie, mais pas le Kenya.** C'est la seule solution (les 8 valuations ont été testées).

---

## Exercice 3 : Colombo

### Q 3.1 Déclaration d'Alice

« Bob ment » : Bob est le menteur, donc Alice ne l'est pas : `¬a`.
« Je n'ai rien volé » : ni l'ordinateur, ni le téléphone : `¬o ∧ ¬t`.

**`A = ¬a ∧ ¬o ∧ ¬t`**

### Q 3.2 Déclaration de Bob

« Celui qui ment a commis tous les vols » : si c'est Alice qui ment, elle a tout volé ; si c'est Bob, c'est lui qui a tout volé (donc Alice rien).

**`B = (a ⇒ (o ∧ t)) ∧ (¬a ⇒ (¬o ∧ ¬t))`**

(équivalent à `(a ∧ o ∧ t) ∨ (¬a ∧ ¬o ∧ ¬t)`, ou encore à `(a ⇔ o) ∧ (a ⇔ t)`)

### Q 3.3 Menteur et sincère

- Si Alice ment (`a`), sa phrase est fausse et celle de Bob est vraie : `a ⇒ (¬A ∧ B)`.
- Si Bob ment (`¬a`), la phrase d'Alice est vraie et celle de Bob fausse : `¬a ⇒ (A ∧ ¬B)`.

**`(a ⇒ (¬A ∧ B)) ∧ (¬a ⇒ (A ∧ ¬B))`**, ce qui revient à **`(A ⇔ ¬a) ∧ (B ⇔ a)`**.

### Q 3.4 Les faits

- **Supposons `a = 0`** (Bob est le menteur). Alors `A` doit être vraie : `¬o ∧ ¬t`, donc Bob a tout volé. Mais alors la phrase de Bob « celui qui ment (Bob) a tout volé » est **vraie** ; or Bob ment, elle devrait être fausse. **Contradiction.**
- **Donc `a = 1`** : Alice ment. La phrase de Bob est vraie : comme Alice ment, elle a tout volé : `o = 1` et `t = 1`.
- **Vérification** : la phrase d'Alice `¬a ∧ ¬o ∧ ¬t` est bien fausse ✅ (elle ment) ; celle de Bob est vraie ✅.

**Alice est la menteuse et a volé l'ordinateur et le téléphone. Bob dit la vérité.** C'est la seule solution.

---

## Exercice 4 : le puzzle

### Q 4.1 Variables

`x_{p,i,j}` vraie ssi **la pièce `p` est posée sur la case `(i, j)`**, avec `p ∈ P` et `(i, j) ∈ C`. Il y a `n² × n² = n⁴` variables.

### Q 4.2 Chaque pièce occupe une et une seule case

- au moins une : `⋀_{p∈P} ⋁_{(i,j)∈C} x_{p,i,j}`
- au plus une : `⋀_{p∈P} ⋀_{(i,j)≠(i',j')} (¬x_{p,i,j} ∨ ¬x_{p,i',j'})`

### Q 4.3 Chaque case contient une et une seule pièce

- au moins une : `⋀_{(i,j)∈C} ⋁_{p∈P} x_{p,i,j}`
- au plus une : `⋀_{(i,j)∈C} ⋀_{p<p'} (¬x_{p,i,j} ∨ ¬x_{p',i,j})`

> 💡 Comme pour les pigeons et la table ronde, l'une des deux familles « au plus une » est redondante (principe des tiroirs : `n²` pièces, `n²` cases).

### Q 4.4 Bord nord = bord sud de la pièce au nord

La case au nord de `(i, j)` est `(i, j + 1)`, qui existe seulement si `j < n`. Si `p` est en `(i, j)`, la pièce `q` au-dessus doit vérifier `(p, q) ∈ NS`.

```
⋀_{p∈P} ⋀_{i∈[1,n]} ⋀_{j∈[1,n−1]} ( ¬x_{p,i,j} ∨ ⋁_{q | (p,q)∈NS} x_{q,i,j+1} )
```

Variante équivalente (avec les contraintes de la Q 4.3) : **interdire** les mauvaises paires :
`⋀ (¬x_{p,i,j} ∨ ¬x_{q,i,j+1})` pour tous `p ≠ q` avec `(p, q) ∉ NS`.

### Q 4.5 Bord est = bord ouest de la pièce à l'est

La case à l'est de `(i, j)` est `(i + 1, j)`, qui existe si `i < n` :

```
⋀_{p∈P} ⋀_{i∈[1,n−1]} ⋀_{j∈[1,n]} ( ¬x_{p,i,j} ∨ ⋁_{q | (p,q)∈EO} x_{q,i+1,j} )
```

### Q 4.6 Faut-il la contrainte « sud » ?

**Non.** Si `q` est au sud de `p`, alors `p` est au nord de `q`. La contrainte « bord sud de `p` = bord nord de `q` » est **exactement** la contrainte de la Q 4.4 appliquée à `q`. Chaque paire de pièces verticalement voisines est déjà vérifiée une fois. (D'ailleurs `(p, q) ∈ SN` ⇔ `(q, p) ∈ NS`.) Même raisonnement pour « ouest ».

### Remarque sur l'exemple

`NS` doit être exactement `SN` « retourné ». Avec `SN = {(1,3), (2,4), (3,2), (3,4), (4,2)}`, on obtient `NS = {(3,1), (4,2), (2,3), (4,3), (2,4)}`. **La paire `(2, 4)` manque sur la feuille** : le bord nord de la pièce 2 et le bord sud de la pièce 4 sont tous les deux blancs.

La solution donnée est bien la seule (les 24 placements ont été testés) : pièce 1 en `(1,2)`, pièce 2 en `(2,2)`, pièce 3 en `(1,1)`, pièce 4 en `(2,1)`. Vérification : `(1, 3) ∈ SN` (1 au-dessus de 3), `(2, 4) ∈ SN`, `(1, 2) ∈ EO`, `(3, 4) ∈ EO` ✅.

---

## Exercice 5 : la tournée du facteur

Rappel : `x_{(i,j),k}` vraie ssi le `k`-ième trajet va de `i` à `j`. Une **rue** `{i, j}` correspond à deux **trajets** `(i, j)` et `(j, i)`. On parcourt chaque rue une seule fois : c'est un **circuit eulérien**.

| Q | Contrainte | Formule FNC |
|---|---|---|
| 5.1 | chaque rue au moins une fois, dans au moins un sens | `⋀_{(i,j)∈T, i<j} ( ⋁_{k=1}^{m} x_{(i,j),k} ∨ ⋁_{k=1}^{m} x_{(j,i),k} )` |
| 5.2 | chaque trajet au plus une fois | `⋀_{(i,j)∈T} ⋀_{1≤k<k'≤m} (¬x_{(i,j),k} ∨ ¬x_{(i,j),k'})` |
| 5.3 | chaque rue dans au plus un sens | `⋀_{(i,j)∈T, i<j} ⋀_{k,k'∈[1,m]} (¬x_{(i,j),k} ∨ ¬x_{(j,i),k'})` |
| 5.4 | au moins un `k`-ième trajet | `⋀_{k=1}^{m} ⋁_{(i,j)∈T} x_{(i,j),k}` |
| 5.5 | le 1er trajet part de la poste | `⋁_{(1,j)∈T} x_{(1,j),1}` |
| 5.6 | le `m`-ième trajet arrive à la poste | `⋁_{(i,1)∈T} x_{(i,1),m}` |
| 5.7 | on repart d'où on est arrivé | `⋀_{k=1}^{m−1} ⋀_{(i,j)∈T} ( ¬x_{(i,j),k} ∨ ⋁_{(j,l)∈T} x_{(j,l),k+1} )` |

**Explications**

- **5.1** : une seule grande clause par rue ; elle contient les deux sens et tous les moments possibles.
- **5.3** : on interdit d'avoir le sens `i → j` à un moment **et** le sens `j → i` à un autre (y compris `k = k'`).
- **5.7** : c'est le motif « si… alors » : `x_{(i,j),k} ⇒ (OU des trajets qui partent de j au rang k + 1)`.
- 💡 Il n'est pas demandé d'écrire « au plus un `k`-ième trajet » : avec 5.1 à 5.4, chacune des `m` rues est prise exactement une fois, pour `m` rangs qui ont chacun au moins un trajet. Le principe des tiroirs donne exactement un trajet par rang.

---

## Exercice 6 : FNC

### Q 6.1

On traite les trois blocs séparément (la formule est déjà un `∧` de trois blocs).

**Bloc 1**
```
((b ⇒ ¬c) ∧ (d ⇒ e)) ∨ a
≡ ((¬b ∨ ¬c) ∧ (¬d ∨ e)) ∨ a          définition de ⇒
≡ (a ∨ ¬b ∨ ¬c) ∧ (a ∨ ¬d ∨ e)        distributivité de ∨ sur ∧
```

**Bloc 2**
```
c ∨ ((a ⇒ ¬f) ∧ (¬b ⇒ f))
≡ c ∨ ((¬a ∨ ¬f) ∧ (b ∨ f))           définition de ⇒ (et ¬¬b ≡ b)
≡ (¬a ∨ c ∨ ¬f) ∧ (b ∨ c ∨ f)         distributivité
```

**Bloc 3** : `b ∨ d ∨ ¬e` est déjà une clause.

✅ **FNC** : `(a ∨ ¬b ∨ ¬c) ∧ (a ∨ ¬d ∨ e) ∧ (¬a ∨ c ∨ ¬f) ∧ (b ∨ c ∨ f) ∧ (b ∨ d ∨ ¬e)`

### Q 6.2 `(a ∨ b ∧ ¬c) ⇔ (a ∧ (c ∨ ¬b))`

Priorités : `∧` avant `∨`, donc la gauche est `a ∨ (b ∧ ¬c)`.
Astuce : on pose `X = b ∧ ¬c`. Par De Morgan, `c ∨ ¬b ≡ ¬X`.
La formule devient `(a ∨ X) ⇔ (a ∧ ¬X)`.

```
(a ∨ X) ⇔ (a ∧ ¬X)
≡ (¬(a ∨ X) ∨ (a ∧ ¬X)) ∧ ((a ∨ X) ∨ ¬(a ∧ ¬X))     définition de ⇔
≡ ((¬a ∧ ¬X) ∨ (a ∧ ¬X)) ∧ (a ∨ X ∨ ¬a ∨ X)         De Morgan
≡ (¬X ∧ (¬a ∨ a)) ∧ ⊤                               distributivité, complémentation
≡ ¬X
≡ ¬b ∨ c                                            De Morgan sur ¬(b ∧ ¬c)
```

✅ **FNC** : `¬b ∨ c`. Une formule qui a l'air compliquée se réduit à une seule clause ! (Vérifié sur les 8 valuations.)

---

## Exercice 7 : FNC avec les étapes

### Q 7.1 `(a ∧ b) ⇔ (c ∨ d)`

```
(a ∧ b) ⇔ (c ∨ d)
≡ ((a ∧ b) ⇒ (c ∨ d)) ∧ ((c ∨ d) ⇒ (a ∧ b))         définition de ⇔
≡ (¬(a ∧ b) ∨ c ∨ d) ∧ (¬(c ∨ d) ∨ (a ∧ b))         définition de ⇒
≡ (¬a ∨ ¬b ∨ c ∨ d) ∧ ((¬c ∧ ¬d) ∨ (a ∧ b))         De Morgan
```

On distribue `(¬c ∧ ¬d) ∨ (a ∧ b)` : un littéral de chaque bloc.
`(¬c ∨ a) ∧ (¬c ∨ b) ∧ (¬d ∨ a) ∧ (¬d ∨ b)`

✅ **FNC** : `(¬a ∨ ¬b ∨ c ∨ d) ∧ (a ∨ ¬c) ∧ (b ∨ ¬c) ∧ (a ∨ ¬d) ∧ (b ∨ ¬d)`

### Q 7.2 `((a ∧ b) ⇒ (c ∧ d)) ∨ (a ∧ ¬d)`

```
((a ∧ b) ⇒ (c ∧ d)) ∨ (a ∧ ¬d)
≡ ¬a ∨ ¬b ∨ (c ∧ d) ∨ (a ∧ ¬d)                      définition de ⇒ + De Morgan
≡ (¬a ∨ (a ∧ ¬d)) ∨ ¬b ∨ (c ∧ d)                    on regroupe ¬a avec (a ∧ ¬d)
≡ ((¬a ∨ a) ∧ (¬a ∨ ¬d)) ∨ ¬b ∨ (c ∧ d)             distributivité
≡ ¬a ∨ ¬d ∨ ¬b ∨ (c ∧ d)                            complémentation + identité
≡ (¬a ∨ ¬b ∨ ¬d ∨ c) ∧ (¬a ∨ ¬b ∨ ¬d ∨ d)           distributivité
≡ ¬a ∨ ¬b ∨ c ∨ ¬d                                  la 2ᵉ clause vaut ⊤
```

✅ **FNC** : `¬a ∨ ¬b ∨ c ∨ ¬d`

**Vérification** : cette clause n'est fausse que pour `a = 1, b = 1, c = 0, d = 1`. Dans ce cas, `(a ∧ b) ⇒ (c ∧ d) = 1 ⇒ 0 = 0` et `a ∧ ¬d = 0` : la formule de départ vaut bien 0 ✅.

> 💡 Sans le regroupement astucieux, la distributivité directe donne plusieurs clauses qui contiennent `x ∨ ¬x` et disparaissent. Les deux chemins mènent au même résultat.
