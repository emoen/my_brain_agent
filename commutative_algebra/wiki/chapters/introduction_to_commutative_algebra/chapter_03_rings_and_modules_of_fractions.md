        ---
        title: "Ch 3: Rings and Modules of Fractions"
        book: "introduction to commutative algebra"
        source: "introduction_to_commutative_algebra.pdf"
        pages: "46–59"
        chapter: 3
        type: chapter-summary
        status: auto-generated
        model: gpt-4o
        date: 2026-06-12
        tags: [knowledge-base, auto-ingested, chapter-note]
        ---

        # Chapter 3: Rings and Modules of Fractions

        > *Auto-generated rich summary — introduction to commutative algebra*
        > *Pages 46–59 | Ingested 2026-06-12*

        # Rings and Modules of Fractions (Chapter 3)

This article provides a detailed summary of Chapter 3 ("Rings and Modules of Fractions") from *Introduction to Commutative Algebra* by M. Atiyah and I.G. Macdonald. The chapter introduces the construction and properties of rings and modules of fractions, localization, and related concepts such as flatness, extended and contracted ideals, and the support of modules. These tools are foundational in commutative algebra and algebraic geometry, enabling the study of rings and modules "locally" and facilitating the analysis of their structure.

---

## Overview

Chapter 3 focuses on the process of **localization**, which allows us to "zoom in" on specific parts of a ring or module by inverting a multiplicatively closed subset of the ring. This technique generalizes the construction of the field of fractions for integral domains and is a cornerstone in commutative algebra. Localization is essential for studying local properties of rings and modules, such as flatness, and for constructing local rings and modules.

The chapter also explores the interplay between localization and various algebraic operations, such as sums, intersections, and quotients of ideals and modules. It introduces the notions of extended and contracted ideals, the support of a module, and the concept of faithfully flat modules, all of which are crucial in algebraic geometry and homological algebra. The chapter concludes by establishing the local nature of key properties like flatness and injectivity, and by exploring the behavior of prime ideals under localization.

---

## Definitions & Notation

### Rings and Modules of Fractions
- **Integral Domain**: A commutative ring $A$ with no zero divisors.
- **Field of Fractions**: For an integral domain $A$, the field of fractions is constructed as equivalence classes of pairs $(a, s)$ with $a, s \in A$ and $s \neq 0$, where $(a, s) \sim (b, t)$ if $at = bs$.
- **Multiplicatively Closed Subset**: A subset $S \subseteq A$ such that $1 \in S$ and $S$ is closed under multiplication.
- **Ring of Fractions**: For a ring $A$ and a multiplicatively closed subset $S$, the ring of fractions $S^{-1}A$ is formed by equivalence classes of pairs $(a, s)$ under the relation $(a, s) \sim (b, t)$ if $(at - bs)u = 0$ for some $u \in S$.
- **Localization**: The process of forming $S^{-1}A$. If $S = A \setminus \mathfrak{p}$, where $\mathfrak{p}$ is a prime ideal, then $S^{-1}A$ is denoted $A_{\mathfrak{p}}$ and is called the **localization at $\mathfrak{p}$**.
- **Module of Fractions**: For an $A$-module $M$, the module of fractions $S^{-1}M$ consists of equivalence classes of pairs $(m, s)$ under the relation $(m, s) \sim (m', s')$ if $t(sm' - s'm) = 0$ for some $t \in S$.

### Extended and Contracted Ideals
- **Extended Ideal**: For an ideal $a \subseteq A$, the extension $a^e$ in $S^{-1}A$ is defined as $S^{-1}a = \{a/s \mid a \in a, s \in S\}$.
- **Contracted Ideal**: For an ideal $b \subseteq S^{-1}A$, the contraction $b^c$ in $A$ is $b^c = \{x \in A \mid x/s \in b \text{ for some } s \in S\}$.

### Flatness
- **Flat Module**: An $A$-module $M$ is flat if the functor $- \otimes_A M$ is exact, i.e., it preserves the exactness of sequences.
- **Faithfully Flat Module**: An $A$-module $M$ is faithfully flat if $M \neq 0$ and $N \otimes_A M \neq 0$ for all nonzero $A$-modules $N$.

### Support of a Module
- **Support**: The support of an $A$-module $M$ is $\text{Supp}(M) = \{\mathfrak{p} \in \text{Spec}(A) \mid M_{\mathfrak{p}} \neq 0\}$.

---

## Theorems, Lemmas & Corollaries

### Proposition 3.1: Universal Property of Localization
**Statement**: Let $g: A \to B$ be a ring homomorphism such that $g(s)$ is a unit in $B$ for all $s \in S$. Then there exists a unique ring homomorphism $h: S^{-1}A \to B$ such that $g = h \circ f$, where $f: A \to S^{-1}A$ is the natural map defined by $f(a) = a/1$.

---

### Proposition 3.3: Exactness of Localization
**Statement**: The localization functor $S^{-1}$ is exact. If $M' \to M \to M''$ is exact at $M$, then $S^{-1}M' \to S^{-1}M \to S^{-1}M''$ is exact at $S^{-1}M$.

---

### Proposition 3.5: Tensor Product and Localization
**Statement**: Let $M$ be an $A$-module. Then the $S^{-1}A$-modules $S^{-1}M$ and $S^{-1}A \otimes_A M$ are isomorphic. Specifically, there exists a unique isomorphism $f: S^{-1}A \otimes_A M \to S^{-1}M$ such that $f((a/s) \otimes m) = am/s$ for all $a \in A$, $m \in M$, $s \in S$.

---

### Proposition 3.8: Localization and Zero Modules
**Statement**: Let $M$ be an $A$-module. Then the following are equivalent:
1. $M = 0$,
2. $M_{\mathfrak{p}} = 0$ for all prime ideals $\mathfrak{p}$ of $A$,
3. $M_m = 0$ for all maximal ideals $m$ of $A$.

---

### Proposition 3.10: Flatness is Local
**Statement**: For any $A$-module $M$, the following are equivalent:
1. $M$ is a flat $A$-module,
2. $M_{\mathfrak{p}}$ is a flat $A_{\mathfrak{p}}$-module for each prime ideal $\mathfrak{p}$,
3. $M_m$ is a flat $A_m$-module for each maximal ideal $m$.

---

## Proof Ideas

### Proposition 3.1
The proof constructs $h$ by defining $h(a/s) = g(a)g(s)^{-1}$ and verifies that $h$ is well-defined, respects the equivalence relation, and satisfies $g = h \circ f$.

---

## Worked Examples & Constructions

### Example: Localization at a Prime Ideal
Let $\mathfrak{p}$ be a prime ideal of $A$. Then $S = A \setminus \mathfrak{p}$ is multiplicatively closed, and $A_{\mathfrak{p}} = S^{-1}A$. The ring $A_{\mathfrak{p}}$ is a local ring with $\mathfrak{p}A_{\mathfrak{p}}$ as its unique maximal ideal.

---

## Exercises (Selected)

1. **Exactness of Localization**: Prove that if $M' \to M \to M''$ is exact, then $S^{-1}M' \to S^{-1}M \to S^{-1}M''$ is exact.
2. **Flatness and Localization**: Prove that $S^{-1}A$ is a flat $A$-module.
3. **Support of Modules**: Show that $\text{Supp}(M)$ is a closed subset of $\text{Spec}(A)$ if $M$ is finitely generated.

---

## Key Insights

1. Localization allows us to focus on specific parts of a ring or module by inverting a multiplicatively closed subset.
2. The universal property of localization ensures compatibility with ring homomorphisms.
3. Localization preserves exact sequences, making it a powerful tool for studying modules.
4. Flatness is a local property and can be checked at prime or maximal ideals.
5. The support of a module is a geometric tool that connects module theory with the spectrum of a ring.

---

## Connections & Backlinks

- [[Chapter 1: Rings and Ideals]]: Definitions of ideals and prime ideals.
- [[Chapter 2: Modules]]: Tensor products and flatness.
- [[Chapter 4: Primary Decomposition]]: Applications of localization to primary decomposition.

---

## Further Reading

- Eisenbud, D. *Commutative Algebra with a View Toward Algebraic Geometry*.
- Matsumura, H. *Commutative Ring Theory*.

        ---
        *Generated by `ingest_chapters.py` · model: gpt-4o*
