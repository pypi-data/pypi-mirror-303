# sage_setup: distribution = sagemath-combinat
# sage.doctest: needs sage.combinat sage.modules
r"""
Lie Conformal Algebra

Let `R` be a commutative ring, a *super Lie conformal algebra*
[Kac1997]_ over `R`
(also known as a *vertex Lie algebra*) is an `R[T]` super module `L`
together with a `\mathbb{Z}/2\mathbb{Z}`-graded `R`-bilinear
operation (called the `\lambda`-bracket)
`L\otimes L \rightarrow L[\lambda]`
(polynomials in `\lambda` with
coefficients in `L`), `a \otimes b \mapsto [a_\lambda b]` satisfying

1. Sesquilinearity:

   .. MATH::

        [Ta_\lambda b] = - \lambda [a_\lambda b], \qquad [a_\lambda Tb] =
        (\lambda+ T) [a_\lambda b].

2. Skew-Symmetry:

   .. MATH::

        [a_\lambda b] = - (-1)^{p(a)p(b)} [b_{-\lambda - T} a],

   where `p(a)` is `0` if `a` is *even* and `1` if `a` is *odd*. The
   bracket in the RHS is computed as follows. First we evaluate
   `[b_\mu a]` with the formal
   parameter `\mu` to the *left*, then
   replace each appearance of the formal variable `\mu` by `-\lambda - T`.
   Finally apply `T` to the coefficients in `L`.

3. Jacobi identity:

   .. MATH::

       [a_\lambda [b_\mu c]] = [ [a_{\lambda + \mu} b]_\mu c] +
       (-1)^{p(a)p(b)} [b_\mu [a_\lambda c ]],

   which is understood as an equality in `L[\lambda,\mu]`.

   `T` is usually called the *translation operation* or the *derivative*.
   For an element `a \in L` we will say that `Ta` is the *derivative of*
   `a`. We define the *`n`-th products* `a_{(n)} b` for `a,b \in L` by

   .. MATH::

        [a_\lambda b] = \sum_{n \geq 0} \frac{\lambda^n}{n!} a_{(n)} b.

   A Lie conformal algebra is called *H-Graded* [DSK2006]_ if there exists
   a decomposition `L = \oplus L_n` such that the
   `\lambda`-bracket becomes graded of degree `-1`, that is:

   .. MATH::

        a_{(n)} b \in L_{p + q -n -1} \qquad
        a \in L_p, \: b \in L_q, \: n \geq 0.

   In particular this implies that the action of `T` increases
   degree by `1`.

.. NOTE::

    In the literature arbitrary gradings are allowed. In this
    implementation we only support nonnegative rational gradings.

EXAMPLES:

1. The **Virasoro** Lie conformal algebra `Vir` over a ring `R`
   where `12` is invertible has two generators `L, C` as an `R[T]`-module.
   It is the direct sum of a free module of rank `1` generated by `L`, and
   a free rank one `R` module generated by `C` satisfying `TC = 0`.  `C`
   is central (the `\lambda`-bracket of `C` with any other vector
   vanishes). The remaining `\lambda`-bracket is given by

   .. MATH::

        [L_\lambda L] = T L + 2 \lambda L + \frac{\lambda^3}{12} C.

2. The **affine** or current Lie conformal algebra `L(\mathfrak{g})`
   associated to a finite dimensional Lie algebra `\mathfrak{g}` with
   non-degenerate, invariant `R`-bilinear form `(,)` is given as a central
   extension of the free
   `R[T]` module generated by `\mathfrak{g}` by a central element `K`. The
   `\lambda`-bracket of generators is given by

   .. MATH::

        [a_\lambda b] = [a,b] + \lambda (a,b) K, \qquad a,b \in \mathfrak{g}

3. The **Weyl** Lie conformal algebra, or `\beta-\gamma` system is
   given as the central extension of a free `R[T]` module with two
   generators `\beta` and `\gamma`, by a central element `K`.
   The only non-trivial brackets among generators are

   .. MATH::

        [\beta_\lambda \gamma] = - [\gamma_\lambda \beta] = K

4. The **Neveu-Schwarz** super Lie conformal algebra is a super Lie
   conformal algebra which is an extension of the Virasoro Lie conformal
   algebra. It consists of a Virasoro generator `L` as in example 1 above
   and an *odd* generator `G`. The remaining brackets are given by:

   .. MATH::

        [L_\lambda G] = \left( T + \frac{3}{2} \lambda \right) G \qquad
        [G_\lambda G] = 2 L + \frac{\lambda^2}{3} C

.. SEEALSO::

    :mod:`sage.algebras.lie_conformal_algebras.examples`

The base class for all Lie conformal algebras is
:class:`LieConformalAlgebra`.
All subclasses are called through its method ``__classcall_private__``.
This class provides no functionality besides calling the appropriate
constructor.

We provide some convenience classes to define named Lie conformal
algebras. See
:mod:`sage.algebras.lie_conformal_algebras.examples`.

EXAMPLES:

- We construct the Virasoro Lie conformal algebra, its universal
  enveloping vertex algebra and lift some elements::

    sage: Vir = lie_conformal_algebras.Virasoro(QQ)
    sage: Vir.inject_variables()
    Defining L, C
    sage: L.bracket(L)
    {0: TL, 1: 2*L, 3: 1/2*C}

- We construct the Current algebra for `\mathfrak{sl}_2`::

    sage: R = lie_conformal_algebras.Affine(QQ, 'A1', names = ('e', 'h', 'f'))
    sage: R.gens()
    (e, h, f, K)
    sage: R.inject_variables()
    Defining e, h, f, K
    sage: e.bracket(f.T())
    {0: Th, 1: h, 2: 2*K}
    sage: e.T(3)
    6*T^(3)e

- We construct the `\beta-\gamma` system by directly giving the
  `\lambda`-brackets of the generators::

    sage: betagamma_dict = {('b','a'):{0:{('K',0):1}}}
    sage: V = LieConformalAlgebra(QQ, betagamma_dict, names=('a','b'), weights=(1,0), central_elements=('K',))
    sage: V.category()
    Category of H-graded finitely generated Lie conformal algebras with basis over Rational Field
    sage: V.inject_variables()
    Defining a, b, K
    sage: a.bracket(b)
    {0: -K}

AUTHORS:

- Reimundo Heluani (2019-08-09): Initial implementation.
"""


#******************************************************************************
#       Copyright (C) 2019 Reimundo Heluani <heluani@potuz.net>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#                  http://www.gnu.org/licenses/
#*****************************************************************************

from sage.structure.unique_representation import UniqueRepresentation
from sage.sets.family import Family
from sage.categories.commutative_rings import CommutativeRings
from sage.structure.parent import Parent


class LieConformalAlgebra(UniqueRepresentation, Parent):
    r"""
    Lie Conformal Algebras base class and factory.

    INPUT:

    - ``R`` -- a commutative ring (default: ``None``); the base
      ring of this Lie conformal algebra. Behaviour is undefined
      if it is not a field of characteristic zero.

    - ``arg0`` -- dictionary (default: ``None``);
      a dictionary containing the `\lambda` brackets of the
      generators of this Lie conformal algebra. The keys of this
      dictionary are pairs of either names or indices of the
      generators and the values are themselves dictionaries. For a
      pair of generators ``'a'`` and ``'b'``, the value of
      ``arg0[('a','b')]`` is a dictionary whose keys are positive
      integer numbers and the corresponding value for the
      key ``j`` is a dictionary itself representing the `j`-th product
      `a_{(j)}b`. Thus, for a positive integer number `j`, the
      value of ``arg0[('a','b')][j]`` is a dictionary whose entries
      are pairs ``('c',n)`` where ``'c'`` is the name of a generator
      and ``n`` is a positive number. The value for this key is the
      coefficient of `\frac{T^{n}}{n!} c` in `a_{(j)}b`. For
      example the ``arg0`` for the *Virasoro* Lie conformal algebra
      is::

            {('L','L'):{0:{('L',1):1}, 1:{('L',0):2}, 3:{('C',0):1/2}}}


      Do not include central elements as keys in this dictionary. Also,
      if the key ``('a','b')`` is present, there is no need to include
      ``('b','a')`` as it is defined by skew-symmetry. Any missing
      pair (besides the ones defined by skew-symmetry) is assumed
      to have vanishing `\lambda`-bracket.

    - ``names`` -- tuple of strings (default: ``None``); the list of
      names for generators of this Lie conformal algebra. Do not
      include central elements in this list.

    - ``central_elements`` -- tuple of strings (default: ``None``);
      a list of names for central elements of this Lie conformal algebra

    - ``index_set`` -- enumerated set (default: ``None``); an
      indexing set for the generators of this Lie conformal algebra.
      Do not include central elements in this list.

    - ``weights`` -- tuple of nonnegative rational numbers
      (default: ``None``); a list of degrees for this Lie
      conformal algebra.
      The returned Lie conformal algebra is H-Graded. This tuple
      needs to have the same cardinality as ``index_set`` or
      ``names``. Central elements are assumed to have weight `0`.

    - ``parity`` -- tuple of `0` or `1` (default: tuple of `0`);
      if this is a super Lie conformal algebra, this tuple
      specifies the parity of each of the non-central generators of
      this Lie conformal algebra. Central elements are assumed to
      be even. Notice that if this tuple is present, the category
      of this Lie conformal algebra is set to be a subcategory of
      ``LieConformalAlgebras(R).Super()``, even if all generators
      are even.

    - ``category`` -- the category that this Lie conformal algebra
      belongs to

    In addition we accept the following keywords:

    - ``graded`` -- boolean (default: ``False``);
      if ``True``, the returned algebra is H-Graded.
      If ``weights`` is not specified, all non-central generators
      are assigned degree `1`. This keyword is ignored if
      ``weights`` is specified

    - ``super`` -- boolean (default: ``False``);
      if ``True``, the returned algebra is a super
      Lie conformal algebra even if all generators are even.
      If ``parity`` is not specified, all generators are
      assigned even parity. This keyword is ignored if
      ``parity`` is specified.

    .. Note::

        Any remaining keyword is currently passed to
        :class:`CombinatorialFreeModule<sage.combinat.free_module.CombinatorialFreeModule>`.

    EXAMPLES:

    We construct the `\beta-\gamma` system or *Weyl* Lie conformal
    algebra::

        sage: betagamma_dict = {('b','a'):{0:{('K',0):1}}}
        sage: V = LieConformalAlgebra(QQbar, betagamma_dict, names=('a','b'), weights=(1,0), central_elements=('K',))
        sage: V.category()
        Category of H-graded finitely generated Lie conformal algebras with basis over Algebraic Field
        sage: V.inject_variables()
        Defining a, b, K
        sage: a.bracket(b)
        {0: -K}

    We construct the current algebra for `\mathfrak{sl}_2`::

        sage: sl2dict = {('e','f'):{0:{('h',0):1}, 1:{('K',0):1}}, ('e','h'):{0:{('e',0):-2}}, ('f','h'):{0:{('f',0):2}}, ('h', 'h'):{1:{('K', 0):2}}}
        sage: V = LieConformalAlgebra(QQ, sl2dict, names=('e', 'h', 'f'), central_elements=('K',), graded=True)
        sage: V.inject_variables()
        Defining e, h, f, K
        sage: e.bracket(f)
        {0: h, 1: K}
        sage: h.bracket(e)
        {0: 2*e}
        sage: e.bracket(f.T())
        {0: Th, 1: h, 2: 2*K}
        sage: V.category()
        Category of H-graded finitely generated Lie conformal algebras with basis over Rational Field
        sage: e.degree()
        1

    .. TODO::

        This class checks that the provided dictionary is consistent
        with skew-symmetry. It does not check that it is consistent
        with the Jacobi identity.

    .. SEEALSO::

        :mod:`sage.algebras.lie_conformal_algebras.graded_lie_conformal_algebra`
    """
    @staticmethod
    def __classcall_private__(cls, R=None, arg0=None, index_set=None,
                              central_elements=None, category=None,
                              prefix=None, names=None, latex_names=None,
                              parity=None, weights=None, **kwds):
        """
        Lie conformal algebra factory.

        EXAMPLES::

            sage: betagamma_dict = {('b','a'):{0:{('K',0):1}}}
            sage: V = LieConformalAlgebra(QQ, betagamma_dict, names=('a','b'), weights=(1,0), central_elements=('K',))
            sage: type(V)
            <class 'sage.algebras.lie_conformal_algebras.graded_lie_conformal_algebra.GradedLieConformalAlgebra_with_category'>
        """
        if R not in CommutativeRings():
            raise ValueError(f"arg0 must be a commutative ring got {R}")

        # This is the only exposed class so we clean keywords here
        known_keywords = ['category', 'prefix', 'bracket', 'latex_bracket',
                          'string_quotes', 'sorting_key', 'graded', 'super']
        for key in kwds:
            if key not in known_keywords:
                raise ValueError("got an unexpected keyword argument '%s'" % key)

        if isinstance(arg0,dict) and arg0:
            graded = kwds.pop("graded", False)
            if weights is not None or graded:
                from .graded_lie_conformal_algebra import \
                                                    GradedLieConformalAlgebra
                return GradedLieConformalAlgebra(R, Family(arg0),
                    index_set=index_set, central_elements=central_elements,
                    category=category, prefix=prefix, names=names,
                    latex_names=latex_names, parity=parity, weights=weights,
                    **kwds)
            else:
                from .lie_conformal_algebra_with_structure_coefs import \
                        LieConformalAlgebraWithStructureCoefficients
                return LieConformalAlgebraWithStructureCoefficients(R,
                       Family(arg0), index_set=index_set,
                       central_elements=central_elements, category=category,
                       prefix=prefix, names=names, latex_names=latex_names,
                       parity=parity, **kwds)
        raise NotImplementedError("not implemented")
