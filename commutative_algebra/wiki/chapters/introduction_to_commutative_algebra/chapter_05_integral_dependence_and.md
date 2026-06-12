        ---
        title: "Ch 5: Integral Dependence and"
        book: "introduction to commutative algebra"
        source: "introduction_to_commutative_algebra.pdf"
        pages: "69–83"
        chapter: 5
        type: chapter-summary
        status: auto-generated
        model: gpt-4o
        date: 2026-06-12
        tags: [knowledge-base, auto-ingested, chapter-note]
        ---

        # Chapter 5: Integral Dependence and

        > *Auto-generated rich summary — introduction to commutative algebra*
        > *Pages 69–83 | Ingested 2026-06-12*

        # Chapter 5: Integral Dependence and Valuations

This article provides a detailed summary of Chapter 5 of *Introduction to Commutative Algebra* by M. F. Atiyah and I. G. Macdonald. The chapter explores the concept of integral dependence, integral closures, and their applications in commutative algebra. It also delves into valuation rings, their properties, and their connections to valuations and value groups. The chapter culminates in significant results such as the Going-Up and Going-Down theorems, which describe the behavior of prime ideals in integral extensions.

---

## Overview

Integral dependence is a central concept in commutative algebra, generalizing the notion of algebraic dependence to rings and subrings. This chapter introduces the concept of integral elements, integral closures, and integral extensions, establishing their fundamental properties and applications. Key results include the equivalence of various characterizations of integral elements, the transitivity of integral dependence, and the preservation of integral dependence under localization and quotients.

The chapter also introduces valuation rings, which are integral domains with a total ordering on their ideals. These rings are closely tied to valuations of fields and their associated value groups. The Going-Up and Going-Down theorems, which describe the behavior of chains of prime ideals in integral extensions, are pivotal results with applications in algebraic geometry and number theory.

This material is foundational for understanding the structure of rings and their spectra, as well as for studying algebraic varieties and schemes. The chapter emphasizes the interplay between algebraic and geometric perspectives, providing tools that are essential in modern commutative algebra.

---

## Definitions & Notation

1. **Integral Dependence**:  
   Let $B$ be a ring and $A$ a subring of $B$. An element $x \in B$ is **integral over $A$** if it satisfies a monic polynomial with coefficients in $A$:  

$$
x^n + a_1x^{n-1} + \cdots + a_n = 0, \quad a_i \in A.
$$

2. **Integral Closure**:  
   The set of elements in $B$ that are integral over $A$ is called the **integral closure** of $A$ in $B$.  
   - If the integral closure of $A$ in $B$ is $A$, then $A$ is **integrally closed** in $B$.  
   - If the integral closure of $A$ in $B$ is $B$, then $B$ is **integral over $A$**.

3. **Integral Homomorphism**:  
   A ring homomorphism $f: A \to B$ is **integral** if $B$ is integral over $f(A)$. In this case, $B$ is called an **integral $A$-algebra**.

4. **Valuation Ring**:  
   A ring $A$ is a **valuation ring** of a field $K$ if, for every $x \in K^*$, either $x \in A$ or $x^{-1} \in A$ (or both).

5. **Value Group**:  
   Let $A$ be a valuation ring of a field $K$. The **value group** $\Gamma$ is defined as $\Gamma = K^* / U$, where $U$ is the group of units of $A$. $\Gamma$ is a totally ordered abelian group.

6. **Going-Up Property**:  
   A ring homomorphism $f: A \to B$ has the **going-up property** if chains of prime ideals in $A$ can always be extended to chains of prime ideals in $B$.

7. **Going-Down Property**:  
   A ring homomorphism $f: A \to B$ has the **going-down property** if descending chains of prime ideals in $A$ can always be extended to descending chains of prime ideals in $B$.

---

## Theorems, Lemmas & Corollaries

### Proposition 5.1  
**Statement**: The following are equivalent for $x \in B$:  
i) $x$ is integral over $A$.  
ii) $A[x]$ is a finitely generated $A$-module.  
iii) $A[x]$ is contained in a subring $C$ of $B$ such that $C$ is a finitely generated $A$-module.  
iv) There exists a faithful $A[x]$-module $M$ which is finitely generated as an $A$-module.

---

### Corollary 5.2  
**Statement**: Let $x_1, \dots, x_n \in B$ be integral over $A$. Then $A[x_1, \dots, x_n]$ is a finitely generated $A$-module.

---

### Theorem 5.10  
**Statement**: Let $A \subseteq B$ be rings, and suppose $B$ is integral over $A$. Let $\mathfrak{p}$ be a prime ideal of $A$. Then there exists a prime ideal $q$ of $B$ such that $q \cap A = \mathfrak{p}$.

---

### Theorem 5.11 (Going-Up Theorem)  
**Statement**: Let $A \subseteq B$ be rings, and suppose $B$ is integral over $A$. Let $\mathfrak{p}_1 \subseteq \cdots \subseteq \mathfrak{p}_n$ be a chain of prime ideals of $A$, and let $q_1 \subseteq \cdots \subseteq q_m$ ($m < n$) be a chain of prime ideals of $B$ such that $q_i \cap A = \mathfrak{p}_i$ for $1 \leq i \leq m$. Then the chain $q_1 \subseteq \cdots \subseteq q_m$ can be extended to a chain $q_1 \subseteq \cdots \subseteq q_n$ such that $q_i \cap A = \mathfrak{p}_i$ for $1 \leq i \leq n$.

---

### Theorem 5.16 (Going-Down Theorem)  
**Statement**: Let $A \subseteq B$ be integral domains, with $A$ integrally closed and $B$ integral over $A$. Let $\mathfrak{p}_1 \supseteq \cdots \supseteq \mathfrak{p}_n$ be a chain of prime ideals of $A$, and let $q_1 \supseteq \cdots \supseteq q_m$ ($m < n$) be a chain of prime ideals of $B$ such that $q_i \cap A = \mathfrak{p}_i$ for $1 \leq i \leq m$. Then the chain $q_1 \supseteq \cdots \supseteq q_m$ can be extended to a chain $q_1 \supseteq \cdots \supseteq q_n$ such that $q_i \cap A = \mathfrak{p}_i$ for $1 \leq i \leq n$.

---

## Proof Ideas

- **Proposition 5.1**: The equivalences are proven by constructing modules and subrings that satisfy the required properties and leveraging the definition of integral dependence.  
- **Theorem 5.10**: Uses localization to construct a prime ideal $q$ in $B$ lying over $\mathfrak{p}$.  
- **Theorem 5.11**: Reduces to the case $m = 1, n = 2$, using Theorem 5.10 to find a prime ideal $q_2$ in $B$ lying over $\mathfrak{p}_2$.  
- **Theorem 5.16**: Uses localization and the integrally closed property of $A$ to show that $\mathfrak{p}_2$ is the contraction of a prime ideal in $B$.

---

## Worked Examples & Constructions

- **Example**: Let $A = \mathbb{Z}$ and $B = \mathbb{Q}$. If $x = \frac{r}{s} \in \mathbb{Q}$ is integral over $\mathbb{Z}$, then $x$ satisfies a monic polynomial with integer coefficients. This forces $s = \pm 1$, so $x \in \mathbb{Z}$.

---

## Exercises (Selected)

1. **Exercise**: Prove that if $A \to B$ is integral and $C$ is an $A$-algebra, then $\text{Spec}(B \otimes_A C) \to \text{Spec}(C)$ is a closed map.  
2. **Exercise**: Show that the integral closure of $A$ in $B$ is preserved under localization.

---

## Key Insights

1. Integral dependence generalizes algebraic dependence to rings.
2. Integral closure is a subring containing all elements of $B$ integral over $A$.
3. The Going-Up and Going-Down theorems describe prime ideal behavior in integral extensions.
4. Valuation rings are integrally closed and have a total ordering on their ideals.
5. The integral closure of $A$ in $B$ is the intersection of all valuation rings of $B$ containing $A$.

---

## Connections & Backlinks

- [[Chapter 3: Modules and Localization]]  
- [[Chapter 4: Prime Ideals and Spec]]  
- [[Chapter 6: Dedekind Domains]]  

---

## Further Reading

- M. Reid, *Undergraduate Commutative Algebra*  
- H. Matsumura, *Commutative Ring Theory*  
- D. Eisenbud, *Commutative Algebra with a View Toward Algebraic Geometry*  

        ---
        *Generated by `ingest_chapters.py` · model: gpt-4o*
