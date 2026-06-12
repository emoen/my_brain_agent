 ---
 title: "Ch 1: Normed Linear S paces"
 book: "GTM208 Analysis for Applied Mathematics, Ward Cheney (2001, ISBN 978-0-387-95279-6)"
 source: "GTM208.Analysis.for.Applied.Mathematics,.Ward.Cheney.(2001,.ISBN.978-0-387-95279-6).pdf"
 pages: "9–68"
 chapter: 1
 type: chapter-summary
 status: auto-generated
 model: gpt-4o
 date: 2026-04-15
 tags: [knowledge-base, auto-ingested, chapter-note]
 ---

 # Chapter 1: Normed Linear S paces

 > *Auto-generated rich summary — GTM208 Analysis for Applied Mathematics, Ward Cheney (2001, ISBN 978-0-387-95279-6)*
 > *Pages 9–68 | Ingested 2026-04-15*

 # Normed Linear Spaces: Chapter 1 Summary

This article provides a cohesive and detailed summary of Chapter 1 ("Normed Linear Spaces") from *Analysis for Applied Mathematics* by Ward Cheney (GTM208, 2001). The chapter introduces foundational concepts in normed linear spaces, explores key theorems, and provides examples and exercises to deepen understanding. It serves as a cornerstone for the study of functional analysis and its applications in applied mathematics.

---

## Overview

Chapter 1 of *Analysis for Applied Mathematics* focuses on the theory of normed linear spaces, which generalize Euclidean spaces to abstract settings, enabling the study of infinite-dimensional spaces. These spaces are pivotal in functional analysis and applied mathematics, providing the framework for analyzing the behavior of functions, sequences, and operators. The chapter introduces key definitions, such as norms, vector spaces, compactness, and completeness, and explores their interplay through rigorous theorems and examples.

The chapter lays the groundwork for understanding convergence, continuity, and compactness in normed spaces, which are essential for solving problems in approximation theory, numerical analysis, and optimization. It also introduces fundamental results such as Riesz's Lemma and the equivalence of norms in finite-dimensional spaces, preparing readers for more advanced topics like Banach spaces, Hilbert spaces, and operator theory.

---

## Definitions & Notation

### Vector Space
A **vector space** $X$ over a field $\mathbb{R}$ (or $\mathbb{C}$) is a set equipped with two operations: vector addition and scalar multiplication. These operations satisfy the following axioms:
1. Closure under addition and scalar multiplication.
2. Commutativity and associativity of addition.
3. Existence of additive identity ($0$) and additive inverses.
4. Distributive properties of scalar multiplication over vector addition and scalar addition.
5. Associativity and identity element for scalar multiplication.

### Norm
A **norm** on a vector space $X$ is a function $\|\cdot\|: X \to \mathbb{R}$ satisfying:
1. **Positivity**:$\|x\| > 0$ for all $x \neq 0$, and $\|x\| = 0$ if and only if $x = 0$.
2. **Homogeneity**: $\|\lambda x\| = |\lambda| \|x\|$ for all $\lambda \in \mathbb{R}$ and $x \in X$.
3. **Triangle inequality**: $\|x + y\| \leq \|x\| + \|y\|$ for all $x, y \in X$.

A vector space equipped with a norm is called a **normed linear space**.

### Compact Set
A subset $K$ of a normed linear space is **compact** if every sequence in $K$ has a convergent subsequence whose limit lies in $K$.

### Open Set
A subset $U$ of a normed linear space is **open** if for every $x \in U$, there exists $\epsilon > 0$ such that $B(x, \epsilon) \subseteq U$, where $B(x, \epsilon) = \{y \in X : \|x - y\| < \epsilon\}$.

### Closed Set
A subset $F$ of a normed linear space is **closed** if the limit of every convergent sequence in $F$ is also in $F$.

### Finite-Dimensional Space
A vector space is **finite-dimensional** if it has a finite basis. Its dimension is the number of elements in any basis.

### Banach Space
A **Banach space** is a normed linear space that is complete, meaning every Cauchy sequence in the space converges to a point within the space.

### Riesz's Lemma
If $U$ is a closed proper subspace of a normed linear space $X$, and $0 < \lambda < 1$, then there exists $x \in X$ such that $\|x\| = 1$ and $\text{dist}(x, U) > \lambda$.

---

## Theorems, Lemmas & Corollaries

### Theorem 1: Compactness in Finite-Dimensional Spaces
**Statement**: In a finite-dimensional normed linear space, every closed and bounded set is compact.

### Corollary 1: Completeness of Finite-Dimensional Spaces
**Statement**: Every finite-dimensional normed linear space is complete.

### Corollary 2: Closed Subspaces
**Statement**: Every finite-dimensional subspace of a normed linear space is closed.

### Theorem 5: Rearrangement of Absolutely Convergent Series
**Statement**: If a series in a Banach space is absolutely convergent, then all rearrangements of the series converge to the same value.

### Riemann's Theorem
**Statement**: If a series of real numbers converges but is not absolutely convergent, then for every real number $r$, there exists a rearrangement of the series that converges to $r$.

### Lemma 1: Compactness of Balls in $\ell_\infty$-Norm
**Statement**: In $\mathbb{R}^n$ with the $\ell_\infty$-norm, every ball $\{x \in \mathbb{R}^n : \|x\|_\infty \leq c\}$ is compact.

### Lemma 2: Compactness of Closed Subsets
**Statement**: A closed subset of a compact set is compact.

---

## Proof Ideas

### Theorem 1
The proof uses the fact that finite-dimensional normed spaces are isomorphic to $\mathbb{R}^n$, where compactness is guaranteed by the Heine-Borel theorem.

### Corollary 1
The proof shows that every Cauchy sequence in a finite-dimensional normed space is bounded. Using the compactness of the closed ball containing the sequence, a convergent subsequence is extracted.

### Riesz's Lemma
The proof constructs a point $x$ outside the subspace $U$ and normalizes it to satisfy the required distance properties.

---

## Worked Examples & Constructions

### Example: Norm Continuity
The norm function $\|\cdot\|$ is continuous in any normed linear space. This follows from the inequality $|\|x_n\| - \|x\|| \leq \|x_n - x\|$.

### Example: Compactness of Unit Ball
The unit ball $\{x : \|x\| \leq 1\}$ in a finite-dimensional normed space is compact, as it is closed and bounded.

---

## Exercises (Selected)

1. **Exercise 7**: Prove the equivalence of the definition of open sets and the existence of $\epsilon$-balls.
2. **Exercise 10**: Show that if a series converges in a normed linear space, then its terms must converge to zero.
3. **Exercise 13**: Explore the divergence of positive terms in a conditionally convergent series.

---

## Key Insights

1. Normed linear spaces generalize Euclidean spaces and are foundational to functional analysis.
2. Compactness in finite-dimensional spaces is equivalent to closedness and boundedness.
3. Completeness ensures that Cauchy sequences converge within the space, a property critical for Banach spaces.
4. Absolute convergence in Banach spaces guarantees invariance under series rearrangements.
5. Riesz's Lemma provides a way to find points at a specific distance from closed subspaces, with applications in approximation theory.
6. The interplay between compactness, continuity, and convergence is central to the study of normed spaces.

---

## Connections & Backlinks

- [[Chapter 2: Banach Spaces]]: Builds on the completeness property introduced in Chapter 1.
- [[Heine-Borel Theorem]]: Used to establish compactness in finite-dimensional spaces.
- [[Riesz's Lemma]]: A foundational result in functional analysis.

---

## Further Reading

- *Functional Analysis* by Peter Lax: A deeper exploration of normed spaces and Banach spaces.
- *Principles of Mathematical Analysis* by Walter Rudin: A classic text covering compactness, completeness, and convergence.
- Online resources: MIT OpenCourseWare on Functional Analysis.

 ---
 *Generated by `ingest_chapters.py` · model: gpt-4o*
