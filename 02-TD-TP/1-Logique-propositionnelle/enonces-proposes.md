# Partie 1 — Logique propositionnelle : énoncés proposés

> Exercices **que je t'ai préparés** pour t'entraîner sur les chapitres 1 à 4. Ils vont du plus simple au plus difficile.
> ✅ La correction est dans un fichier à part : [corrections-proposes.md](corrections-proposes.md). Essaie d'abord seule !
>
> Cours : [Ch. 1 Syntaxe](../../01-Cours/01-Logique-propositionnelle/1-Syntaxe.md) · [Ch. 2 Sémantique](../../01-Cours/01-Logique-propositionnelle/2-Semantique.md) · [Ch. 3 Équivalences](../../01-Cours/01-Logique-propositionnelle/3-Equivalences.md) · [Ch. 4 Formes normales](../../01-Cours/01-Logique-propositionnelle/4-Formes-normales.md)

---

## Partie A — Syntaxe

### A1. Traduire des phrases ⭐

Choisis tes variables (en écrivant ce qu'elles signifient) et traduis :

1. « S'il y a une grève, je prends le vélo ou je marche. »
2. « Je ne vais au cinéma **que si** j'ai fini mes devoirs. »
3. « Je sors ce soir si Léa sort et que je n'ai pas de DS demain. »
4. « Ni Paul ni Marie ne sont venus. »

### A2. Ajouter les parenthèses ⭐

Réécris chaque formule avec toutes ses parenthèses :

1. `¬p ∨ q ∧ r ⇒ s`
2. `a ∧ b ∨ ¬c ∧ d`
3. `p ⇒ q ⇒ r ∧ s`

### A3. Arbre, variables, hauteur ⭐

Pour `(a ⇒ b) ∧ ¬c` puis pour `¬¬(p ∨ (q ∧ ¬r))` :
dessine l'arbre, puis calcule `Var` et `h`.

### A4. Substitution ⭐⭐

Calcule `subst(φ, σ)` pour `φ = (a ⇒ b) ∨ ¬a`, avec `σ(a) = b ∧ c` et `σ(b) = ¬a`.

### A5. Une nouvelle fonction récursive ⭐⭐

Définis cas par cas la fonction `nc(φ)` qui compte le **nombre de connecteurs** d'une formule, puis calcule `nc(r ⇒ (¬b ∨ c))`.

---

## Partie B — Sémantique

### B1. Évaluer ⭐

Avec `a = 0` et `b = 1`, que vaut `¬a ⇒ (a ∧ b)` ?

### B2. La promesse ⭐

Un parent dit : « Si tu ranges ta chambre, tu auras ton argent de poche. »
Avec `r` = tu ranges, `g` = tu as l'argent : dans quelle(s) situation(s) le parent **a-t-il menti** ?

### B3. Table de vérité ⭐

Fais la table de vérité de `(p ⇒ q) ∧ (q ⇒ p)` et compare-la avec celle de `p ⇔ q`.

### B4. Table de vérité à 3 variables ⭐⭐

Fais la table de vérité de `(a ∨ b) ⇒ (a ∧ c)`. Est-elle satisfiable ? Est-ce une tautologie ?

### B5. Classer ⭐⭐

Pour chaque formule, dis si c'est une tautologie, une formule satisfiable (mais pas tautologie) ou une formule insatisfiable :

1. `p ∨ ¬p`
2. `p ∧ ¬p`
3. `(p ⇒ q) ∨ (q ⇒ p)`
4. `p ⇒ q`
5. `(p ∧ q) ∧ ¬(p ∨ q)`

### B6. Raisonnements corrects ou non ? ⭐⭐

1. *« S'il pleut, la route est mouillée. Si la route est mouillée, je glisse. Donc s'il pleut, je glisse. »*
   Est-ce que `p ⇒ m, m ⇒ g ⊨ p ⇒ g` ?
2. *« S'il pleut, la route est mouillée. La route est mouillée. Donc il pleut. »*
   Est-ce que `p ⇒ m, m ⊨ p` ?

### B7. L'île des chevaliers et des menteurs ⭐⭐⭐

Sur une île, les **chevaliers** disent toujours la vérité et les **menteurs** mentent toujours.

- A dit : « B est un menteur. »
- B dit : « A et moi sommes du même type. »

Avec `a` = « A est chevalier » et `b` = « B est chevalier », traduis la situation en formule et trouve qui est quoi.

> 💡 Indice : si A est chevalier, ce qu'il dit est vrai ; s'il est menteur, c'est faux. Donc « A dit X » se traduit par `a ⇔ X`.

---

## Partie C — Équivalences

### C1. Simplifier ⭐

1. `¬(¬a ∨ b)`
2. `a ∨ (a ∧ b)`
3. `(a ∧ b) ∨ (a ∧ ¬b)`

### C2. Nier en français ⭐

Écris la négation de chaque phrase (avec De Morgan) :

1. « Il pleut et il fait froid. »
2. « Je prends le bus ou le tram. »
3. « Si tu travailles, tu réussis. »

### C3. Contraposée et réciproque ⭐

« Si je suis à Lille, alors je suis en France. »
Écris sa contraposée et sa réciproque. Laquelle est toujours vraie ?

### C4. Prouver une équivalence par le calcul ⭐⭐

Montre que `(a ⇒ b) ∧ (a ⇒ c) ≡ a ⇒ (b ∧ c)` en nommant la loi utilisée à chaque ligne.

### C5. Systèmes complets ⭐⭐

1. Écris `a ∨ b` avec seulement `¬` et `∧`.
2. Écris `a ∧ b` avec seulement `¬` et `⇒`.
3. Écris `¬a`, puis `a ∨ b`, avec seulement `⇒` et `⊥`.

---

## Partie D — Formes normales

### D1. Échauffement ⭐

1. FNC de `p ⇒ (q ∧ r)`
2. FND de `(p ∨ q) ∧ r`

### D2. À l'entrée de la boîte de nuit ⭐

Pour entrer : il faut être majeur (`m`), **et** avoir une pièce d'identité (`i`) **ou** une carte étudiante (`e`), **et** ne pas être en survêtement (`s`).
Écris la règle en FNC, puis en FND.

### D3. Par la table de vérité ⭐⭐

Donne la FND et la FNC de `a ⇔ b` à partir de sa table de vérité.

### D4. « Exactement un » ⭐⭐

1. Donne la FND de « exactement un parmi `a`, `b`, `c` » (par la table).
2. Donne sa FNC par la table.
3. Montre que la FNC peut se simplifier en `(a ∨ b ∨ c) ∧ (¬a ∨ ¬b) ∧ (¬a ∨ ¬c) ∧ (¬b ∨ ¬c)`. Où reverras-tu cette forme ?

### D5. Par le calcul ⭐⭐

1. FNC de `¬(a ∧ (b ∨ ¬c))`
2. FNC de `(a ⇔ b) ∨ c`
