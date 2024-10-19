# sage_setup: distribution = sagemath-combinat
# sage.doctest: needs sage.modules
r"""
Down-Up Algebras

AUTHORS:

- Travis Scrimshaw (2023-4): initial version
"""

# ****************************************************************************
#       Copyright (C) 2023 Travis Scrimshaw <tcscrims at gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#                  https://www.gnu.org/licenses/
# ****************************************************************************

from sage.misc.cachefunc import cached_method
from sage.categories.algebras import Algebras
from sage.categories.modules import Modules
from sage.categories.rings import Rings
from sage.combinat.free_module import CombinatorialFreeModule
from sage.sets.non_negative_integers import NonNegativeIntegers
from sage.categories.sets_cat import cartesian_product
from sage.sets.family import Family
from sage.misc.lazy_list import lazy_list
from sage.misc.misc_c import prod
from sage.modules.free_module import FreeModule


class DownUpAlgebra(CombinatorialFreeModule):
    r"""
    The down-up algebra.

    Let `R` be a commutative ring, and let `\alpha, \beta, \gamma \in R`.
    The *down-up algebra* is the associative unital algebra
    `DU(\alpha, \beta, \gamma)` generated by `d, u` with relations

    .. MATH::

        \begin{aligned}
        d^2u & = \alpha dud + \beta ud^2 + \gamma d,
        \\ du^2 & = \alpha udu + \beta u^2d + \gamma u.
        \end{aligned}

    The down-up algebra has a PBW-type basis given by

    .. MATH::

        \{ u^i (du)^j d^k \mid i,j,k \in \ZZ_{\geq 0} \}.

    This algebra originates in the study of posets. For a poset `P`,
    we define operators acting on `R[P]` by

    .. MATH::

        d(y) = \sum_x x \qquad\qquad u(y) = \sum_z z,

    where `y` covers `x` and `z` covers `y`. For `r`-differential posets
    we have `du - ud = r 1`, and thus it affords a representation of a
    :class:`Weyl algebra <sage.algebras.weyl_algebra.DifferentialWeylAlgebra>`.
    This Weyl algebra is obtained as the quotient of `DU(0, 1, 2r)` by the
    ideal generated by `du - ud - r`. For a `(q, r)`-differential poset,
    we have the `d` and `u` operators satisfying

    .. MATH::

        \begin{aligned}
        d^2u & = q(q+1) dud - q^3 ud^2 + r d,
        \\ du^2 & = q(q+1) udu - q^3 u^2d + r u,
        \end{aligned}

    or `\alpha = q(q+1)`, `\beta = -q^3`, and `\gamma = r`. Specializing
    `q = -1` recovers the `r`-differential poset relation.

    Two other noteworthy quotients are:

    - the `q`-Weyl algebra from `DU(0, q^2, q+1)` by the ideal generated by
      `du - qud - 1`, and
    - the quantum plane `R_q[d, u]`, where `du = qud`, from `DU(2q, -q^2, 0)`
      by the ideal generated by `du - qud`.

    EXAMPLES:

    We begin by constructing the down-up algebra and perform some
    basic computations::

        sage: R.<a,b,g> = QQ[]
        sage: DU = algebras.DownUp(a, b, g)
        sage: d, u = DU.gens()
        sage: d * u
        (d*u)
        sage: u * d
        u*d
        sage: d^2 * u
        b*u*d^2 + a*(d*u)*d + g*d
        sage: d * u^2
        b*u^2*d + a*u*(d*u) + g*u

    We verify some examples of Proposition 3.5 in [BR1998]_, which states
    that the `0`-th degree part is commutative::

        sage: DU0 = [u^i * (d*u)^j * d^i for i,j in
        ....:        cartesian_product([range(3), range(3)])]
        sage: all(x.degree() == 0 for x in DU0)
        True
        sage: all(x * y == y * x for x, y in cartesian_product([DU0, DU0]))
        True

    We verify that `DU(2, -1, \gamma)` can be described as the universal
    enveloping algebra of the 3-dimensional Lie algebra spanned by `x,y,z`
    satisfying `z = [x, y]`, `[x, z] = \gamma x`, and `[z, y] = \gamma y`::

        sage: R.<g> = QQ[]
        sage: L = LieAlgebra(R, {('x','y'): {'z': 1}, ('x','z'): {'x': g}, ('z','y'): {'y': g}},
        ....:                names='x,y,z')
        sage: x, y, z = L.basis()
        sage: (L[x, y], L[x, z], L[z, y])
        (z, g*x, g*y)
        sage: x, y, z = L.pbw_basis().gens()
        sage: x^2*y - 2*x*y*x + y*x^2 == g*x
        True
        sage: x*y^2 - 2*y*x*y + y^2*x == g*y
        True
        sage: DU = algebras.DownUp(2, -1, g)
        sage: d, u = DU.gens()
        sage: d^2*u - 2*d*u*d + u*d^2 == g*d
        True
        sage: d*u^2 - 2*u*d*u + u^2*d == g*u
        True

    Young's lattice is known to be a differential poset. Thus we can
    construct a representation of `DU(0, 1, 2)` on this poset (which
    gives a proof that Fomin's :class:`growth diagrams <GrowthDiagram>`
    are equivalent to edge local rules or shadow lines construction
    for :func:`RSK`)::

        sage: DU = algebras.DownUp(0, 1, 2)
        sage: d, u = DU.gens()
        sage: d^2*u == 0*d*u*d + 1*u*d*d + 2*d
        True
        sage: d*u^2 == 0*u*d*u + 1*u*u*d + 2*u
        True

        sage: YL = CombinatorialFreeModule(DU.base_ring(), Partitions())
        sage: def d_action(la):
        ....:     return YL.sum_of_monomials(la.remove_cell(*c) for c in la.removable_cells())
        sage: def u_action(la):
        ....:     return YL.sum_of_monomials(la.add_cell(*c) for c in la.addable_cells())
        sage: D = YL.module_morphism(on_basis=d_action, codomain=YL)
        sage: U = YL.module_morphism(on_basis=u_action, codomain=YL)
        sage: for la in PartitionsInBox(5, 5):
        ....:     b = YL.basis()[la]
        ....:     assert (D*D*U)(b) == 0*(D*U*D)(b) + 1*(U*D*D)(b) + 2*D(b)
        ....:     assert (D*U*U)(b) == 0*(U*D*U)(la) + 1*(U*U*D)(b) + 2*U(b)
        ....:     assert (D*U)(b) == (U*D)(b) + b  # the Weyl algebra relation

    .. TODO::

        Implement the homogenized version.

    REFERENCES:

    - [BR1998]_
    - [CM2000]_
    """
    @staticmethod
    def __classcall_private__(cls, alpha, beta, gamma, base_ring=None):
        r"""
        Standardize input to ensure a unique representation.

        TESTS::

            sage: R.<a,b,g> = QQ[]
            sage: DU1 = algebras.DownUp(a, 1, g)
            sage: DU2 = algebras.DownUp(a, R.one(), g)
            sage: DU3 = algebras.DownUp(a, 1, g, R)
            sage: DU1 is DU2 and DU2 is DU3
            True
        """
        if base_ring is None:
            from sage.structure.element import get_coercion_model
            base_ring = get_coercion_model().common_parent(alpha, beta, gamma)
        if base_ring not in Rings().Commutative():
            raise TypeError("base ring must be a commutative ring")
        alpha = base_ring(alpha)
        beta = base_ring(beta)
        gamma = base_ring(gamma)
        return super().__classcall__(cls, alpha, beta, gamma, base_ring=base_ring)

    def __init__(self, alpha, beta, gamma, base_ring):
        r"""
        Initialize ``self``.

        EXAMPLES::

            sage: R.<a,b,g> = QQ[]
            sage: DU = algebras.DownUp(a, b, g)
            sage: d, u = DU.gens()
            sage: elts = [d, u, d^2, u^2, d*u, u*d]
            sage: TestSuite(DU).run(elements=elts)
            sage: elts += [d*(d*u)*u]
            sage: TestSuite(DU).run(elements=elts)  # long time
        """
        self._alpha = alpha
        self._beta = beta
        self._gamma = gamma
        cat = Algebras(base_ring).WithBasis().Graded()
        if self._beta:
            from sage.categories.domains import Domains
            cat &= Domains()
        indices = cartesian_product([NonNegativeIntegers()] * 3)
        CombinatorialFreeModule.__init__(self, base_ring, indices, category=cat, sorting_reverse=True)
        self._assign_names(['d', 'u'])

    def _repr_(self):
        r"""
        Return a string representation of ``self``.

        EXAMPLES::

            sage: DU = algebras.DownUp(1, 2, 3)
            sage: DU
            Down-Up algebra with parameters (1, 2, 3) over Integer Ring
        """
        return "Down-Up algebra with parameters ({}, {}, {}) over {}".format(
            self._alpha, self._beta, self._gamma, self.base_ring())

    def _latex_(self):
        r"""
        Return a latex representation of ``self``.

        EXAMPLES::

            sage: R.<a,b,g> = QQ[]
            sage: DU = algebras.DownUp(a, b, g)
            sage: latex(DU)
            \mathcal{DU}(a,b,g)
        """
        return "\\mathcal{DU}(%s,%s,%s)" % (self._alpha, self._beta, self._gamma)

    def _repr_term(self, m):
        r"""
        Return a string representation of the basis element indexed by ``m``.

        EXAMPLES::

            sage: R.<a,b,g> = QQ[]
            sage: DU = algebras.DownUp(a, b, g)
            sage: I = DU.indices()
            sage: DU._repr_term(I([1,0,5]))
            'u*d^5'
            sage: DU._repr_term(I([6,3,1]))
            'u^6*(d*u)^3*d'
            sage: DU._repr_term(I([0,1,2]))
            '(d*u)*d^2'
            sage: DU._repr_term(I([0,0,0]))
            '1'
        """
        if not any(m):
            return '1'
        ret = ''
        for i, s in enumerate(['u', '(d*u)', 'd']):
            if not m[i]:
                continue
            if ret:
                ret += '*'
            if m[i] == 1:
                ret += s
            else:
                ret += f"{s}^{m[i]}"
        return ret

    def _latex_term(self, m):
        r"""
        Return a latex representation for the basis element indexed by ``m``.

        EXAMPLES::

            sage: R.<a,b,g> = QQ[]
            sage: DU = algebras.DownUp(a, b, g)
            sage: I = DU.indices()
            sage: DU._latex_term(I([1,0,5]))
            'ud^{5}'
            sage: DU._latex_term(I([6,3,1]))
            'u^{6}(du)^{3}d'
            sage: DU._latex_term(I([0,1,2]))
            '(du)d^{2}'
            sage: DU._latex_term(I([0,0,0]))
            '1'
        """
        if all(val == 0 for val in m):
            return '1'
        ret = ''
        for i, s in enumerate(['u', '(du)', 'd']):
            if not m[i]:
                continue
            if m[i] == 1:
                ret += s
            else:
                ret += f"{s}^{{{m[i]}}}"
        return ret

    @cached_method
    def algebra_generators(self):
        r"""
        Return the algebra generators of ``self``.

        EXAMPLES::

            sage: DU = algebras.DownUp(2, 3, 4)
            sage: dict(DU.algebra_generators())
            {'d': d, 'u': u}
        """
        u = self.monomial(self._indices([1,0,0]))
        d = self.monomial(self._indices([0,0,1]))
        return Family({'d': d, 'u': u})

    @cached_method
    def gens(self):
        r"""
        Return the generators of ``self``.

        EXAMPLES::

            sage: DU = algebras.DownUp(2, 3, 4)
            sage: DU.gens()
            (d, u)
        """
        G = self.algebra_generators()
        return (G['d'], G['u'])

    @cached_method
    def one_basis(self):
        r"""
        Return the index of the basis element of `1`.

        EXAMPLES::

            sage: DU = algebras.DownUp(2, 3, 4)
            sage: DU.one_basis()
            (0, 0, 0)
        """
        return self._indices([0, 0, 0])

    def product_on_basis(self, m1, m2):
        r"""
        Return the product of the basis elements indexed by ``m1`` and ``m2``.

        EXAMPLES::

            sage: R.<a,b,g> = QQ[]
            sage: DU = algebras.DownUp(a, b, g)
            sage: I = DU.indices()
            sage: DU.product_on_basis(I([2,0,0]), I([4,0,0]))
            u^6
            sage: DU.product_on_basis(I([2,0,0]), I([0,4,0]))
            u^2*(d*u)^4
            sage: DU.product_on_basis(I([2,0,0]), I([0,0,4]))
            u^2*d^4
            sage: DU.product_on_basis(I([0,2,0]), I([0,4,0]))
            (d*u)^6
            sage: DU.product_on_basis(I([0,2,0]), I([0,0,4]))
            (d*u)^2*d^4
            sage: DU.product_on_basis(I([0,0,2]), I([0,0,4]))
            d^6
            sage: DU.product_on_basis(I([5,3,1]), I([1,0,4]))
            u^5*(d*u)^4*d^4

            sage: DU.product_on_basis(I([0,1,0]), I([1,0,0]))
            b*u^2*d + a*u*(d*u) + g*u
            sage: DU.product_on_basis(I([0,0,2]), I([1,0,0]))
            b*u*d^2 + a*(d*u)*d + g*d
            sage: DU.product_on_basis(I([0,0,1]), I([2,0,0]))
            b*u^2*d + a*u*(d*u) + g*u
            sage: DU.product_on_basis(I([0,0,1]), I([0,1,0]))
            b*u*d^2 + a*(d*u)*d + g*d

            sage: DU.product_on_basis(I([0,1,0]), I([3,0,0]))
            (a^2*b+b^2)*u^4*d + (a^3+2*a*b)*u^3*(d*u) + (a^2*g+a*g+b*g+g)*u^3
            sage: DU.product_on_basis(I([1,1,3]), I([0,1,1]))
            (a^2*b^2+b^3)*u^3*d^6 + (a^3*b+a*b^2)*u^2*(d*u)*d^5 + (a^2*b*g+b^2*g)*u^2*d^5
             + (a^3+2*a*b)*u*(d*u)^2*d^4 + (a^2*g+a*g+b*g+g)*u*(d*u)*d^4
        """
        # Check trivial cases
        if not any(m1):
            return self.monomial(m2)
        if not any(m2):
            return self.monomial(m1)

        u1, du1, d1 = m1
        u2, du2, d2 = m2
        I = self._indices

        if not d1:
            if not u2:
                return self.monomial(I([u1, du1+du2, d2]))
            # else u2 > 0
            if not du1:
                return self.monomial(I([u1+u2, du2, d2]))
            # Perform du * u reduction
            lhs = self.monomial(I([u1, du1-1, 0]))
            mid = self._from_dict({I([1,1,0]): self._alpha,
                                   I([2,0,1]): self._beta,
                                   I([1,0,0]): self._gamma})
            rhs = self.monomial(I([u2-1, du2, d2]))
        else:  # d1 > 0
            if not u2:
                if not du2:
                    return self.monomial(I([u1, du1, d1+d2]))
                # Perform a d * du reduction
                lhs = self.monomial(I([u1, du1, d1-1]))
                mid = self._from_dict({I([0,1,1]): self._alpha,
                                       I([1,0,2]): self._beta,
                                       I([0,0,1]): self._gamma})
                rhs = self.monomial(I([0, du2-1, d2]))
            elif u2 > 1:
                # Perform d * u^2 reduction
                lhs = self.monomial(I([u1, du1, d1-1]))
                mid = self._from_dict({I([1,1,0]): self._alpha,
                                       I([2,0,1]): self._beta,
                                       I([1,0,0]): self._gamma})
                rhs = self.monomial(I([u2-2, du2, d2]))
            elif u2 == 1:
                if d1 == 1:
                    return self.monomial(I([u1, du1+du2+1, d2]))
                # Perform a d^2 * u reduction
                lhs = self.monomial(I([u1, du1, d1-2]))
                mid = self._from_dict({I([0,1,1]): self._alpha,
                                       I([1,0,2]): self._beta,
                                       I([0,0,1]): self._gamma})
                rhs = self.monomial(I([0, du2, d2]))

        if lhs == self.one():
            if rhs == self.one():
                return mid
            return mid * rhs
        if rhs == self.one():
            return lhs * mid
        return lhs * mid * rhs

    def degree_on_basis(self, m):
        r"""
        Return the degree of the basis element indexed by ``m``.

        EXAMPLES::

            sage: R.<a,b,g> = QQ[]
            sage: DU = algebras.DownUp(a, b, g)
            sage: I = DU.indices()
            sage: DU.degree_on_basis(I([0, 3, 2]))
            -2
            sage: DU.degree_on_basis(I([2, 3, 0]))
            2
            sage: DU.degree_on_basis(I([2, 0, 3]))
            -1
            sage: DU.degree_on_basis(I([3, 10, 3]))
            0
        """
        return m[0] - m[2]

    def verma_module(self, la):
        r"""
        Return the :class:`Verma module
        <sage.algebras.down_up_algebra.VermaModule>`
        `V(\lambda)` of ``self``.

        EXAMPLES::

            sage: R.<a,b,g> = QQ[]
            sage: DU = algebras.DownUp(a, b, g)
            sage: DU.verma_module(5)
            Verma module of weight 5 of Down-Up algebra with parameters (a, b, g)
             over Multivariate Polynomial Ring in a, b, g over Rational Field
        """
        return VermaModule(self, la)


class VermaModule(CombinatorialFreeModule):
    r"""
    The Verma module `V(\lambda)` of a down-up algebra.

    The Verma module `V(\lambda)` for the down-up algebra generated
    by `d, u` is the span of `\{v_n \mid n \in \ZZ_{\geq 0} \}`
    satisfying the relations

    .. MATH::

        d \cdot v_n = \lambda_{n-1} v_{n-1}, \qquad\qquad
        u \cdot v_n = v_{n+1},

    where `\lambda_n = \alpha \lambda_{n-1} + \beta \lambda_{n-2} + \gamma`
    and we set `\lambda_0 = \lambda` and `\lambda_{-1} = 0`.

    By Proposition 2.4 in [BR1998]_, `V(\lambda)` is simple if and
    only if `\lambda_n \neq 0` for all `n \geq 0`. Moreover, a maximal
    submodule is spanned by `\{ v_n \mid n > m \}`, where `m` is the
    minimal index such that `\lambda_m = 0`. Moreover, this is unique
    unless `\gamma = \lambda = 0`.

    EXAMPLES::

        sage: R.<a,b> = QQ[]
        sage: DU = algebras.DownUp(0, b, 1)
        sage: d, u = DU.gens()
        sage: V = DU.verma_module(a)
        sage: list(V.weights()[:6])
        [a, 1, a*b + 1, b + 1, a*b^2 + b + 1, b^2 + b + 1]
        sage: v = V.basis()
        sage: d^2 * v[2]
        a*v[0]
        sage: d * (d * v[2])
        a*v[0]

    The weight is computed by looking at the scalars associated to the
    action of `du` and `ud`::

        sage: d*u * v[3]
        (b+1)*v[3]
        sage: u*d * v[3]
        (a*b+1)*v[3]
        sage: v[3].weight()
        (b + 1, a*b + 1)

    An `U(\mathfrak{sl}_2)` example::

        sage: DU = algebras.DownUp(2, -1, -2)
        sage: d, u = DU.gens()
        sage: V = DU.verma_module(5)
        sage: list(V.weights()[:10])
        [5, 8, 9, 8, 5, 0, -7, -16, -27, -40]
        sage: v6 = V.basis()[6]
        sage: d * v6
        0
        sage: [V.basis()[i].weight() for i in range(6)]
        [(5, 0), (8, 5), (9, 8), (8, 9), (5, 8), (0, 5)]

    Note that these are the same `\mathfrak{sl}_2` weights from the usual
    construction of the irreducible representation `V(5)` (but they are
    different as `\mathfrak{gl}_2` weights)::

        sage: B = crystals.Tableaux(['A',1], shape=[5])                                 # needs sage.graphs
        sage: [b.weight() for b in B]                                                   # needs sage.graphs
        [(5, 0), (4, 1), (3, 2), (2, 3), (1, 4), (0, 5)]

    An example with periodic weights (see Theorem 2.13 of [BR1998]_)::

        sage: # needs sage.rings.number_field
        sage: k.<z6> = CyclotomicField(6)
        sage: al = z6 + 1
        sage: (al - 1)^6 == 1
        True
        sage: DU = algebras.DownUp(al, 1-al, 0)
        sage: V = DU.verma_module(5)
        sage: list(V.weights()[:8])
        [5, 5*z6 + 5, 10*z6, 10*z6 - 5, 5*z6 - 5, 0, 5, 5*z6 + 5]
    """
    @staticmethod
    def __classcall_private__(cls, DU, la):
        """
        Normalize input to ensure a unique representation.

        EXAMPLES::

            sage: R.<a,b,g> = QQ[]
            sage: DU = algebras.DownUp(a, b, g)
            sage: from sage.algebras.down_up_algebra import VermaModule
            sage: VermaModule(DU, 5) is VermaModule(DU, R(5))
            True
            sage: VermaModule(DU, 1/a)
            Traceback (most recent call last):
            ...
            TypeError: fraction must have unit denominator
        """
        R = DU.base_ring()
        la = R(la)
        return super().__classcall__(cls, DU, la)

    def __init__(self, DU, la):
        """
        Initialize ``self``.

        EXAMPLES::

            sage: R.<a,b,g> = QQ[]
            sage: DU = algebras.DownUp(a, b, g)
            sage: V = DU.verma_module(5)
            sage: TestSuite(V).run()
            sage: V = DU.verma_module(0)
            sage: TestSuite(V).run()

            sage: DU = algebras.DownUp(a, 0, g)
            sage: V = DU.verma_module(5)
            sage: TestSuite(V).run()
            sage: V = DU.verma_module(0)
            sage: TestSuite(V).run()

            sage: DU = algebras.DownUp(a, 1-a, 0)
            sage: V = DU.verma_module(5)
            sage: TestSuite(V).run()
            sage: V = DU.verma_module(0)
            sage: TestSuite(V).run()
        """
        self._DU = DU
        R = DU.base_ring()

        def _la_iter():
            m2 = la
            yield la
            m2 = R.zero()
            m1 = la
            while True:
                cur = DU._alpha * m1 + DU._beta * m2 + DU._gamma
                yield cur
                m2 = m1
                m1 = cur

        self._weights = lazy_list(_la_iter())
        cat = Modules(R).WithBasis()
        CombinatorialFreeModule.__init__(self, R, NonNegativeIntegers(),
                                         prefix='v', category=cat)

    def _repr_(self):
        r"""
        Return a string representation of ``self``.

        EXAMPLES::

            sage: DU = algebras.DownUp(1, 2, 3)
            sage: DU.verma_module(5)
            Verma module of weight 5 of Down-Up algebra with parameters (1, 2, 3) over Integer Ring
        """
        return f"Verma module of weight {self._weights[0]} of {self._DU}"

    def _latex_(self):
        r"""
        Return a latex representation of ``self``.

        EXAMPLES::

            sage: DU = algebras.DownUp(1, 2, 3)
            sage: latex(DU.verma_module(5))
            V\left(5\right)
        """
        return f"V\\left({self._weights[0]}\\right)"

    def highest_weight_vector(self):
        r"""
        Return the highest weight vector of ``self`` that generates
        ``self`` as a down-up module.

        EXAMPLES::

            sage: DU = algebras.DownUp(1, 2, 3)
            sage: V = DU.verma_module(5)
            sage: V.highest_weight_vector()
            v[0]
        """
        return self.basis()[0]

    def weights(self):
        r"""
        Return the sequence of weights `(\lambda_n)_{n=0}^{\infty}`.

        EXAMPLES::

            sage: R.<a,b,g> = QQ[]
            sage: DU = algebras.DownUp(a, b, g)
            sage: V = DU.verma_module(5)
            sage: V.weights()
            lazy list [5, 5*a + g, 5*a^2 + a*g + 5*b + g, ...]

            sage: V = DU.verma_module(0)
            sage: DU = algebras.DownUp(a, 1-a, 0)
            sage: V = DU.verma_module(0)
            sage: V.weights()
            lazy list [0, 0, 0, ...]

        We reproduce the Fibonacci numbers example from [BR1998]_::

            sage: R.<la> = QQ[]
            sage: DU = algebras.DownUp(1, 1, 0, R)
            sage: V = DU.verma_module(la)
            sage: list(V.weights()[:11])
            [la, la, 2*la, 3*la, 5*la, 8*la, 13*la, 21*la, 34*la, 55*la, 89*la]
        """
        return self._weights

    def _action_on_basis(self, m, n):
        r"""
        Return the action of a basis element of the down-up algebra indexed
        by ``m`` on the basis element of ``self`` indexed by ``n``.

        EXAMPLES::

            sage: R.<a,b,g> = QQ[]
            sage: DU = algebras.DownUp(0, b, 1)
            sage: I = DU.indices()
            sage: V = DU.verma_module(1)
            sage: V.weights()
            lazy list [1, 1, b + 1, ...]
            sage: V._action_on_basis(I([0,0,1]), 0)
            0
            sage: V._action_on_basis(I([0,1,0]), 0)
            v[0]
            sage: V._action_on_basis(I([1,0,0]), 0)
            v[1]

            sage: V._action_on_basis(I([0,0,1]), 3)
            (b+1)*v[2]
            sage: V._action_on_basis(I([0,1,0]), 3)
            (b+1)*v[3]
            sage: V._action_on_basis(I([1,0,0]), 3)
            v[4]

            sage: V._action_on_basis(I([0,0,3]), 3)
            (b+1)*v[0]
            sage: V._action_on_basis(I([1,2,1]), 3)
            (b^3+3*b^2+3*b+1)*v[3]

            sage: V = DU.verma_module(0)
            sage: V._action_on_basis(I([0,0,1]), 1)
            0
        """
        if m[2] > n:
            return self.zero()
        np = n - m[2]
        coeff = prod(self._weights[np:n]) * self._weights[np] ** m[1]
        return self.term(n - m[2] + m[0], coeff)

    class Element(CombinatorialFreeModule.Element):
        r"""
        An element of a Verma module of a down-up algebra.
        """
        def _acted_upon_(self, scalar, self_on_left):
            r"""
            Return the action of ``scalar`` (an element of the base ring or
            the defining down-up algebra) on ``self``.

            EXAMPLES::

                sage: R.<a,b> = QQ[]
                sage: DU = algebras.DownUp(0, b, 1)
                sage: d, u = DU.gens()
                sage: V = DU.verma_module(a)
                sage: it = iter(DU.basis())
                sage: scalars = [next(it) for _ in range(10)]; scalars
                [1, u, (d*u), d, u^2, u*(d*u), u*d, (d*u)^2, (d*u)*d, d^2]
                sage: vecs = [V.basis()[0], V.basis()[1], V.basis()[6]]
                sage: all((x * y) * v == x * (y * v)
                ....:     for x in scalars for y in scalars for v in vecs)
                True
                sage: 5 * V.basis()[3]
                5*v[3]
                sage: V.basis()[0] * d
                Traceback (most recent call last):
                ...
                TypeError: unsupported operand parent(s) for *:
                 'Verma module of weight a of Down-Up algebra ...'
                 and 'Down-Up algebra ...'
            """
            ret = super()._acted_upon_(scalar, self_on_left)
            if ret is not None:
                return ret
            P = self.parent()
            try:
                scalar = P._DU(scalar)
            except (TypeError, ValueError):
                return None
            if self_on_left:
                return None
            return P.linear_combination((P._action_on_basis(m, n), mc*nc)
                                        for m, mc in scalar._monomial_coefficients.items()
                                        for n, nc in self._monomial_coefficients.items())

        def is_weight_vector(self):
            r"""
            Return if ``self`` is a weight vector.

            EXAMPLES::

                sage: DU = algebras.DownUp(2, -1, -2)
                sage: V = DU.verma_module(5)
                sage: V.zero().is_weight_vector()
                False
                sage: B = V.basis()
                sage: [B[i].weight() for i in range(6)]
                [(5, 0), (8, 5), (9, 8), (8, 9), (5, 8), (0, 5)]
                sage: B[5].is_weight_vector()
                True
                sage: v = B[0] + B[1]
                sage: v.is_weight_vector()
                False

                sage: DU = algebras.DownUp(2, -1, 0)
                sage: V = DU.verma_module(0)
                sage: B = V.basis()
                sage: v = sum(i*B[i] for i in range(1,5))
                sage: v.is_weight_vector()
                True
            """
            if not self:
                return False

            P = self.parent()
            R = P.base_ring()
            weights = P._weights

            def get_wt(n):
                if not n:
                    return (R(P._weights[0]), R.zero())
                return (R(P._weights[n]), R(P._weights[n-1]))

            it = iter(self._monomial_coefficients)
            wt = get_wt(next(it))
            return all(get_wt(n) == wt for n in it)

        def weight(self):
            r"""
            Return the weight of ``self``.

            For `v_n`, this is the vector with the pair
            `(\lambda_n, \lambda_{n-1})`.

            EXAMPLES::

                sage: R.<a,b,g> = QQ[]
                sage: DU = algebras.DownUp(a, b, g)
                sage: V = DU.verma_module(5)
                sage: B = V.basis()
                sage: B[0].weight()
                (5, 0)
                sage: B[1].weight()
                (5*a + g, 5)
                sage: B[2].weight()
                (5*a^2 + a*g + 5*b + g, 5*a + g)

                sage: V.zero().weight()
                Traceback (most recent call last):
                ...
                ValueError: the zero element does not have well-defined weight
                sage: (B[0] + B[1]).weight()
                Traceback (most recent call last):
                ...
                ValueError: not a weight vector
            """
            if not self:
                raise ValueError("the zero element does not have well-defined weight")
            if not self.is_weight_vector():
                raise ValueError("not a weight vector")
            P = self.parent()
            R = P.base_ring()
            V = FreeModule(R, 2)
            weights = P._weights
            it = iter(self._monomial_coefficients)
            n = next(it)
            if not n:
                return V([P._weights[0], R.zero()])
            return V([P._weights[n], P._weights[n-1]])
