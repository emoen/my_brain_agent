        ---
        title: "Ch 10: Completions"
        book: "introduction to commutative algebra"
        source: "introduction_to_commutative_algebra.pdf"
        pages: "110–125"
        chapter: 10
        type: chapter-summary
        status: auto-generated
        model: gpt-4o
        date: 2026-06-12
        tags: [knowledge-base, auto-ingested, chapter-note]
        ---

        # Chapter 10: Completions

        > *Auto-generated rich summary — introduction to commutative algebra*
        > *Pages 110–125 | Ingested 2026-06-12*

        # Chapter 10: Completions

This article provides a comprehensive summary of Chapter 10 ("Completions") from the graduate textbook *Introduction to Commutative Algebra*. The chapter explores the concept of completions in commutative algebra, with a focus on topological methods, inverse limits, and $a$-adic topologies. It presents key results, including the exactness of completion, properties of graded rings and modules, and the Noetherian property of completed rings. The chapter culminates with applications such as Hensel's Lemma and the faithful flatness of power series rings.

---

## Overview

The concept of completion is a cornerstone of modern commutative algebra, with applications in algebraic geometry, number theory, and algebraic topology. This chapter introduces the completion of rings and modules with respect to an ideal, using both topological and categorical approaches. The completion process simplifies algebraic structures by focusing on their local behavior, often making problems more tractable. For example, $p$-adic numbers arise as completions of the integers with respect to the $p$-adic topology, and formal power series rings are completions of polynomial rings.

The chapter develops the theory of completions in the context of topological abelian groups and modules, emphasizing the role of $a$-adic topologies and filtrations. It establishes the exactness of completion for finitely-generated modules over Noetherian rings and proves that the $a$-adic completion of a Noetherian ring is Noetherian. Key tools include the Artin-Rees Lemma, the theory of graded rings and modules, and the interplay between completions and inverse limits. The chapter also discusses Hensel's Lemma, a fundamental result for lifting solutions of polynomial equations from residue fields to complete local rings.

---

## Definitions & Notation

1. **Topological Abelian Group**:
   - A group $G$ that is both a topological space and an abelian group, where addition and negation are continuous.

2. **$a$-adic Topology**:
   - For a ring $A$ and an ideal $a$, the $a$-adic topology on $A$ is defined by taking the powers $a^n$ as a fundamental system of neighborhoods of $0$.

3. **Completion of a Topological Abelian Group**:
   - The completion $\widehat{G}$ of a topological abelian group $G$ is the set of equivalence classes of Cauchy sequences in $G$.

4. **Inverse Limit**:
   - For an inverse system of groups $\{A_n, \phi_n\}$, the inverse limit $\varprojlim A_n$ is the set of coherent sequences $(a_n)$ such that $\phi_n(a_{n+1}) = a_n$.

5. **Graded Ring**:
   - A ring $A$ is graded if $A = \bigoplus_{n=0}^\infty A_n$ and $A_i A_j \subseteq A_{i+j}$.

6. **$a$-adic Completion of a Module**:
   - For an $A$-module $M$, the $a$-adic completion $\widehat{M}$ is the inverse limit $\varprojlim M/a^nM$.

7. **Zariski Ring**:
   - A Noetherian topological ring whose topology is defined by an ideal contained in the Jacobson radical.

8. **Hensel's Lemma**:
   - A result that allows lifting factorizations or roots of polynomials from residue fields to complete local rings.

---

## Theorems, Lemmas & Corollaries

### Lemma 10.1
**Statement**:  
Let $H$ be the intersection of all neighborhoods of $0$ in a topological abelian group $G$. Then:
1. $H$ is a subgroup of $G$.
2. $H$ is the closure of $\{0\}$.
3. $G/H$ is Hausdorff.
4. $G$ is Hausdorff if and only if $H = 0$.

---

### Proposition 10.2
**Statement**:  
Let $0 \to \{A_n\} \to \{B_n\} \to \{C_n\} \to 0$ be an exact sequence of inverse systems. Then:
1. $0 \to \varprojlim A_n \to \varprojlim B_n \to \varprojlim C_n$ is always exact.
2. If $\{A_n\}$ is a surjective system, then $0 \to \varprojlim A_n \to \varprojlim B_n \to \varprojlim C_n \to 0$ is exact.

---

### Theorem 10.17 (Krull's Theorem)
**Statement**:  
Let $A$ be a Noetherian ring, $a$ an ideal, and $M$ a finitely-generated $A$-module. Then the kernel $E = \bigcap_{n=1}^\infty a^n M$ of the natural map $M \to \widehat{M}$ consists of elements annihilated by some element of $1 + a$.

---

### Corollary 10.27
**Statement**:  
If $A$ is a Noetherian ring, the power series ring $B = A[[x_1, \dots, x_n]]$ in $n$ variables is Noetherian.

---

### Hensel's Lemma
**Statement**:  
Let $A$ be a local ring with maximal ideal $m$, and assume $A$ is $m$-adically complete. Let $f(x) \in A[x]$ be a monic polynomial of degree $n$, and let $\overline{f(x)} \in (A/m)[x]$ denote its reduction modulo $m$. If $\overline{f(x)} = g(x)h(x)$, where $g(x)$ and $h(x)$ are coprime monic polynomials in $(A/m)[x]$, then $g(x)$ and $h(x)$ can be lifted to monic polynomials in $A[x]$ such that $f(x) = g(x)h(x)$.

---

## Proof Ideas

### Lemma 10.1
- The proof relies on the continuity of group operations and the properties of topological spaces. The key insight is that $H$ is the smallest closed subgroup containing $0$, and its cosets partition $G$ into equivalence classes.

### Proposition 10.2
- The proof uses the definition of inverse limits and exact sequences, constructing commutative diagrams to verify the exactness of the induced sequence.

### Hensel's Lemma
- The proof uses an iterative lifting process, leveraging the completeness of $A$ to ensure convergence of the lifted polynomials $g(x)$ and $h(x)$.

---

## Worked Examples & Constructions

1. **Completion of $\mathbb{Z}$**:
   - The $p$-adic completion of $\mathbb{Z}$ is the ring of $p$-adic integers $\mathbb{Z}_p$.

2. **Formal Power Series**:
   - The $x$-adic completion of $k[x]$ (polynomials over a field $k$) is $k[[x]]$, the ring of formal power series.

3. **Convergent Power Series**:
   - The ring of power series $B$ converging near the origin in $\mathbb{C}^n$ has its completion as the ring of formal power series $C$.

---

## Exercises (Selected)

1. **Exercise 6**: Prove that $a$ is contained in the Jacobson radical of $A$ if and only if every maximal ideal of $A$ is closed in the $a$-topology.
2. **Exercise 9**: Prove Hensel's Lemma and apply it to lift roots and factorizations.
3. **Exercise 12**: Show that $A[[x_1, \dots, x_n]]$ is faithfully flat over $A$.

---

## Key Insights

1. Completion simplifies algebraic structures by focusing on local behavior.
2. The $a$-adic topology is central to defining completions.
3. Completions of Noetherian rings are Noetherian.
4. Hensel's Lemma is a powerful tool for lifting solutions in complete local rings.
5. Power series rings over Noetherian rings are Noetherian and faithfully flat.

---

## Connections & Backlinks

- [[Chapter 2: Modules]]: Exact sequences and module properties.
- [[Chapter 6: Noetherian Rings]]: Noetherian properties and their preservation under completion.
- [[Chapter 7: Graded Rings]]: Graded structures in completions.
- [[Chapter 8: Flatness]]: Flatness of completions and power series rings.

---

## Further Reading

1. Matsumura, H. *Commutative Ring Theory*. Springer.
2. Eisenbud, D. *Commutative Algebra with a View Toward Algebraic Geometry*. Springer.
3. Atiyah, M.F., Macdonald, I.G. *Introduction to Commutative Algebra*. Oxford University Press.

        ---
        *Generated by `ingest_chapters.py` · model: gpt-4o*
