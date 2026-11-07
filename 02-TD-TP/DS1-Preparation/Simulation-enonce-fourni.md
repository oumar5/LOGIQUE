# Simulation d'examen — énoncé fourni

> 📄 **Sujet officiel** de simulation (Logique, Licence Informatique, 2026-2027), à faire avant le TD de la semaine du 2 novembre.
> ✅ Correction : [Simulation-correction.md](Simulation-correction.md) · 📝 Mon travail : [mes-reponses-Simulation.md](mes-reponses-Simulation.md)

> ⏱️ **Conditions d'examen** : 2 heures maximum, **aucun document**, sans aide, sans ordinateur ni téléphone.
> Seul le tableau des lois de la fin du sujet est fourni (« matériel supplémentaire »).

---

## Exercice 1 : Tables de vérité

**Q 1.1** Table de vérité de `¬(P ∧ Q) ∨ ((R → (P ∨ ¬Q)) ∧ ((¬R ∨ Q) ↔ (P → ¬Q)))` (avec les colonnes `P, Q, R` dans l'ordre `000` à `111`).

**Q 1.2** Table de vérité de `((A ∧ ¬B) ∨ (¬C ∧ D)) ∧ ((¬A ∨ C) ∨ (B ∧ ¬D))` (avec les colonnes `A, B, C, D` dans l'ordre `0000` à `1111`).

> `→` et `↔` sont d'autres notations pour `⇒` et `⇔`.

---

## Exercice 2 : Que fait Mario dans la vie ?

Mario est un ami d'amis. Trois personnes nous ont donné ces informations :

- Mario est architecte ou géomètre ;
- si Mario était architecte, alors il serait titulaire d'un diplôme universitaire ;
- Mario n'est pas diplômé du supérieur.

On ne sait pas combien ni lesquelles de ces personnes disent la vérité.

**Q 2.1** Écrivez les affirmations avec des formules (en décrivant vos variables). Est-il possible que tout le monde dise la vérité ? Si oui, que fait Mario dans la vie ?

---

## Exercice 3 : Les `n` reines

Sur un échiquier `n × n`, placer `n` reines sans qu'aucune n'en attaque une autre : deux reines s'attaquent si elles sont sur la même **ligne**, la même **colonne** ou la même **diagonale**. Lignes et colonnes sont numérotées de 1 à `n`.

Variable : `x_{i,j}` vraie ssi **il y a une reine sur la case `(i, j)`**. La case `(1, 1)` est en **haut à gauche** (`i` = ligne, `j` = colonne).

**Figure 1** — une solution pour `n = 5` :

| | 1 | 2 | 3 | 4 | 5 |
|:-:|:-:|:-:|:-:|:-:|:-:|
| **1** | | | | ♛ | |
| **2** | | ♛ | | | |
| **3** | | | | | ♛ |
| **4** | | | ♛ | | |
| **5** | ♛ | | | | |

- **Q 3.1** Donnez la valuation des variables pour la solution de la Figure 1.
- **Q 3.2** Exprimez la contrainte : chaque **ligne** contient **exactement une** reine.
- **Q 3.3** Exprimez la contrainte : chaque **colonne** contient **exactement une** reine.
- **Q 3.4** Exprimez la contrainte : **au plus une reine par diagonale**. Il y a deux types de diagonales : les **décroissantes** (la **différence** `i − j` est constante) et les **croissantes** (la **somme** `i + j` est constante).
- **Q 3.5** Faut-il ajouter une contrainte disant que chaque case contient au plus une reine ? Argumentez.

---

## Exercice 4 : Formes normales (sans table de vérité)

- **Q 4.1** Réécrivez `a ⇔ ((b ∧ ¬a) ∨ c)` en **FNC** et en **FND**, en expliquant chaque étape.
- **Q 4.2** Mettez `((q ∧ (s ⇒ f)) ∨ (¬s ∧ g)) ⇒ (q ∨ (¬f ∧ ¬g))` sous **FNC**, en expliquant chaque étape.

---

## Matériel supplémentaire (fourni le jour de l'examen)

| Loi | |
|---|---|
| Commutativité | `φ ∨ ψ ≡ ψ ∨ φ`, `φ ∧ ψ ≡ ψ ∧ φ` |
| Associativité | `(φ ∨ ψ) ∨ θ ≡ φ ∨ (ψ ∨ θ)`, `(φ ∧ ψ) ∧ θ ≡ φ ∧ (ψ ∧ θ)` |
| Distributivité | `φ ∨ (ψ ∧ θ) ≡ (φ ∨ ψ) ∧ (φ ∨ θ)`, `φ ∧ (ψ ∨ θ) ≡ (φ ∧ ψ) ∨ (φ ∧ θ)` |
| Identité | `φ ∨ ⊥ ≡ φ`, `φ ∧ ⊤ ≡ φ` |
| Zéro | `φ ∨ ⊤ ≡ ⊤`, `φ ∧ ⊥ ≡ ⊥` |
| Idempotence | `φ ∨ φ ≡ φ`, `φ ∧ φ ≡ φ` |
| Absorption | `φ ∨ (φ ∧ ψ) ≡ φ`, `φ ∧ (φ ∨ ψ) ≡ φ` |
| Complémentation | `φ ∨ ¬φ ≡ ⊤`, `φ ∧ ¬φ ≡ ⊥` |
| Double négation | `¬¬φ ≡ φ` |
| De Morgan | `¬(φ ∨ ψ) ≡ ¬φ ∧ ¬ψ`, `¬(φ ∧ ψ) ≡ ¬φ ∨ ¬ψ` |
| Définition | `φ ⇒ ψ ≡ ¬φ ∨ ψ`, `φ ⇔ ψ ≡ (φ ⇒ ψ) ∧ (ψ ⇒ φ)` |
