# ✅ Quiz d'auto-évaluation

> Réponds sur papier, **puis** compare avec la [correction du quiz](Quiz-correction.md).
> Note tes erreurs et relis le chapitre indiqué.

| Score (sur 36) | Interprétation |
|---|---|
| 31 – 36 | prête pour le DS 🎉 |
| 22 – 30 | relire les parties ratées |
| moins de 22 | refaire les chapitres et les exercices |

---

## Partie A — Syntaxe (ch. 1)

- **A1.** Ajoute toutes les parenthèses : `a ∨ b ∧ ¬c ⇒ d`
- **A2.** Comment se lit `a ⇒ b ⇒ c` ?
- **A3.** Calcule `h(¬(a ∧ ¬b))` et `Var(¬(a ∧ ¬b))`.

## Partie B — Sémantique (ch. 2)

- **B1.** Avec `a = 1, b = 0, c = 1`, que vaut `(a ⇒ b) ∨ ¬c` ?
- **B2.** `(a ⇒ b) ∨ (b ⇒ a)` est-elle une tautologie ?
- **B3.** `(a ∨ b) ∧ ¬a ∧ ¬b` est-elle satisfiable ?
- **B4.** Vrai ou faux : « `φ` est une tautologie ssi `¬φ` est insatisfiable ».
- **B5.** Combien de lignes a la table de vérité d'une formule à 5 variables ?

## Partie C — Équivalences (ch. 3)

- **C1.** Simplifie `¬(¬a ∨ b)`.
- **C2.** Simplifie `(a ∧ b) ∨ a`.
- **C3.** `{∧, ∨}` est-il un système complet ? Pourquoi ?
- **C4.** Quelle est la contraposée de « s'il neige, l'école est fermée » ?

## Partie D — Formes normales (ch. 4)

- **D1.** FND de `a ⇔ b` (par la table) ?
- **D2.** FNC de `a ⇔ b` (par la table) ?
- **D3.** FNC de `(a ∧ b) ∨ (c ∧ d)` ?
- **D4.** `(a ∨ b) ∧ ¬c` est-elle en FNC ? En FND ?

## Partie E — SAT (ch. 5 à 7)

- **E1.** Écris « au plus un parmi `a, b, c` ».
- **E2.** Combien de clauses pour « au plus un » parmi 9 variables ?
- **E3.** « Si Paul vient, Marie ne vient pas » en clause ?
- **E4.** Écris `(x₁ ∨ ¬x₃) ∧ x₂` au format DIMACS.
- **E5.** Que signifie « SAT est NP-complet » ?

## Partie F — Tseitin, DPLL, programmation (ch. 8 à 10)

- **F1.** Clauses de Tseitin pour `x ⇔ (y ∧ z)` ?
- **F2.** Pourquoi Tseitin plutôt que la distributivité ?
- **F3.** DPLL sur `(a ∨ b) ∧ (¬a ∨ c) ∧ ¬c ∧ (b ∨ d)`.
- **F4.** Quels sont les littéraux purs dans `(a ∨ ¬b) ∧ (¬b ∨ c) ∧ (a ∨ c)` ?
- **F5.** Pourquoi `x != 0 and 10 / x > 1` ne plante pas quand `x = 0` ?

## Partie G — Termes (ch. 11 à 14)

- **G1.** Avec `{ zero/0, succ/1, plus/2 }`, `plus(succ(zero))` est-il un terme ?
- **G2.** Que vaut `succ(plus(x, x))` dans ℕ avec `x = 4` ?
- **G3.** Calcule `f(x, y)σ` avec `σ = { x ↦ y, y ↦ a }`.
- **G4.** Donne le mgu de `f(x, a)` et `f(b, y)`.
- **G5.** Pourquoi `x` et `g(x)` ne sont-ils pas unifiables ?

## Partie H — Premier ordre (ch. 15 à 17)

- **H1.** Quelles sont les variables libres de `∀x R(x, y)` ?
- **H2.** Nie « tous les étudiants ont une carte ».
- **H3.** Traduis « certains profs sont sympas ».
- **H4.** `∀x ∃y Aime(x, y)` et `∃y ∀x Aime(x, y)` disent-elles la même chose ?
- **H5.** Traduis « aucun chat n'aboie ».
