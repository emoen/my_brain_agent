 ---
 title: "Ch 8: Meas ure and Integration"
 book: "GTM208 Analysis for Applied Mathematics, Ward Cheney (2001, ISBN 978-0-387-95279-6)"
 source: "GTM208.Analysis.for.Applied.Mathematics,.Ward.Cheney.(2001,.ISBN.978-0-387-95279-6).pdf"
 pages: "389–456"
 chapter: 8
 type: chapter-summary
 status: auto-generated
 model: gpt-4o
 date: 2026-04-15
 tags: [knowledge-base, auto-ingested, chapter-note]
 ---

 # Chapter 8: Meas ure and Integration

 > *Auto-generated rich summary — GTM208 Analysis for Applied Mathematics, Ward Cheney (2001, ISBN 978-0-387-95279-6)*
 > *Pages 389–456 | Ingested 2026-04-15*

 # Chapter 8: Measure and Integration

This article provides a cohesive summary of Chapter 8 ("Measure and Integration") from *Analysis for Applied Mathematics* by Ward Cheney (2001, ISBN 978-0-387-95279-6). The chapter introduces foundational concepts in measure theory and integration, essential tools for modern analysis and applied mathematics. It builds upon earlier chapters in the book, extending the study of functions, spaces, and operators into the realm of measurable sets and functions, Lebesgue integration, and convergence theorems. These topics are crucial for understanding advanced mathematical analysis, probability theory, and functional analysis, as well as their applications in physics, engineering, and economics.

---

## Overview

Chapter 8 of *Analysis for Applied Mathematics* explores the rigorous mathematical framework underlying measure theory and integration. The chapter begins with the construction of measures, including the concept of outer measures and the definition of measurable sets. It then introduces the Lebesgue measure and Lebesgue integration, which generalizes the Riemann integral and allows for the integration of a broader class of functions. The chapter also presents key convergence theorems—such as the Monotone Convergence Theorem, Fatou's Lemma, and the Dominated Convergence Theorem—that are foundational to the study of integration in measure spaces. These results are indispensable for analyzing the behavior of sequences of functions and for solving problems in applied mathematics, such as those arising in differential equations, probability, and optimization.

---

## Definitions & Notation

### Measure Theory
- **Measure Space**: A triple $(X, \mathcal{A}, \mu)$, where:
 - $X$ is a set,
 -$\mathcal{A}$ is a $\sigma$-algebra of subsets of $X$,
 - $\mu: \mathcal{A} \to [0, \infty]$ is a measure satisfying:
 1.$\mu(\emptyset) = 0$,
 2. Countable additivity: $\mu\left(\bigcup_{i=1}^\infty A_i\right) = \sum_{i=1}^\infty \mu(A_i)$ for pairwise disjoint sets $\{A_i\}_{i=1}^\infty \subseteq \mathcal{A}$. (p. 386)

- **Outer Measure**: A function $\mu^*: \mathcal{P}(X) \to [0, \infty]$ (where $\mathcal{P}(X)$ is the power set of $X$) satisfying:
 1. $\mu^*(\emptyset) = 0$,
 2. Monotonicity: If $A \subseteq B$, then $\mu^*(A) \leq \mu^*(B)$,
 3. Countable subadditivity: $\mu^*\left(\bigcup_{i=1}^\infty A_i\right) \leq \sum_{i=1}^\infty \mu^*(A_i)$. (p. 382)

- **Lebesgue Outer Measure**: A specific outer measure $\mu^*$ defined on subsets of $\mathbb{R}^n$. (p. 382)

- **Lebesgue Measure**: The restriction of the Lebesgue outer measure $\mu^*$ to the $\sigma$-algebra of Lebesgue measurable sets. (p. 391)

- **Lebesgue Measurable Set**: A set $A \subseteq \mathbb{R}^n$ is Lebesgue measurable if, for every $E \subseteq \mathbb{R}^n$, $\mu^*(E) = \mu^*(E \cap A) + \mu^*(E \cap A^c)$. (p. 389)

- **Complete Measure Space**: A measure space $(X, \mathcal{A}, \mu)$ is complete if every subset of a $\mu$-null set is measurable (i.e., belongs to $\mathcal{A}$). (p. 387)

### Convergence and Integration
- **Monotone Convergence**: A sequence of functions $\{f_n\}$ satisfies $f_n(x) \uparrow f(x)$ if $f_n(x)$ is non-decreasing and converges pointwise to $f(x)$. (p. 401)

- **Dominated Convergence**: A sequence of functions $\{f_n\}$ is dominated by $g \in L^1(\mu)$ if $|f_n(x)| \leq g(x)$ for all $n$ and almost every $x \in X$. (p. 406)

---

## Theorems, Lemmas & Corollaries

### Monotone Convergence Theorem
**Statement**: Let $\{f_n\}$ be a sequence of non-negative measurable functions on a measure space $(X, \mathcal{A}, \mu)$ such that $f_n(x) \uparrow f(x)$ for all $x \in X$. Then:

$$
\lim_{n \to \infty} \int_X f_n \, d\mu = \int_X f \, d\mu.
$$

**Context**: This theorem allows the interchange of limits and integrals for non-negative increasing sequences. (p. 401)

---

### Fatou's Lemma
**Statement**: Let $\{f_n\}$ be a sequence of non-negative measurable functions on a measure space $(X, \mathcal{A}, \mu)$. Then:

$$
\int_X \liminf_{n \to \infty} f_n \, d\mu \leq \liminf_{n \to \infty} \int_X f_n \, d\mu.
$$

**Context**: Fatou's Lemma provides a lower bound for the integral of the $\liminf$ of a sequence of functions. (p. 403)

---

### Dominated Convergence Theorem
**Statement**: Let $\{f_n\}$ be a sequence of measurable functions on a measure space $(X, \mathcal{A}, \mu)$ such that $f_n \to f$ pointwise $\mu$-almost everywhere. If there exists a function $g \in L^1(\mu)$ such that $|f_n(x)| \leq g(x)$ for all $n$ and almost every $x \in X$, then:

$$
\lim_{n \to \infty} \int_X f_n \, d\mu = \int_X f \, d\mu.
$$

**Context**: This theorem enables the interchange of limits and integrals under the condition of domination by an integrable function. (p. 406)

---

## Proof Ideas

1. **Monotone Convergence Theorem**: 
 The proof relies on the monotonicity of $\{f_n\}$ and the countable additivity of $\mu$. By approximating $f$ from below using $\{f_n\}$, the equality of limits is established.

2. **Fatou's Lemma**: 
 The proof uses the definition of $\liminf$ and the monotonicity of the integral. By considering a sequence of functions that approximate $\liminf f_n$ from below, the inequality is derived.

3. **Dominated Convergence Theorem**: 
 The proof combines the boundedness of $\{f_n\}$ by $g$ and the properties of $L^1$ integrable functions. Fatou's Lemma and the linearity of the integral are key tools in the argument.

---

## Worked Examples & Constructions

- **Simple Function Approximation**: 
 Simple functions are introduced as building blocks for measurable functions. They are used to approximate more complex measurable functions in the context of integration theory. (p. 397)

---

## Exercises (Selected)

1. **Monotone Convergence**: 
 Prove the Monotone Convergence Theorem for $f_n(x) = \min\{n, x\}$ on $[0, \infty)$ with the Lebesgue measure. (p. 401)

2. **Fatou's Lemma**: 
 Verify Fatou's Lemma for $f_n(x) = \frac{1}{n} \chi_{[0, n]}(x)$, where $\chi_{[0, n]}$ is the characteristic function of $[0, n]$. (p. 403)

---

## Key Insights

- Measure theory generalizes the concept of length, area, and volume to arbitrary sets.
- Lebesgue integration extends the Riemann integral, enabling the integration of more complex functions.
- Convergence theorems (Monotone Convergence, Fatou's Lemma, Dominated Convergence) are fundamental tools for analyzing sequences of functions.
- Simple functions are essential for approximating measurable functions in integration.
- The concept of outer measure is critical for defining measurable sets and constructing the Lebesgue measure.

---

## Connections & Backlinks

- [[Chapter 7: Function Spaces]]: Introduces $L^p$ spaces, which are central to Lebesgue integration.
- [[Chapter 9: Fourier Analysis]]: Builds on measure theory and integration to study Fourier transforms and distributions.
- [[Chapter 10: Sobolev Spaces]]: Applies measure theory to functional analysis and partial differential equations.

---

## Further Reading

- H.L. Royden, *Real Analysis* (classic text on measure theory).
- P.R. Halmos, *Measure Theory* (comprehensive introduction to measure and integration).
- E. Stein & R. Shakarchi, *Real Analysis: Measure Theory, Integration, and Hilbert Spaces*.

 ---
 *Generated by `ingest_chapters.py` · model: gpt-4o*
