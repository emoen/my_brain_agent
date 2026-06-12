        ---
        title: "Ch 2: Modules"
        book: "introduction to commutative algebra"
        source: "introduction_to_commutative_algebra.pdf"
        pages: "27–45"
        chapter: 2
        type: chapter-summary
        status: auto-generated
        model: gpt-4o
        date: 2026-06-12
        tags: [knowledge-base, auto-ingested, chapter-note]
        ---

        # Chapter 2: Modules

        > *Auto-generated rich summary — introduction to commutative algebra*
        > *Pages 27–45 | Ingested 2026-06-12*

        # Chapter 2: Modules

## Overview

Chapter 2 of *Introduction to Commutative Algebra* introduces the foundational concepts of modules over commutative rings, a central construct in algebra. Modules generalize vector spaces by allowing scalars to come from arbitrary commutative rings rather than fields. This chapter explores the structure and properties of modules, including submodules, quotient modules, module homomorphisms, operations on modules, and exact sequences. It also delves into specific types of modules such as finitely generated modules, free modules, and flat modules, as well as constructions like tensor products and direct limits.

The material covered in this chapter is crucial for understanding more advanced topics in commutative algebra, such as localization, primary decomposition, and homological algebra. The chapter lays the groundwork for studying modules as algebraic objects and their interactions with rings, ideals, and other modules. The concepts introduced here are foundational for many areas of mathematics, including algebraic geometry, representation theory, and homological algebra.

---

## Definitions & Notation

### Modules and Related Concepts

1. **$A$-Module**:  
   Let $A$ be a commutative ring. An **$A$-module** is a pair $(M, \mu)$, where $M$ is an abelian group (written additively) and $\mu: A \times M \to M$ is a mapping satisfying the following axioms for $a, b \in A$ and $x, y \in M$:  
   - $a(x + y) = ax + ay$,  
   - $(a + b)x = ax + bx$,  
   - $(ab)x = a(bx)$,  
   - $1x = x$, where $1$ is the multiplicative identity in $A$.  

   Alternatively, $M$ can be seen as an abelian group with a ring homomorphism $A \to \text{End}(M)$, where $\text{End}(M)$ is the ring of endomorphisms of $M$.

2. **$A$-Module Homomorphism**:  
   A map $f: M \to N$ between $A$-modules $M$ and $N$ is an **$A$-module homomorphism** if:  
   - $f(x + y) = f(x) + f(y)$ for all $x, y \in M$,  
   - $f(ax) = a f(x)$ for all $a \in A$ and $x \in M$.  

3. **Submodule**:  
   A **submodule** $M'$ of an $A$-module $M$ is a subgroup of $M$ that is closed under multiplication by elements of $A$.

4. **Quotient Module**:  
   If $M'$ is a submodule of $M$, the quotient $M/M'$ inherits an $A$-module structure defined by $a(x + M') = ax + M'$ for $a \in A$ and $x \in M$.

5. **Exact Sequence**:  
   A sequence of $A$-modules and $A$-homomorphisms  

$$
M_1 \xrightarrow{f} M_2 \xrightarrow{g} M_3
$$

   is **exact at $M_2$** if $\text{im}(f) = \ker(g)$. A sequence is **exact** if it is exact at every module in the sequence.  

6. **Tensor Product**:  
   The **tensor product** of $A$-modules $M$ and $N$, denoted $M \otimes_A N$, is an $A$-module satisfying a universal property related to bilinear mappings. Elements $x \otimes y$ in $M \otimes_A N$ satisfy bilinearity relations:
   - $(x + x') \otimes y = x \otimes y + x' \otimes y$,  
   - $x \otimes (y + y') = x \otimes y + x \otimes y'$,  
   - $(ax) \otimes y = x \otimes (ay) = a(x \otimes y)$ for $a \in A$.  

7. **Direct Limit**:  
   The **direct limit** of a direct system of $A$-modules $(M_i, \phi_{ij})$ over a directed set $I$ is an $A$-module $M = \varinjlim M_i$ constructed as a quotient of the direct sum of the $M_i$ by relations ensuring compatibility of the homomorphisms $\phi_{ij}$.

---

## Theorems, Lemmas & Corollaries

### Proposition 2.1
**Statement**:  
1. If $L \supseteq M \supseteq N$ are $A$-modules, then  

$$
(L/N) / (M/N) \cong L/M.
$$

2. If $M_1, M_2$ are submodules of $M$, then  

$$
(M_1 + M_2) / M_1 \cong M_2 / (M_1 \cap M_2).
$$


---

### Proposition 2.3
**Statement**:  
An $A$-module $M$ is finitely generated if and only if $M$ is isomorphic to a quotient of $A^n$ for some integer $n > 0$.  

---

### Proposition 2.6 (Nakayama's Lemma)  
**Statement**:  
Let $M$ be a finitely generated $A$-module, and let $a$ be an ideal of $A$ contained in the Jacobson radical $m$ of $A$. If $aM = M$, then $M = 0$.  

---

### Proposition 2.9  
**Statement**:  
Exactness of module sequences corresponds to exactness of Hom sequences. Specifically:  
1. If  

$$
M' \xrightarrow{f} M \xrightarrow{g} M'' \to 0
$$

   is exact, then for all $A$-modules $N$, the sequence  

$$
0 \to \text{Hom}(M'', N) \to \text{Hom}(M, N) \to \text{Hom}(M', N)
$$

   is exact.  
2. Similarly, exactness of  

$$
0 \to N' \xrightarrow{f} N \xrightarrow{g} N''
$$

   implies exactness of  

$$
0 \to \text{Hom}(M, N') \to \text{Hom}(M, N) \to \text{Hom}(M, N'').
$$


---

### Proposition 2.18  
**Statement**:  
Let  

$$
M' \xrightarrow{f} M \xrightarrow{g} M'' \to 0
$$

be an exact sequence of $A$-modules, and let $N$ be any $A$-module. Then the sequence  

$$
M' \otimes N \xrightarrow{f \otimes 1} M \otimes N \xrightarrow{g \otimes 1} M'' \otimes N \to 0
$$

is exact.

---

## Proof Ideas

- **Proposition 2.6 (Nakayama's Lemma)**:  
  Use the fact that $a$ is contained in the Jacobson radical to construct an element $x \in A$ such that $xM = 0$. Since $x$ is a unit, $M = 0$.  

- **Proposition 2.18**:  
  Use the universal property of the tensor product and the exactness of Hom sequences to deduce the exactness of the tensor sequence.

---

## Worked Examples & Constructions

1. **Examples of Modules**:  
   - Ideals of $A$ are $A$-modules.  
   - $\mathbb{Z}$-modules are abelian groups.  
   - $k[x]$-modules correspond to $k$-vector spaces with a linear transformation.  

2. **Tensor Product Construction**:  
   The tensor product $M \otimes_A N$ is constructed as a quotient of the free $A$-module $A^{M \times N}$ by relations enforcing bilinearity.

---

## Exercises (selected)

1. **Exercise 2.2**: Show $\text{Ann}(M + N) = \text{Ann}(M) \cap \text{Ann}(N)$.  
2. **Exercise 2.15**: Prove that tensor products commute with direct limits.  
3. **Exercise 2.22**: Show that the direct limit of nilradicals is the nilradical of the direct limit of rings.

---

## Key Insights

1. Modules generalize vector spaces and ideals, allowing scalars from commutative rings.  
2. Submodules and quotient modules inherit the structure of $A$-modules.  
3. Finitely generated modules are quotients of free modules.  
4. Exact sequences are central tools for understanding module structure.  
5. Nakayama's Lemma is critical for analyzing finitely generated modules over local rings.  
6. Tensor products satisfy universal properties and are essential for bilinear mappings.  
7. Direct limits provide a way to construct modules from directed systems.  
8. Flat modules preserve exactness under tensor products.  
9. Tensor products commute with direct limits, a key property in homological algebra.  
10. The nilradical of a direct limit of rings is the direct limit of the nilradicals of the individual rings.

---

## Connections & Backlinks

- [[Chapter 1: Rings and Ideals]]: Modules generalize ideals, which were introduced in Chapter 1.  
- [[Chapter 3: Localization]]: Modules play a key role in localization and the study of local rings.  
- [[Exact Sequences]]: A foundational concept in homological algebra.  
- [[Tensor Products]]: Explored further in advanced algebra and algebraic geometry.  
- [[Nakayama's Lemma]]: Frequently used in module theory and commutative algebra.

---

## Further Reading

1. *Commutative Algebra* by H. Matsumura — for deeper insights into modules and their applications.  
2. *Algebra* by Serge Lang — provides an introduction to modules and their role in algebra.  
3. Online resources like [Math Stack Exchange](https://math.stackexchange.com/) for discussions on specific module theory problems.  

        ---
        *Generated by `ingest_chapters.py` · model: gpt-4o*
