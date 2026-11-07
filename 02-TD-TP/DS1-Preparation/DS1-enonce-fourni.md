# Préparation au DS1 — énoncé fourni

> 📄 **Feuille officielle** de préparation au DS1 (Logique, Licence Informatique, 2026-2027) : exercices tirés d'anciens DS.
> ✅ Correction : [DS1-correction.md](DS1-correction.md) · 📝 Mon travail : [mes-reponses-DS1.md](mes-reponses-DS1.md)
> 📚 Cours : [Ch. 2 Sémantique](../../01-Cours/01-Logique-propositionnelle/2-Semantique.md) · [Ch. 4 Formes normales](../../01-Cours/01-Logique-propositionnelle/4-Formes-normales.md) · [Ch. 6 Modéliser avec SAT](../../01-Cours/02-SAT/6-Modeliser-avec-SAT.md)

> **Conseils de l'enseignante** : réviser les slides du CM, les exercices de préparation des TD et les DM. Refaire **tous** les exercices des TD, en particulier ceux non terminés en séance.
> ⚠️ Un type d'exercice absent de cette feuille peut quand même tomber au DS : le programme évolue chaque année.

---

## Exercice 1 : Tables de vérité

Construire les tables de vérité des formules suivantes :

- **Q 1.1** `(a ⇔ b) ⇒ (a ∧ b)`
- **Q 1.2** `(¬c ∧ b) ∨ (b ⇒ (a ∧ c))`
- **Q 1.3** `(¬a ∨ ¬b ∨ c) ∧ ((a ∨ c) ⇒ (b ∧ ¬c))`
- **Q 1.4** `((a ∨ ¬b) ⇒ (b ∧ c)) ⇔ ((¬a ∧ c) ∨ (b ∧ a))`
- **Q 1.5** `((a ∨ b) ⇒ c) ⇔ (¬a ∧ (b ∨ c))`
- **Q 1.6** `(x ∧ y) ⇒ ((z ∨ ¬x) ∧ (y ∨ ¬z ∨ x))`

---

## Exercice 2 : Modélisation en logique propositionnelle — les voyages d'Assia

Assia, facétieuse et grande voyageuse, vous propose de deviner les pays qu'elle a visités :

1. J'ai visité au moins un des trois pays suivants : la Colombie, le Kenya et la Malaisie.
2. Si j'ai visité la Colombie ou si je n'ai pas visité le Kenya, alors j'ai visité la Malaisie.
3. Si j'ai été au Kenya et en Malaisie, alors je n'ai pas été en Colombie.
4. Si j'ai été en Malaisie, alors j'ai visité un seul et un seul autre pays (parmi le Kenya et la Colombie).
5. Si je n'ai pas été en Colombie, alors je n'ai pas été au Kenya.

- **Q 2.1** Indiquez les variables propositionnelles utilisées et leur signification.
- **Q 2.2** Modélisez chaque phrase d'Assia par une formule.
- **Q 2.3** Trouvez les pays qu'Assia a visités.

---

## Exercice 3 : Modélisation en logique propositionnelle — Colombo

Alice et Bob sont arrêtés par Colombo pour le vol d'un ordinateur et d'un téléphone portable. Chaque vol a été commis par **un seul** des deux. L'un des deux dit **toujours la vérité**, l'autre **ment toujours**, mais Colombo ne sait plus qui est qui.

Variables :

- `a` vraie ssi **Alice** ment tout le temps (fausse ssi c'est Bob) ;
- `o` vraie ssi **Alice** a volé l'ordinateur (fausse ssi c'est Bob) ;
- `t` vraie ssi **Alice** a volé le téléphone (fausse ssi c'est Bob).

> Alice déclare : *« Bob ment et je n'ai rien volé. »*
> Bob déclare : *« Celui qui ment a commis tous les vols. »*

- **Q 3.1** Traduisez la déclaration d'Alice en une formule `A`.
- **Q 3.2** Traduisez la déclaration de Bob en une formule `B`.
- **Q 3.3** Avec `a`, `A` et `B`, modélisez le fait que ce que dit le menteur est faux et que l'autre dit la vérité.
- **Q 3.4** Aidez Colombo à établir les faits, avec des justifications solides.

---

## Exercice 4 : SAT — Puzzle

On dispose de pièces **carrées** dont les bords sont **colorés** et marqués N (nord), S (sud), E (est), O (ouest). Il faut placer les `n²` pièces sur une grille `n × n` (une et une seule pièce par case) de façon que les bords qui se touchent aient **la même couleur** :

- la pièce au **nord** d'une autre a son bord **sud** de la même couleur que le bord **nord** de sa voisine ;
- la pièce à l'**ouest** d'une autre a son bord **est** de la même couleur que le bord **ouest** de sa voisine ;
- etc.

**Conventions**

- les cases sont notées `(i, j)` avec `i, j ∈ [1, n]` ; la case `(1, 1)` est en **bas à gauche** (sud-ouest) ;
- `(i + 1, j)` est juste à l'**est** de `(i, j)` ; `(i, j + 1)` est juste au **nord** de `(i, j)` ;
- les pièces sont numérotées de 1 à `n²` ; `P` est l'ensemble des pièces, `C` l'ensemble des cases ;
- **SN** : paires `(p₁, p₂)`, `p₁ ≠ p₂`, telles que le bord **sud** de `p₁` a la couleur du bord **nord** de `p₂` ;
- **NS** : paires telles que le bord **nord** de `p₁` a la couleur du bord **sud** de `p₂` ;
- **EO** : paires telles que le bord **est** de `p₁` a la couleur du bord **ouest** de `p₂` ;
- **OE** : paires telles que le bord **ouest** de `p₁` a la couleur du bord **est** de `p₂`.

**Exemple** (`n = 2`, bords noirs ⬛ ou blancs ⬜) :

| Pièce | Nord | Sud | Est | Ouest |
|:-:|:-:|:-:|:-:|:-:|
| 1 | ⬛ | ⬛ | ⬛ | ⬛ |
| 2 | ⬜ | ⬜ | ⬜ | ⬛ |
| 3 | ⬛ | ⬜ | ⬜ | ⬜ |
| 4 | ⬜ | ⬜ | ⬜ | ⬜ |

- SN = {(1, 3), (2, 4), (3, 2), (3, 4), (4, 2)}
- NS = {(2, 3), (3, 1), (4, 2), (4, 3)} *(la paire (2, 4) manque sur la feuille : voir la correction)*
- EO = {(1, 2), (2, 3), (2, 4), (3, 4), (4, 3)}
- OE = {(2, 1), (3, 2), (3, 4), (4, 2), (4, 3)}

La seule solution est :

| | colonne `i = 1` | colonne `i = 2` |
|:-:|:-:|:-:|
| **ligne `j = 2`** (nord) | pièce 1 | pièce 2 |
| **ligne `j = 1`** (sud) | pièce 3 | pièce 4 |

- **Q 4.1** Identifiez les variables et leur signification.
- **Q 4.2** FNC : chaque pièce occupe **une et une seule** case.
- **Q 4.3** FNC : chaque case est occupée par **une et une seule** pièce.
- **Q 4.4** FNC : chaque pièce a son bord **nord** de la même couleur que le bord **sud** de la pièce à son nord.
- **Q 4.5** FNC : chaque pièce a son bord **est** de la même couleur que le bord **ouest** de la pièce à son est.
- **Q 4.6** Faut-il aussi exprimer la contrainte « bord **sud** = bord **nord** de la pièce au sud » ? Pourquoi ?

---

## Exercice 5 : Modélisation SAT — la tournée du facteur

La poste veut trouver, pour chaque quartier, un itinéraire qui part de la poste et fait passer le facteur **une et une seule fois** dans chaque rue.

- Les carrefours sont numérotés de 1 à `n` ; la poste est au carrefour **1**.
- `T` est l'ensemble des **trajets** `(i, j)` (emprunter la rue entre `i` et `j`, de `i` vers `j`). Les rues sont à double sens : si `(i, j) ∈ T` alors `(j, i) ∈ T`.
- `m = |T| / 2` est le nombre de rues : la tournée comporte `m` trajets.
- Variables : `x_{(i,j),k}` pour `(i, j) ∈ T` et `k ∈ [1, m]`, vraie ssi **le `k`-ième trajet du facteur va du carrefour `i` au carrefour `j`**.

Toutes les contraintes sont à donner **en FNC**.

- **Q 5.1** Chaque rue est empruntée au moins une fois, dans au moins une direction.
- **Q 5.2** Chaque trajet est emprunté au plus une fois.
- **Q 5.3** Chaque rue est empruntée dans au plus une direction.
- **Q 5.4** Pour chaque `k ∈ [1, m]`, il y a au moins un `k`-ième trajet.
- **Q 5.5** Le premier trajet part de la poste (carrefour 1).
- **Q 5.6** Le dernier trajet (le `m`-ième) arrive à la poste.
- **Q 5.7** Si le `k`-ième trajet arrive au carrefour `j`, alors le `(k + 1)`-ième trajet part du carrefour `j`.

---

## Exercice 6 : Mise sous forme normale conjonctive

- **Q 6.1** `(((b ⇒ ¬c) ∧ (d ⇒ e)) ∨ a) ∧ (c ∨ ((a ⇒ ¬f) ∧ (¬b ⇒ f))) ∧ (b ∨ d ∨ ¬e)`
- **Q 6.2** `(a ∨ b ∧ ¬c) ⇔ (a ∧ (c ∨ ¬b))`

## Exercice 7 : Mise sous forme normale conjonctive (avec les étapes)

- **Q 7.1** `(a ∧ b) ⇔ (c ∨ d)`
- **Q 7.2** `((a ∧ b) ⇒ (c ∧ d)) ∨ (a ∧ ¬d)`
