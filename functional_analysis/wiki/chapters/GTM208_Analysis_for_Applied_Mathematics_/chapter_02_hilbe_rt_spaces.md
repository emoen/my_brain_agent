 ---
 title: "Ch 2: Hilbe rt Spaces"
 book: "GTM208 Analysis for Applied Mathematics, Ward Cheney (2001, ISBN 978-0-387-95279-6)"
 source: "GTM208.Analysis.for.Applied.Mathematics,.Ward.Cheney.(2001,.ISBN.978-0-387-95279-6).pdf"
 pages: "69–122"
 chapter: 2
 type: chapter-summary
 status: auto-generated
 model: gpt-4o
 date: 2026-04-15
 tags: [knowledge-base, auto-ingested, chapter-note]
 ---

 # Chapter 2: Hilbe rt Spaces

 > *Auto-generated rich summary — GTM208 Analysis for Applied Mathematics, Ward Cheney (2001, ISBN 978-0-387-95279-6)*
 > *Pages 69–122 | Ingested 2026-04-15*

 # Chapter 2: Hilbert Spaces

This article provides a detailed summary of Chapter 2 ("Hilbert Spaces") from *Analysis for Applied Mathematics* by Ward Cheney (2001, ISBN 978-0-387-95279-6). The chapter introduces the foundational concepts of Hilbert spaces, which generalize the geometry of Euclidean spaces to infinite-dimensional settings. These spaces are central to functional analysis and underpin many areas of applied mathematics, including Fourier analysis, quantum mechanics, partial differential equations, and numerical methods.

The chapter explores the interplay between geometry (orthogonality, projections) and operator theory (boundedness, compactness, adjoints), culminating in key results such as the Riesz Representation Theorem, spectral theorem for compact Hermitian operators, and applications to Sturm-Liouville problems. Through definitions, theorems, proofs, examples, and exercises, readers gain a rigorous understanding of Hilbert spaces and their applications.

---

## Overview

Hilbert spaces are complete inner-product spaces that extend the geometric and algebraic properties of finite-dimensional Euclidean spaces to infinite dimensions. This chapter begins by defining inner-product spaces and their associated norms, followed by an exploration of orthogonality, orthogonal projections, and orthonormal bases. These geometric concepts are then used to study the decomposition of Hilbert spaces into orthogonal subspaces.

The chapter also introduces compact operators, integral operators, and their spectral properties, emphasizing their importance in applied mathematics. The Riesz Representation Theorem connects bounded linear functionals to inner products, while the spectral theorem provides a framework for analyzing compact Hermitian operators. Sturm-Liouville theory and Green's functions are presented as applications of Hilbert space theory to differential equations, showcasing the practical relevance of the material.

---

## Definitions & Notation

### Key Terms

1. **Inner-product space**: 
 A vector space $X$ over $\mathbb{C}$ (or $\mathbb{R}$) equipped with an inner product $(x, y)$, satisfying:
 - Conjugate symmetry: $(x, y) = \overline{(y, x)}$,
 - Linearity in the first argument: $(ax, y) = a(x, y)$,
 - Positive definiteness: $(x, x) > 0$ if $x \neq 0$,
 - Additivity: $(x + y, z) = (x, z) + (y, z)$.

2. **Hilbert space**: 
 A complete inner-product space, where completeness means every Cauchy sequence converges to an element in the space.

3. **Norm**: 
 Derived from the inner product as $\|x\| = \sqrt{(x, x)}$.

4. **Orthogonality**: 
 Two vectors $x$ and $y$ are orthogonal if $(x, y) = 0$, denoted $x \perp y$.

5. **Orthogonal complement**: 
 The set $Y^\perp = \{x \in X : (x, y) = 0 \text{ for all } y \in Y\}$.

6. **Orthonormal set**: 
 A set $\{u_i\}$ is orthonormal if $\|u_i\| = 1$ and $(u_i, u_j) = \delta_{ij}$, where $\delta_{ij}$ is the Kronecker delta.

7. **Orthogonal projection**: 
 For $x \in X$ and a subspace $Y$, the orthogonal projection of $x$ onto $Y$ is the unique point $y \in Y$ closest to $x$.

8. **Compact operator**: 
 A linear operator $A$ is compact if it maps bounded sets to relatively compact sets (sets with compact closure).

9. **Weak convergence**: 
 A sequence $\{x_n\}$ converges weakly to $x$ (denoted $x_n \rightharpoonup x$) if $(x_n, y) \to (x, y)$ for all $y \in X$.

10. **Sturm-Liouville operator**: 
 $Ax = (px')' + qx$, where $p, q$ are real-valued functions defined on $[a, b]$, and $x$ satisfies boundary conditions.

11. **Green's function**: 
 A function $g(s, t)$ that satisfies $Ag_t = \delta(s - t)$, where $\delta$ is the Dirac delta function.

---

## Theorems, Lemmas & Corollaries

### **Theorem 1: Properties of the Norm in Inner-Product Spaces**
1.$\|x\| > 0$ if $x \neq 0$,
2. $\|ax\| = |a| \|x\|$ for $a \in \mathbb{C}$,
3. $|(x, y)| \leq \|x\| \|y\|$ (Cauchy-Schwarz Inequality),
4.$\|x + y\| \leq \|x\| + \|y\|$ (Triangle Inequality),
5.$\|x + y\|^2 + \|x - y\|^2 = 2\|x\|^2 + 2\|y\|^2$ (Parallelogram Law),
6. If $x \perp y$, then $\|x + y\|^2 = \|x\|^2 + \|y\|^2$ (Pythagorean Law).

---

### **Theorem 2: Closest Point in a Closed Convex Set**
If $K$ is a closed, convex, non-empty subset of a Hilbert space $X$, then for each $x \in X$, there exists a unique $y \in K$ such that:

$$
\|x - y\| = \inf\{\|x - v\| : v \in K\}.
$$

---

### **Theorem 3: Orthogonal Projection**
Let $Y$ be a subspace of $X$. For $x \in X$, the point $y \in Y$ closest to $x$ satisfies:
1.$x - y \perp Y$, i.e., $(x - y, v) = 0$ for all $v \in Y$,
2. $y$ is unique.

---

### **Theorem 4: Decomposition of Hilbert Spaces**
If $Y$ is a closed subspace of $X$, then:

$$
X = Y \oplus Y^\perp.
$$

Every $x \in X$ can be uniquely written as $x = y + z$, where $y \in Y$ and $z \in Y^\perp$.

---

### **Theorem 5: Riesz Representation Theorem**
Every continuous linear functional $\phi$ on a Hilbert space $X$ can be expressed as:

$$
\phi(x) = (x, v) \quad \text{for a unique } v \in X.
$$

---

### **Theorem 6: Spectral Theorem for Compact Hermitian Operators**
A compact Hermitian operator $A$ on a Hilbert space has the representation:

$$
Ax = \sum \lambda_k (x, e_k)e_k,
$$

where $\{e_k\}$ is an orthonormal basis,$\lambda_k$ are real eigenvalues, and $\lambda_k \to 0$.

---

## Proof Ideas

1. **Cauchy-Schwarz Inequality**: 
 Analyze $(x - \lambda y, x - \lambda y)$ for $\lambda = (x, y)$.

2. **Orthogonal Projection**: 
 Use the Parallelogram Law to show that the minimizing sequence converges to a unique point in the subspace.

3. **Riesz Representation Theorem**: 
 Decompose $x$ using the null space of $\phi$ and construct $v$ such that $\phi(x) = (x, v)$.

4. **Spectral Theorem**: 
 Construct an orthonormal basis by iteratively applying the spectral decomposition to $A$, leveraging the compactness and Hermitian properties of $A$.

---

## Worked Examples & Constructions

1. **Example**: 
 Legendre polynomials $P_n(t)$ form an orthonormal basis for $L^2[-1, 1]$.

2. **Example**: 
 Solve $Ax = -x''$ with boundary conditions $x(0) = x(\pi) = 0$. The eigenvalues are $n^2$, and the eigenfunctions are $\sin(nt)$.

---

## Exercises (Selected)

1. **Exercise**: Prove the Parallelogram Law. 
2. **Exercise**: Show $X = Y \oplus Y^\perp$ for closed subspaces $Y$. 
3. **Exercise**: Find the eigenvalues and eigenfunctions for $A = -x'' + 2x' - x$, with domain consisting of twice continuously differentiable functions on $[0, 1]$ satisfying $x(0) = x(1) = 0$.

---

## Key Insights

1. Hilbert spaces generalize Euclidean geometry to infinite dimensions. 
2. Orthogonality is fundamental to the structure of Hilbert spaces. 
3. The Riesz Representation Theorem connects linear functionals to inner products. 
4. Compact operators have discrete spectra, and their eigenvalues converge to zero. 
5. Sturm-Liouville theory is central to solving boundary-value problems. 
6. Green's functions provide explicit solutions to differential equations. 

---

## Connections & Backlinks

- [[Chapter 1: Normed Linear Spaces]] 
- [[Chapter 3: Operators on Hilbert Spaces]] 
- [[Spectral Theorem]] 
- [[Sturm-Liouville Theory]] 

---

## Further Reading

- *Functional Analysis* by Peter Lax 
- *Introduction to Hilbert Space* by Paul Halmos 
- *Principles of Functional Analysis* by Martin Schechter 

 ---
 *Generated by `ingest_chapters.py` · model: gpt-4o*
