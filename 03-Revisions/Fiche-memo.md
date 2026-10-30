# 📋 Fiche mémo — tout le cours en un coup d'œil

> À relire la veille d'un DS. Chaque bloc renvoie au chapitre correspondant.

---

## Logique propositionnelle (ch. 1 à 4)

### Tables de vérité

| a | b | ¬a | a ∧ b | a ∨ b | a ⇒ b | a ⇔ b |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| 0 | 0 | 1 | 0 | 0 | 1 | 1 |
| 0 | 1 | 1 | 0 | 1 | 1 | 0 |
| 1 | 0 | 0 | 0 | 1 | **0** | 0 |
| 1 | 1 | 0 | 1 | 1 | 1 | 1 |

`¬ = 1 − x` · `∧ = min` · `∨ = max` · `⇒` faux **seulement** pour `1 ⇒ 0` (promesse rompue) · `⇔` vrai si **mêmes valeurs**

### Priorités

`¬` > `∧` > `∨` > `⇒`, `⇔` · `∧ ∨ ⇔` se regroupent à gauche · `⇒` à **droite** : `a ⇒ b ⇒ c = a ⇒ (b ⇒ c)`

### Vocabulaire

| Mot | Sens |
|---|---|
| valuation | une situation : chaque variable vaut 0 ou 1 |
| satisfiable | vraie dans **au moins une** situation |
| tautologie `⊨ φ` | vraie dans **toutes** les situations |
| `φ ≡ ψ` | même table de vérité |
| `Γ ⊨ φ` | quand tout `Γ` est vrai, `φ` est vrai |
| littéral / clause | `x` ou `¬x` / des littéraux reliés par `∨` |
| FND / FNC | **∨** de **∧** (scénarios) / **∧** de **∨** (règles) |
| table à `n` variables | `2ⁿ` lignes |

### Lois

| | |
|---|---|
| `φ ⇒ ψ ≡ ¬φ ∨ ψ` | `φ ⇔ ψ ≡ (¬φ ∨ ψ) ∧ (φ ∨ ¬ψ)` |
| `¬(φ ∨ ψ) ≡ ¬φ ∧ ¬ψ` | `¬(φ ∧ ψ) ≡ ¬φ ∨ ¬ψ` |
| `¬¬φ ≡ φ` | `¬(φ ⇒ ψ) ≡ φ ∧ ¬ψ` |
| `φ ∨ (ψ ∧ θ) ≡ (φ ∨ ψ) ∧ (φ ∨ θ)` | `φ ∧ (ψ ∨ θ) ≡ (φ ∧ ψ) ∨ (φ ∧ θ)` |
| `φ ∨ (φ ∧ ψ) ≡ φ` | `φ ∧ (φ ∨ ψ) ≡ φ` |
| `φ ∨ ¬φ ≡ ⊤`, `φ ∧ ¬φ ≡ ⊥` | contraposée : `φ ⇒ ψ ≡ ¬ψ ⇒ ¬φ` |

Systèmes complets : `{¬,∨}` `{¬,∧}` `{¬,⇒}` `{⇒,⊥}`

### FND / FNC par la table

| | Lignes | Par ligne |
|---|---|---|
| FND | à **1** | un `∧` : `1 → x`, `0 → ¬x` |
| FNC | à **0** | un `∨` **inversé** : `0 → x`, `1 → ¬x` |

---

## SAT (ch. 5 à 10)

### Motifs

| Règle | Clauses |
|---|---|
| au moins un | `x₁ ∨ … ∨ xₙ` |
| au plus un | `¬xᵢ ∨ ¬xⱼ` pour chaque `i < j` (`n(n−1)/2` clauses) |
| si `a` alors `b` | `¬a ∨ b` |
| pas les deux | `¬a ∨ ¬b` |
| imposé / interdit | `a` / `¬a` |

### Python / DIMACS

`xₖ → k` · `¬xₖ → -k` · clause → `[1, -2, 3]` · `⋀` → boucle extérieure · `⋁` → liste intérieure · condition → `if`

### Tseitin

| Nœud | Clauses |
|---|---|
| `x ⇔ x₁ ∧ x₂` | `(¬x₁ ∨ ¬x₂ ∨ x)(¬x ∨ x₁)(¬x ∨ x₂)` |
| `x ⇔ x₁ ∨ x₂` | `(x₁ ∨ x₂ ∨ ¬x)(¬x₁ ∨ x)(¬x₂ ∨ x)` |
| `x ⇔ x₁ ⇒ x₂` | `(¬x₁ ∨ x₂ ∨ ¬x)(x ∨ x₁)(x ∨ ¬x₂)` |
| `x ⇔ ¬y` | `(x ∨ y)(¬x ∨ ¬y)` |

\+ la clause **`x`**. Taille linéaire, **équisatisfiable**.

### DPLL

simplification → **unitaire** → **pur** → **pari** (puis l'autre branche si échec).
Fixer `l` : supprimer les clauses avec `l`, retirer `l̄` des autres. Plus de clauses = SAT ; clause vide = échec.

### Programmation

`&&`, `||` séquentiels à gauche : `0 && ⊥⊥ = 0`, `1 || ⊥⊥ = 1`, mais `⊥⊥ && 0 = ⊥⊥` → mettre la **protection à gauche**.
SAT est **NP-complet** (Cook-Levin 1971).

---

## Termes (ch. 11 à 14)

| Notion | À retenir |
|---|---|
| signature | symboles + **arité** (arité 0 = constante) |
| terme | variable, constante, ou `f(t₁, …, tₙ)` avec **exactement** `n` arguments |
| clos | sans variable |
| F-algèbre | domaine + une fonction `f_A : Dⁿ → D` par symbole |
| valeur | `⟦x⟧ρ = ρ(x)`, `⟦f(t₁…tₙ)⟧ρ = f_A(⟦t₁⟧ρ, …)` |
| substitution | remplacement **simultané** des variables |
| `στ` | appliquer `τ` dans `σ`, puis ajouter `τ` pour les variables hors de `σ` |
| unification | trouver `σ` avec `sσ = tσ` ; le **mgu** est le plus général |

**Règles d'unification** : effacer · décomposer · **conflit ❌** · orienter · **occurrence ❌** · éliminer

---

## Premier ordre (ch. 15 à 17)

| Notion | À retenir |
|---|---|
| fonction / prédicat | donne un **objet** / donne **vrai ou faux** |
| variable liée / libre | attrapée par `∀`/`∃` / non |
| structure | domaine + sens des fonctions + sens des prédicats |
| `∀x φ` / `∃x φ` | pour **chaque** objet (`all`) / pour **au moins un** (`any`) |
| négation | `¬∀x φ ≡ ∃x ¬φ` · `¬∃x φ ≡ ∀x ¬φ` |
| ordre | `∀x ∃y` ≠ `∃y ∀x` |
| distributivité | `∀` sur `∧` ✅, `∃` sur `∨` ✅, l'inverse ❌ |
| valide | vraie dans toutes les structures ; **indécidable** en général |

**Règle d'or de modélisation** : `∀x (A(x) ⇒ B(x))` · `∃x (A(x) ∧ B(x))` · « seuls les A sont B » : `∀x (B(x) ⇒ A(x))`
