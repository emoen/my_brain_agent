 ---
 title: "Ch 5: Distributions"
 book: "GTM208 Analysis for Applied Mathematics, Ward Cheney (2001, ISBN 978-0-387-95279-6)"
 source: "GTM208.Analysis.for.Applied.Mathematics,.Ward.Cheney.(2001,.ISBN.978-0-387-95279-6).pdf"
 pages: "254–294"
 chapter: 5
 type: chapter-summary
 status: auto-generated
 model: gpt-4o
 date: 2026-04-15
 tags: [knowledge-base, auto-ingested, chapter-note]
 ---

 # Chapter 5: Distributions

 > *Auto-generated rich summary — GTM208 Analysis for Applied Mathematics, Ward Cheney (2001, ISBN 978-0-387-95279-6)*
 > *Pages 254–294 | Ingested 2026-04-15*

 # Chapter 5: Distributions

## Overview

Chapter 5 of *GTM208 Analysis for Applied Mathematics* by Ward Cheney introduces the theory of distributions, also known as generalized functions. This framework extends the classical notion of functions to include objects such as the Dirac delta and the Heaviside function, which are indispensable in mathematical physics, engineering, and applied mathematics. These objects, while not functions in the traditional sense, allow for the rigorous treatment of singularities, discontinuities, and other irregularities that arise in real-world applications.

The chapter begins by defining distributions as continuous linear functionals on the space of test functions $\mathcal{D}$, which consists of smooth functions with compact support. It then develops the core properties of distributions, including their differentiation, support, and convolution with test functions. The chapter also explores the concept of fundamental solutions to linear differential operators, demonstrating how distributions can be used to solve differential equations that are otherwise intractable in the classical framework. 

This material plays a critical role in the book's broader exploration of applied mathematics, particularly in the context of partial differential equations (PDEs), Fourier analysis, and functional analysis. By introducing distributions, the chapter equips readers with the tools to handle problems involving non-smooth phenomena, such as point sources and discontinuities, which frequently appear in physics and engineering.

---

## Definitions & Notation

### Key Definitions
1. **Distributions**: 
 A distribution is a continuous linear functional $T: \mathcal{D} \to \mathbb{R}$, where $\mathcal{D}$ is the space of test functions $C_c^\infty(\mathbb{R}^n)$ (infinitely differentiable functions with compact support). The space of all distributions is denoted $\mathcal{D}'(\mathbb{R}^n)$.

2. **Test Functions ($\mathcal{D}$)**: 
 The space $\mathcal{D}$ consists of functions $\phi \in C^\infty(\mathbb{R}^n)$ with compact support. The support of $\phi$ is the closure of the set $\{x \in \mathbb{R}^n : \phi(x) \neq 0\}$.

3. **Support of a Distribution**: 
 The support of a distribution $T$, denoted $\text{supp}(T)$, is the smallest closed set $F \subset \mathbb{R}^n$ such that $T(\phi) = 0$ for all $\phi \in \mathcal{D}$ with $\text{supp}(\phi) \subset \mathbb{R}^n \setminus F$.

4. **Locally Integrable Functions ($L_{\text{loc}}(\mathbb{R}^n)$)**: 
 A function $f: \mathbb{R}^n \to \mathbb{R}$ is locally integrable if $\int_K |f(x)| \, dx < \infty$ for every compact set $K \subset \mathbb{R}^n$.

5. **Distributional Derivative**: 
 If $T \in \mathcal{D}'$ and $\alpha$ is a multi-index, the derivative $\partial^\alpha T$ is defined by:

$$
\partial^\alpha T(\phi) = (-1)^{|\alpha|} T(D^\alpha \phi),
$$

where $D^\alpha \phi$ is the classical partial derivative of $\phi$.

6. **Convolution of a Distribution and a Test Function**: 
 If $T \in \mathcal{D}'$ and $\phi \in \mathcal{D}$, the convolution $T * \phi$ is defined as:

$$
(T * \phi)(x) = T(E_x B\phi),
$$

where $(E_x \phi)(y) = \phi(y - x)$ and $(B\phi)(y) = \phi(-y)$.

7. **Fundamental Solution**: 
 A distribution $T$ is a fundamental solution of a linear differential operator $L$ if $L T = \delta$, where $\delta$ is the Dirac delta distribution.

---

## Theorems, Lemmas & Corollaries

### Theorem 1: Continuity of Partial Differential Operators
**Statement**: 
For every multi-index $\alpha$, the operator $D^\alpha$ is a continuous linear map from $\mathcal{D}$ to $\mathcal{D}$ and from $\mathcal{D}'$ to $\mathcal{D}'$. 

---

### Theorem 2: Distributions from Locally Integrable Functions 
**Statement**: 
If $f \in L_{\text{loc}}(\mathbb{R}^n)$, then the mapping:

$$
T_f(\phi) = \int_{\mathbb{R}^n} f(x) \phi(x) \, dx \quad (\phi \in \mathcal{D}),
$$

defines a distribution $T_f$. The map $f \mapsto T_f$ is linear and injective.

---

### Theorem 3: Convolution and Differentiation 
**Statement**: 
If $T \in \mathcal{D}'$ and $\phi \in \mathcal{D}$, then for any multi-index $\alpha$:

$$
D^\alpha(T * \phi) = T * D^\alpha \phi.
$$

---

### Theorem 4: Fundamental Solutions of Differential Operators
**Statement**: 
Let $L$ be a linear differential operator with constant coefficients. If $L$ satisfies certain conditions (e.g., ellipticity), then $L$ has a fundamental solution $T$ such that $L T = \delta$.

---

## Proof Ideas

1. **Theorem 2**: 
 Continuity is shown using the Dominated Convergence Theorem. Injectivity is proved by assuming $f \neq 0$ and constructing a test function $\phi$ such that $T_f(\phi) \neq 0$.

2. **Theorem 3**: 
 The proof relies on the definitions of convolution and distributional derivatives, showing that the differentiation operator commutes with convolution.

3. **Theorem 4**: 
 The proof constructs $T$ explicitly using Fourier transforms and verifies that $L T = \delta$.

---

## Worked Examples & Constructions

1. **Dirac Delta Distribution**: 
 The Dirac delta $\delta_\xi$ is defined by $\delta_\xi(\phi) = \phi(\xi)$. It is shown to be a distribution because it satisfies linearity and continuity.

2. **Heaviside Function**: 
 The Heaviside function $H(x)$ is defined as $H(x) = 1$ for $x \geq 0$ and $H(x) = 0$ for $x < 0$. Its derivative in the distributional sense is $\partial H = \delta$.

3. **Convolution Approximation**: 
 A sequence of mollifiers $\phi_\epsilon(x) = \epsilon^{-n} \phi(x / \epsilon)$ is used to approximate a function $f$ by $f * \phi_\epsilon$, which is smooth and converges to $f$ in $\mathcal{D}'$.

---

## Exercises (Selected)

1. Prove that the Dirac delta $\delta$ is a distribution and compute $\delta * \phi$ for $\phi \in \mathcal{D}$. 
2. Show that $\partial H = \delta$, where $H$ is the Heaviside function. 
3. Prove that $\Delta |x|^{2-n} = 0$ for $n \geq 3$ and $x \neq 0$. 
4. Compute the convolution of $H(x)$ and a test function $\phi(x)$. 

---

## Key Insights

1. Distributions generalize classical functions, enabling differentiation of non-smooth objects. 
2. The space of test functions $\mathcal{D}$ is central to the theory of distributions. 
3. Distributions include regular distributions (derived from functions) and singular distributions (e.g., Dirac delta). 
4. Convolution is a powerful tool for approximating functions and solving differential equations. 
5. The Dirac delta and Heaviside function are fundamental examples of distributions. 
6. Distributional derivatives generalize classical derivatives and are always well-defined. 
7. Fundamental solutions provide a framework for solving linear PDEs using distributions. 
8. The theory of distributions relies heavily on functional analysis and the properties of test functions.

---

## Connections & Backlinks

- [[Chapter 4: Fourier Analysis]] 
- [[Chapter 6: Partial Differential Equations]] 
- [[Sobolev Spaces]] 

---

## Further Reading

1. Lighthill, M. J. *Introduction to Fourier Analysis and Generalized Functions*. 
2. Schwartz, L. *Théorie des Distributions*. 
3. Hörmander, L. *The Analysis of Linear Partial Differential Operators I*. 
4. Strichartz, R. *A Guide to Distribution Theory and Fourier Transforms*. 

 ---
 *Generated by `ingest_chapters.py` · model: gpt-4o*
