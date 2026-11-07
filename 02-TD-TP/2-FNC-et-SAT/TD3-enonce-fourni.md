# TD 3 : DPLL et Tseitin — énoncé fourni

> 📄 **Énoncé officiel** distribué en TD (Logique, Licence Informatique / Double Licence, 2026-2027).
> ✅ Correction : [TD3-correction.md](TD3-correction.md) · 📝 Mon travail : [mes-reponses-TD3.md](mes-reponses-TD3.md)
> 📚 Cours : [Ch. 8 Tseitin](../../01-Cours/02-SAT/8-Tseitin.md) · [Ch. 9 DPLL](../../01-Cours/02-SAT/9-DPLL.md)

> ⚠️ Les feuilles de TD sont volontairement longues. Les exercices non faits en classe sont à faire pour préparer l'examen.

---

## Exercice 1 : DPLL

Déterminez si ces formules sont satisfiables à l'aide de l'algorithme DPLL.

- **Q 1.1** `φ₁ = p ∧ q ∧ r`
- **Q 1.2** `φ₂ = (q ∨ ¬p) ∧ ¬q ∧ p ∧ (r ∨ ¬p)`
- **Q 1.3** `φ₃ = (q ∨ p) ∧ (r ∨ q) ∧ ¬r ∧ ¬q`
- **Q 1.4** `φ₄ = p ∧ q ∧ (q ∨ ¬p) ∧ r`
- **Q 1.5** `φ₅ = (q ∨ p) ∧ ¬q`
- **Q 1.6** `φ₆ = (q ∨ p) ∧ (q ∨ ¬p) ∧ (¬r ∨ ¬q) ∧ (r ∨ ¬q)`
- **Q 1.7** `φ₇ = (¬p ∨ t) ∧ (p ∨ ¬r) ∧ (q ∨ r) ∧ (¬q ∨ s)`

## Exercice 2 : Encore DPLL

Trouvez si possible une valuation qui satisfait les formules suivantes avec l'algorithme DPLL. Mettez les formules sous forme normale conjonctive si nécessaire.

- **Q 2.1** `(a ∨ b ∧ ¬c) ⇔ (a ∧ (c ∨ ¬b))`
- **Q 2.2** `(((b ⇒ ¬c) ∧ (d ⇒ e)) ∨ a) ∧ (c ∨ ((a ⇒ ¬f) ∧ (¬b ⇒ f))) ∧ (b ∨ d ∨ ¬e)`

## Exercice 3 : Transformation de Tseitin

- **Q 3.1** Convertir `(p ∧ q) ⇒ r` en FNC équisatisfiable avec la transformation de Tseitin.
- **Q 3.2** Convertir `(p ∨ q) ⇒ (p ∧ ¬r)` en FNC équisatisfiable avec la transformation de Tseitin.
- **Q 3.3** Convertir `¬(p ∨ (q ⇒ r)) ∨ s` en FNC équisatisfiable avec la transformation de Tseitin.
