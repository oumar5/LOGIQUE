# ✅ Correction du quiz

> Correction de [Quiz.md](Quiz.md). Chapitre à relire entre parenthèses en cas d'erreur.

---

## Partie A — Syntaxe ([ch. 1](../01-Cours/01-Logique-propositionnelle/1-Syntaxe.md))

| # | Réponse | Pourquoi |
|---|---|---|
| A1 | `(a ∨ (b ∧ (¬c))) ⇒ d` | `¬` > `∧` > `∨` > `⇒` |
| A2 | `a ⇒ (b ⇒ c)` | `⇒` se regroupe à droite |
| A3 | `h = 3`, `Var = {a, b}` | `h(¬b) = 1`, `h(a ∧ ¬b) = 2`, `h(¬(…)) = 3` |

## Partie B — Sémantique ([ch. 2](../01-Cours/01-Logique-propositionnelle/2-Semantique.md))

| # | Réponse | Pourquoi |
|---|---|---|
| B1 | **0** | `a ⇒ b = 1 ⇒ 0 = 0` et `¬c = 0` |
| B2 | **oui** | `a ⇒ b` n'est faux que si `a = 1, b = 0`, et alors `b ⇒ a = 1` |
| B3 | **non** | `¬a ∧ ¬b` impose `a = b = 0`, donc `a ∨ b = 0` |
| B4 | **vrai** | « toujours 1 » ⇔ « sa négation n'est jamais 1 » |
| B5 | **32** | `2⁵` |

## Partie C — Équivalences ([ch. 3](../01-Cours/01-Logique-propositionnelle/3-Equivalences.md))

| # | Réponse | Pourquoi |
|---|---|---|
| C1 | `a ∧ ¬b` | De Morgan + double négation |
| C2 | `a` | absorption |
| C3 | **non** | avec seulement `∧` et `∨`, si toutes les variables valent 1, la formule vaut 1 : impossible d'écrire `¬a` |
| C4 | « si l'école n'est pas fermée, alors il ne neige pas » | `φ ⇒ ψ ≡ ¬ψ ⇒ ¬φ` |

## Partie D — Formes normales ([ch. 4](../01-Cours/01-Logique-propositionnelle/4-Formes-normales.md))

| # | Réponse | Pourquoi |
|---|---|---|
| D1 | `(¬a ∧ ¬b) ∨ (a ∧ b)` | lignes à 1 : `00` et `11` |
| D2 | `(a ∨ ¬b) ∧ (¬a ∨ b)` | lignes à 0 : `01` → `a ∨ ¬b`, `10` → `¬a ∨ b` |
| D3 | `(a ∨ c) ∧ (a ∨ d) ∧ (b ∨ c) ∧ (b ∨ d)` | un littéral de chaque bloc |
| D4 | FNC **oui**, FND **non** | clauses `a ∨ b` et `¬c` ; sa FND serait `(a ∧ ¬c) ∨ (b ∧ ¬c)` |

## Partie E — SAT ([ch. 5](../01-Cours/02-SAT/5-Probleme-SAT.md), [6](../01-Cours/02-SAT/6-Modeliser-avec-SAT.md), [7](../01-Cours/02-SAT/7-SAT-en-Python.md))

| # | Réponse |
|---|---|
| E1 | `(¬a ∨ ¬b) ∧ (¬a ∨ ¬c) ∧ (¬b ∨ ¬c)` |
| E2 | `9 × 8 / 2 = 36` |
| E3 | `p ⇒ ¬m`, donc `¬p ∨ ¬m` |
| E4 | `p cnf 3 2` / `1 -3 0` / `2 0` |
| E5 | SAT est dans NP (un « devin » le résout vite, vérifier est rapide) et **tout** problème de NP se traduit en SAT (Cook-Levin, 1971) |

## Partie F — Tseitin, DPLL, programmation ([ch. 8](../01-Cours/02-SAT/8-Tseitin.md), [9](../01-Cours/02-SAT/9-DPLL.md), [10](../01-Cours/02-SAT/10-Operateurs-en-programmation.md))

| # | Réponse |
|---|---|
| F1 | `(¬y ∨ ¬z ∨ x) ∧ (¬x ∨ y) ∧ (¬x ∨ z)` |
| F2 | la distributivité peut rendre la FNC **exponentielle** ; Tseitin reste **linéaire** (et équisatisfiable) |
| F3 | `c = 0` (unitaire) → `a = 0` (unitaire) → `b = 1` (unitaire) → SAT : `a = 0, b = 1, c = 0` |
| F4 | `a`, `¬b` et `c` sont **tous** purs → `a = 1, b = 0, c = 1` → SAT |
| F5 | `and` est séquentiel à gauche : `x != 0` est faux, la division n'est **jamais calculée** |

## Partie G — Termes ([ch. 11](../01-Cours/03-Termes/11-Termes.md) à [14](../01-Cours/03-Termes/14-Unification.md))

| # | Réponse | Pourquoi |
|---|---|---|
| G1 | **non** | `plus` attend 2 arguments |
| G2 | **9** | `plus(4, 4) = 8`, `succ(8) = 9` |
| G3 | `f(y, a)` | remplacement **simultané** : le `y` venu de `x ↦ y` n'est pas remplacé |
| G4 | `{ x ↦ b, y ↦ a }` | décomposer, puis orienter `a = y` |
| G5 | il faudrait `x = g(x)` | **occurrence** : `x` apparaît dans `g(x)`, ce serait un terme infini |

## Partie H — Premier ordre ([ch. 15](../01-Cours/04-Logique-premier-ordre/15-Syntaxe-premier-ordre.md) à [17](../01-Cours/04-Logique-premier-ordre/17-Modeliser-premier-ordre.md))

| # | Réponse | Pourquoi |
|---|---|---|
| H1 | `{y}` | `x` est lié par `∀x` |
| H2 | `∃x (Etudiant(x) ∧ ¬ACarte(x))` : « un étudiant n'a pas de carte » | `¬∀ ≡ ∃¬`, puis `¬(A ⇒ B) ≡ A ∧ ¬B` |
| H3 | `∃x (Prof(x) ∧ Sympa(x))` | `∃` avec `∧` |
| H4 | **non** | 1ʳᵉ : chacun aime quelqu'un ; 2ᵉ : une même personne est aimée de tous |
| H5 | `∀x (Chat(x) ⇒ ¬Aboie(x))` | `∀` avec `⇒` (ou `¬∃x (Chat(x) ∧ Aboie(x))`) |
