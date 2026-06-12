        ---
        title: "Ch 4: Primary Decomposition"
        book: "introduction to commutative algebra"
        source: "introduction_to_commutative_algebra.pdf"
        pages: "60–68"
        chapter: 4
        type: chapter-summary
        status: auto-generated
        model: gpt-4o
        date: 2026-06-12
        tags: [knowledge-base, auto-ingested, chapter-note]
        ---

        # Chapter 4: Primary Decomposition

        > *Auto-generated rich summary — introduction to commutative algebra*
        > *Pages 60–68 | Ingested 2026-06-12*

        # Primary Decomposition: Chapter 4 Summary

## Overview

Chapter 4 of *Introduction to Commutative Algebra* by Atiyah and Macdonald delves into the theory of primary decomposition, a cornerstone of commutative algebra. This chapter provides a rigorous framework for decomposing ideals in Noetherian rings into intersections of primary ideals. The material is deeply connected to algebraic geometry, where primary decomposition corresponds to the decomposition of algebraic varieties into irreducible components, and to number theory, where it generalizes the notion of prime factorization to higher dimensions.

The chapter introduces key concepts such as primary ideals, $\mathfrak{p}$-primary ideals, and associated prime ideals. It also establishes the existence and uniqueness of minimal primary decompositions, providing tools to analyze the structure of ideals and their associated prime ideals. The chapter emphasizes the interplay between algebraic and geometric perspectives, illustrating how primary decomposition captures the "building blocks" of ideals and their geometric counterparts. The results are extended to modules and localized rings, further demonstrating the versatility and depth of the theory.

---

## Definitions & Notation

### Primary Ideal
- An ideal $q$ in a ring $A$ is **primary** if:
  1. $q \neq A$, and
  2. For any $x, y \in A$, $xy \in q$ implies either $x \in q$ or $y^n \in q$ for some $n > 0$.
- Equivalently, $q$ is primary if $A/q \neq 0$ and every zero-divisor in $A/q$ is nilpotent.
- **Radical of an Ideal**: $\operatorname{rad}(q) = \{x \in A : x^n \in q \text{ for some } n > 0\}$, the smallest prime ideal containing $q$.

### $\mathfrak{p}$-Primary Ideal
- An ideal $q$ is **$\mathfrak{p}$-primary** if $\operatorname{rad}(q) = \mathfrak{p}$.

### Primary Decomposition
- A **primary decomposition** of an ideal $a$ in $A$ is an expression:

$$
a = \bigcap_{i=1}^n q_i,
$$

  where each $q_i$ is a primary ideal.
- A **minimal primary decomposition** satisfies:
  1. The radicals $\operatorname{rad}(q_i)$ are distinct.
  2. $q_i \neq \bigcap_{j \neq i} q_j$ for all $i$.

### Associated Prime Ideals
- The prime ideals $\mathfrak{p}_i = \operatorname{rad}(q_i)$ in a minimal primary decomposition are called **associated prime ideals** of $a$.
- **Minimal Prime Ideals**: The minimal elements of the set of associated primes.
- **Embedded Prime Ideals**: Non-minimal associated primes.

### Zero-Divisors and Nilpotent Elements
- The set of **zero-divisors** of $A$ is the union of all prime ideals associated with the zero ideal.
- The set of **nilpotent elements** of $A$ is the intersection of all minimal prime ideals associated with the zero ideal.

### Localization and Primary Ideals
- If $S$ is a multiplicatively closed subset of $A$, the contraction of an ideal $s^{-1}a$ in $A$ is denoted by $S(a)$.
- Primary ideals correspond to primary ideals under localization.

---

## Theorems, Lemmas & Corollaries

### Proposition 4.1
**Statement**: Let $q$ be a primary ideal in a ring $A$. Then $\operatorname{rad}(q)$ is the smallest prime ideal containing $q$.

---

### Proposition 4.2
**Statement**: If $\operatorname{rad}(a)$ is maximal, then $a$ is primary. In particular, the powers of a maximal ideal $m$ are $m$-primary.

---

### Lemma 4.3
**Statement**: If $q_i$ ($1 \leq i \leq n$) are $\mathfrak{p}$-primary, then $q = \bigcap_{i=1}^n q_i$ is $\mathfrak{p}$-primary.

---

### Lemma 4.4
**Statement**: Let $q$ be a $\mathfrak{p}$-primary ideal and $x \in A$. Then:
1. If $x \in q$, then $(q : x) = (1)$.
2. If $x \not\in q$, then $(q : x)$ is $\mathfrak{p}$-primary, and $\operatorname{rad}(q : x) = \mathfrak{p}$.
3. If $x \not\in \mathfrak{p}$, then $(q : x) = q$.

---

### Theorem 4.5 (1st Uniqueness Theorem)
**Statement**: Let $a$ be a decomposable ideal with a minimal primary decomposition $a = \bigcap_{i=1}^n q_i$. Let $\mathfrak{p}_i = \operatorname{rad}(q_i)$ ($1 \leq i \leq n$). Then the $\mathfrak{p}_i$ are precisely the prime ideals that occur in the set of radicals $\operatorname{rad}(a : x)$ ($x \in A$), and are independent of the particular decomposition of $a$.

---

### Proposition 4.6
**Statement**: Let $a$ be a decomposable ideal. Then any prime ideal $\mathfrak{p} \supseteq a$ contains a minimal prime ideal belonging to $a$. Hence, the minimal prime ideals of $a$ are precisely the minimal elements in the set of all prime ideals containing $a$.

---

### Proposition 4.7
**Statement**: Let $a$ be a decomposable ideal with a minimal primary decomposition $a = \bigcap_{i=1}^n q_i$, and let $\mathfrak{p}_i = \operatorname{rad}(q_i)$. Then:

$$
\bigcup_{i=1}^n \mathfrak{p}_i = \{x \in A : (a : x) \neq a\}.
$$

In particular, if the zero ideal is decomposable, the set $D$ of zero-divisors of $A$ is the union of the prime ideals belonging to $0$.

---

### Theorem 4.10 (2nd Uniqueness Theorem)
**Statement**: Let $a$ be a decomposable ideal with a minimal primary decomposition $a = \bigcap_{i=1}^n q_i$, and let $\{\mathfrak{p}_1, \dots, \mathfrak{p}_m\}$ be an isolated set of prime ideals belonging to $a$. Then $q_1 \cap \cdots \cap q_m$ is independent of the decomposition.

---

### Corollary 4.11
**Statement**: The isolated primary components (i.e., the primary components $q_i$ corresponding to minimal prime ideals $\mathfrak{p}_i$) are uniquely determined by $a$.

---

## Proof Ideas

- **Proposition 4.1**: Follows from the definition of $\operatorname{rad}(q)$ and the property that $xy \in \operatorname{rad}(q)$ implies $x \in \operatorname{rad}(q)$ or $y \in \operatorname{rad}(q)$.
- **Proposition 4.2**: Relies on the fact that $A/a$ has only one prime ideal when $\operatorname{rad}(a)$ is maximal.
- **Lemma 4.3**: Uses the equality $\operatorname{rad}(q) = \mathfrak{p}$ and properties of intersections of primary ideals.
- **Theorem 4.5**: Combines Lemma 4.4 and the fact that $\operatorname{rad}(a : x)$ is prime if and only if it equals $\mathfrak{p}_i$ for some $i$.
- **Theorem 4.10**: Uses saturation $S(a)$ to isolate primary components corresponding to specific prime ideals.

---

## Worked Examples & Constructions

1. **Primary Ideals in $\mathbb{Z}$**: $(0)$ and $(p^n)$ for prime $p$ are the only primary ideals in $\mathbb{Z}$.
2. **Polynomial Rings**: $(x, y^2)$ in $k[x, y]$ is primary with radical $(x, y)$.
3. **Non-primary Prime Powers**: $\mathfrak{p}^2$ in $k[x, y, z]/(xy - z^2)$ is not primary.

---

## Exercises (Selected)

1. **Exercise 1**: Show that if an ideal $a$ has a primary decomposition, $\operatorname{Spec}(A/a)$ has finitely many irreducible components.
2. **Exercise 7**: Extend primary decomposition to polynomial rings $A[x]$.

---

## Key Insights

- Primary decomposition generalizes unique factorization to ideals.
- Minimal primary decompositions are unique up to associated prime ideals.
- Localization preserves primary properties and isolates components.
- Zero-divisors and nilpotent elements are tied to associated primes.
- Symbolic powers of prime ideals are $\mathfrak{p}$-primary.

---

## Connections & Backlinks

- [[Chapter 1: Rings and Ideals]]: Basic properties of ideals and radicals.
- [[Chapter 3: Modules]]: Submodules and their properties.
- [[Chapter 5: Integral Dependence and Chain Conditions]]: Noetherian property and its role in primary decomposition.

---

## Further Reading

- Eisenbud, David. *Commutative Algebra with a View Toward Algebraic Geometry*.  
- Matsumura, Hideyuki. *Commutative Ring Theory*.  
- Zariski, Oscar, and Pierre Samuel. *Commutative Algebra*.

        ---
        *Generated by `ingest_chapters.py` · model: gpt-4o*
