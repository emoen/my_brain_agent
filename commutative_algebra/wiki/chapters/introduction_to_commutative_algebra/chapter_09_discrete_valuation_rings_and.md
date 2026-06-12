        ---
        title: "Ch 9: Discrete Valuation Rings and"
        book: "introduction to commutative algebra"
        source: "introduction_to_commutative_algebra.pdf"
        pages: "103–109"
        chapter: 9
        type: chapter-summary
        status: auto-generated
        model: gpt-4o
        date: 2026-06-12
        tags: [knowledge-base, auto-ingested, chapter-note]
        ---

        # Chapter 9: Discrete Valuation Rings and

        > *Auto-generated rich summary — introduction to commutative algebra*
        > *Pages 103–109 | Ingested 2026-06-12*

        # Discrete Valuation Rings and Dedekind Domains

This article summarizes Chapter 9 of *Introduction to Commutative Algebra*, which focuses on discrete valuation rings (DVRs), Dedekind domains, and their properties. The chapter explores the structure of one-dimensional Noetherian domains, emphasizing their role in algebraic number theory and algebraic geometry. It provides a rigorous treatment of the unique factorization of ideals, the concept of fractional ideals, and the interplay between local and global properties of rings.

Dedekind domains generalize the notion of unique factorization domains (UFDs) to the setting of ideals, where every non-zero ideal factors uniquely into prime ideals. This property makes them central to the study of algebraic integers and number fields. Discrete valuation rings, which are local one-dimensional Noetherian domains with a single non-zero prime ideal, serve as the building blocks of Dedekind domains through localization. The chapter also introduces the ideal class group, a key invariant in algebraic number theory.

---

## Definitions & Notation

### Discrete Valuation
A **discrete valuation** on a field $K$ is a function $v: K^* \to \mathbb{Z}$ (where $K^* = K \setminus \{0\}$) satisfying:
1. $v(xy) = v(x) + v(y)$ for all $x, y \in K^*$ (multiplicative property),
2. $v(x + y) \geq \min(v(x), v(y))$ for all $x, y \in K^*$, with equality if $v(x) \neq v(y)$ (non-Archimedean property).

The set $\{0\} \cup \{x \in K^* : v(x) \geq 0\}$ forms a ring called the **valuation ring** of $v$.

### Discrete Valuation Ring (DVR)
An integral domain $A$ is a **discrete valuation ring** if it is the valuation ring of a discrete valuation $v$ on its field of fractions $K$. Equivalently, $A$ is a DVR if it is a Noetherian local domain of dimension 1, and its maximal ideal is principal.

### Fractional Ideal
Let $A$ be an integral domain with field of fractions $K$. An $A$-submodule $M \subseteq K$ is a **fractional ideal** if there exists $x \in A \setminus \{0\}$ such that $xM \subseteq A$. If $M \subseteq A$, it is called an **integral ideal**.

### Invertible Ideal
A fractional ideal $M$ is **invertible** if there exists another fractional ideal $N$ such that $MN = A$. The inverse $N$ is unique and given by $(A : M) = \{x \in K : xM \subseteq A\}$.

### Dedekind Domain
An integral domain $A$ is a **Dedekind domain** if:
1. $A$ is Noetherian,
2. $A$ is integrally closed,
3. Every non-zero prime ideal of $A$ is maximal.

Equivalently, $A$ is a Dedekind domain if every non-zero fractional ideal of $A$ is invertible.

### Ideal Class Group
The **ideal class group** of a Dedekind domain $A$ is the quotient $H = I / P$, where $I$ is the group of non-zero fractional ideals of $A$ under multiplication, and $P$ is the subgroup of principal fractional ideals.

---

## Theorems, Lemmas & Corollaries

### Proposition 9.1
**Statement:** Let $A$ be a Noetherian domain of dimension 1. Then every non-zero ideal $a$ in $A$ can be uniquely expressed as a product of primary ideals whose radicals are all distinct.

---

### Proposition 9.2
**Statement:** Let $A$ be a Noetherian local domain of dimension 1, $m$ its maximal ideal, and $k = A/m$ its residue field. The following are equivalent:
1. $A$ is a discrete valuation ring,
2. $A$ is integrally closed,
3. $m$ is a principal ideal,
4. $\dim_k(m/m^2) = 1$,
5. Every non-zero ideal is a power of $m$,
6. There exists $x \in A$ such that every non-zero ideal is of the form $(x^k)$ for $k \geq 0$.

---

### Theorem 9.3
**Statement:** Let $A$ be a Noetherian domain of dimension 1. The following are equivalent:
1. $A$ is integrally closed,
2. Every primary ideal in $A$ is a prime power,
3. Every local ring $A_{\mathfrak{p}}$ ($\mathfrak{p} \neq 0$) is a discrete valuation ring.

---

### Corollary 9.4
**Statement:** In a Dedekind domain, every non-zero ideal has a unique factorization as a product of prime ideals.

---

### Theorem 9.5
**Statement:** The ring of integers in an algebraic number field $K$ is a Dedekind domain.

---

### Proposition 9.6
**Statement:** For a fractional ideal $M$, the following are equivalent:
1. $M$ is invertible,
2. $M$ is finitely generated and, for each prime ideal $\mathfrak{p}$, $M_{\mathfrak{p}}$ is invertible,
3. $M$ is finitely generated and, for each maximal ideal $m$, $M_m$ is invertible.

---

### Proposition 9.7
**Statement:** Let $A$ be a local domain. Then $A$ is a discrete valuation ring if and only if every non-zero fractional ideal of $A$ is invertible.

---

### Theorem 9.8
**Statement:** Let $A$ be an integral domain. Then $A$ is a Dedekind domain if and only if every non-zero fractional ideal of $A$ is invertible.

---

## Proof Ideas

### Proposition 9.2
The equivalences are established using integrality arguments, Nakayama's lemma, and primary decomposition. For example, $(iii) \implies (iv)$ uses the fact that $m$ being principal implies $\dim_k(m/m^2) = 1$, while $(v) \implies (vi)$ constructs a generator $x$ for $m$.

### Theorem 9.8
The proof connects the invertibility of fractional ideals to the Noetherian property and the discrete valuation ring structure of localizations. Localization at non-zero prime ideals reduces the problem to the case of DVRs.

---

## Worked Examples & Constructions

### Example 1: Principal Ideal Domains
Any principal ideal domain (PID) is a Dedekind domain because it is Noetherian, of dimension 1, and integrally closed. For example, $\mathbb{Z}$ is a Dedekind domain.

### Example 2: Ring of Integers in Number Fields
The ring of integers in an algebraic number field, such as $\mathbb{Z}[i]$ (the Gaussian integers), is a Dedekind domain. It satisfies the Noetherian property, is integrally closed, and has maximal non-zero prime ideals.

---

## Exercises (selected)

1. **Localization of Dedekind Domains**: Prove that the localization of a Dedekind domain at a prime ideal is a discrete valuation ring.
2. **Gauss's Lemma**: Show that the content of the product of two polynomials is the product of their contents in a Dedekind domain.
3. **Chinese Remainder Theorem**: Prove the Chinese Remainder Theorem for ideals in a Dedekind domain.

---

## Key Insights

1. Discrete valuation rings are one-dimensional Noetherian local domains with a single non-zero prime ideal.
2. Dedekind domains generalize UFDs by allowing unique factorization of ideals into prime ideals.
3. Fractional ideals are central to the structure of Dedekind domains, and their invertibility is a key property.
4. The ideal class group measures the failure of a Dedekind domain to be a PID.
5. Localizing a Dedekind domain at a non-zero prime ideal yields a discrete valuation ring.
6. The ring of integers in an algebraic number field is a canonical example of a Dedekind domain.
7. The Chinese Remainder Theorem holds for Dedekind domains, enabling modular arithmetic with ideals.

---

## Connections & Backlinks

- [[Noetherian Rings and Modules]]
- [[Integral Dependence and Valuation Rings]]
- [[Primary Decomposition]]
- [[Unique Factorization Domains]]

---

## Further Reading

- *Algebraic Number Theory* by J.W.S. Cassels and A. Fröhlich.
- *Commutative Ring Theory* by H. Matsumura.
- *Algebraic Number Theory* by Serge Lang.

        ---
        *Generated by `ingest_chapters.py` · model: gpt-4o*
