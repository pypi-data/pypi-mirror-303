# sage_setup: distribution = sagemath-graphs
r"""
Free monoid generated by prime knots available via the
:class:`~sage.knots.knotinfo.KnotInfoBase` class.

A generator of this free abelian monoid is a prime knot according to
the list at `KnotInfo <https://knotinfo.math.indiana.edu/>`__. A fully
amphicheiral prime knot is represented by exactly one generator with
the corresponding name. For non-chiral prime knots, there are
additionally one or three generators with the suffixes ``m``, ``r``
and ``c`` which specify the mirror and reverse images according to
their symmetry type.

AUTHORS:

- Sebastian Oehms June 2024: initial version
"""

##############################################################################
#       Copyright (C) 2024 Sebastian Oehms <seb.oehms@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#                  http://www.gnu.org/licenses/
##############################################################################

from sage.knots.knotinfo import SymmetryMutant
from sage.monoids.indexed_free_monoid import (IndexedFreeAbelianMonoid,
                                              IndexedFreeAbelianMonoidElement)
from sage.misc.cachefunc import cached_method
from sage.structure.unique_representation import UniqueRepresentation


class FreeKnotInfoMonoidElement(IndexedFreeAbelianMonoidElement):
    """
    An element of an indexed free abelian monoid.
    """
    def as_knot(self):
        r"""
        Return the knot represented by ``self``.

        EXAMPLES::

            sage: from sage.knots.free_knotinfo_monoid import FreeKnotInfoMonoid
            sage: FKIM =  FreeKnotInfoMonoid()
            sage: FKIM.inject_variables(select=3)
            Defining K3_1
            Defining K3_1m
            sage: K = K3_1^2 * K3_1m
            sage: K.as_knot()
            Knot represented by 9 crossings
        """
        wl = self.to_word_list()
        P = self.parent()
        if len(wl) == 1:
            name = wl[0]
            L = P._index_dict[name][0].link()
            if name.endswith(SymmetryMutant.mirror_image.value):
                return L.mirror_image()
            if name.endswith(SymmetryMutant.reverse.value):
                return L.reverse()
            if name.endswith(SymmetryMutant.concordance_inverse.value):
                return L.mirror_image().reverse()
            return L
        else:
            from sage.misc.misc_c import prod
            return prod(P.gen(wl[i]).as_knot() for i in range(len(wl)))

    def to_knotinfo(self):
        r"""
        Return a word representing ``self`` as a list of pairs.

        Each pair ``(ki, sym)`` consists of a
        :class:`~sage.knots.knotinfo.KnotInfoBase` instance ``ki`` and
        :class:`~sage.knots.knotinfo.SymmetryMutant` instance ``sym``.

        EXAMPLES::

            sage: from sage.knots.free_knotinfo_monoid import FreeKnotInfoMonoid
            sage: FKIM =  FreeKnotInfoMonoid()
            sage: FKIM.inject_variables(select=3)
            Defining K3_1
            Defining K3_1m
            sage: K = K3_1^2 * K3_1m
            sage: K.to_knotinfo()
            [(<KnotInfo.K3_1: '3_1'>, <SymmetryMutant.itself: 's'>),
            (<KnotInfo.K3_1: '3_1'>, <SymmetryMutant.itself: 's'>),
            (<KnotInfo.K3_1: '3_1'>, <SymmetryMutant.mirror_image: 'm'>)]
        """
        wl = self.to_word_list()
        P = self.parent()
        return [P._index_dict[w] for w in wl]


class FreeKnotInfoMonoid(IndexedFreeAbelianMonoid):

    Element = FreeKnotInfoMonoidElement

    @staticmethod
    def __classcall_private__(cls, max_crossing_number=6, prefix=None, **kwds):
        r"""
        Normalize input to ensure a unique representation.

        EXAMPLES::

            sage: from sage.knots.free_knotinfo_monoid import FreeKnotInfoMonoid
            sage: FreeKnotInfoMonoid()
            Free abelian monoid of knots with at most 6 crossings
            sage: FreeKnotInfoMonoid(5)
            Free abelian monoid of knots with at most 5 crossings
        """
        if not prefix:
            prefix = 'KnotInfo'
        # We skip the IndexedMonoid__classcall__
        return UniqueRepresentation.__classcall__(cls, max_crossing_number,
                                                  prefix=prefix, **kwds)

    def __init__(self, max_crossing_number, category=None, prefix=None, **kwds):
        r"""
        Initialize ``self`` with generators belonging to prime knots with
        at most ``max_crossing_number`` crossings.

        TESTS:

            sage: from sage.knots.free_knotinfo_monoid import FreeKnotInfoMonoid
            sage: FKIM =  FreeKnotInfoMonoid()
            sage: FKIM4 =  FreeKnotInfoMonoid(4)
            sage: TestSuite(FKIM).run()
            sage: TestSuite(FKIM4).run()
        """
        self._max_crossing_number = None
        self._set_index_dictionary(max_crossing_number=max_crossing_number)
        from sage.sets.finite_enumerated_set import FiniteEnumeratedSet
        indices = FiniteEnumeratedSet(self._index_dict)
        super().__init__(indices, prefix)

    def _from_knotinfo(self, knotinfo, symmetry_mutant):
        r"""
        Return the name on the generator for the given ``symmetry_mutant``
        of the given entry ``knotinfo`` if the KnotInfo database.

        EXAMPLES::

            sage: from sage.knots.free_knotinfo_monoid import FreeKnotInfoMonoid
            sage: from sage.knots.knotinfo import SymmetryMutant
            sage: FKIM =  FreeKnotInfoMonoid()
            sage: ki = KnotInfo.K5_2
            sage: FKIM._from_knotinfo(ki, SymmetryMutant.itself)
            'K5_2'
            sage: FKIM._from_knotinfo(ki, SymmetryMutant.concordance_inverse)
            'K5_2c'
        """
        if symmetry_mutant == SymmetryMutant.itself:
            return knotinfo.name
        else:
            return '%s%s' % (knotinfo.name, symmetry_mutant.value)

    def _set_index_dictionary(self, max_crossing_number=6):
        r"""
        Set or expand the set of generators.
        EXAMPLES::

            sage: from sage.knots.free_knotinfo_monoid import FreeKnotInfoMonoid
            sage: FreeKnotInfoMonoid()
            Free abelian monoid of knots with at most 6 crossings

        TESTS::

            sage: from sage.features.databases import DatabaseKnotInfo
            sage: F = DatabaseKnotInfo()
            sage: F.hide()
            sage: FreeKnotInfoMonoid(7)  # indirect doctest
            Traceback (most recent call last):
            ...
            sage.features.FeatureNotPresentError: database_knotinfo is not available.
            Feature `database_knotinfo` is hidden.
            Use method `unhide` to make it available again.
            sage: F.unhide()
        """
        if max_crossing_number > 6:
            from sage.features.databases import DatabaseKnotInfo
            DatabaseKnotInfo().require()

        current_max_crossing_number = self._max_crossing_number
        if not current_max_crossing_number:
            current_max_crossing_number = - 1
            self._index_dict = {}
        self._max_crossing_number = max_crossing_number

        def add_index(ki, sym):
            self._index_dict[self._from_knotinfo(ki, sym)] = (ki, sym)

        from sage.knots.knotinfo import KnotInfo
        for K in KnotInfo:
            ncr = K.crossing_number()
            if ncr <= current_max_crossing_number:
                continue
            if ncr > self._max_crossing_number:
                break
            for sym in SymmetryMutant:
                if sym.is_minimal(K):
                    add_index(K, sym)
        if current_max_crossing_number > 0:
            from sage.sets.finite_enumerated_set import FiniteEnumeratedSet
            self._indices = FiniteEnumeratedSet(self._index_dict)

    def _repr_(self):
        """
        Return a string representation of ``self``.

        EXAMPLES::

          sage: from sage.knots.free_knotinfo_monoid import FreeKnotInfoMonoid
          sage: FreeKnotInfoMonoid(4)
          Free abelian monoid of knots with at most 4 crossings
        """
        return "Free abelian monoid of knots with at most %s crossings" % self._max_crossing_number

    def _element_constructor_(self, x=None):
        """
        Create an element of this abelian monoid from ``x``.

        EXAMPLES::

            sage: from sage.knots.free_knotinfo_monoid import FreeKnotInfoMonoid
            sage: FKIM =  FreeKnotInfoMonoid()
            sage: K = KnotInfo.K5_1.link().mirror_image()
            sage: FKIM(K)
            KnotInfo['K5_1m']
        """
        if isinstance(x, tuple):
            if len(x) == 2:
                ki, sym = x
                from sage.knots.knotinfo import KnotInfoBase
                if isinstance(ki, KnotInfoBase) and isinstance(sym, SymmetryMutant):
                    mcr = ki.crossing_number()
                    if mcr > self._max_crossing_number:
                        self._set_index_dictionary(max_crossing_number=mcr)

                    sym_min = min([sym] + sym.matches(ki))
                    return self.gen(self._from_knotinfo(ki, sym_min))

        from sage.knots.knot import Knot
        from sage.knots.link import Link
        if not isinstance(x, Knot):
            if isinstance(x, Link):
                x = Knot(x.pd_code())
        if isinstance(x, Knot):
            return self.from_knot(x)
        return self.element_class(self, x)

    @cached_method
    def _check_elements(self, knot, elems):
        r"""
        Return a matching item from the list in ``elems`` if it exists.
        Elsewise return ``None``. This is a helper method for .meth:`from_knot`.

        INPUT:

        - ``knot`` -- an instance of :class:`~sage.knots.knot.Knot`
        - ``elems`` -- a tuple of elements of ``self``

        EXAMPLES::

            sage: from sage.knots.free_knotinfo_monoid import FreeKnotInfoMonoid
            sage: FKIM =  FreeKnotInfoMonoid()
            sage: FKIM.inject_variables(select=3)
            Defining K3_1
            Defining K3_1m
            sage: elems = (K3_1, K3_1m)
            sage: K = Knots().from_table(3, 1)
            sage: FKIM._check_elements(K, elems)
            KnotInfo['K3_1m']
            sage: K = Knots().from_table(4, 1)
            sage: FKIM._check_elements(K, elems) is None
            True
        """
        for e in elems:
            k = e.as_knot()
            if knot.pd_code() == k.pd_code():
                return e
            if knot._markov_move_cmp(k.braid()):
                return e
        return None

    @cached_method
    def _search_composition(self, max_cr, knot, hpoly):
        r"""
        Add KnotInfo items to the list of candidates that have
        matching Homfly polynomial.

        INPUT:

        -  ``max_cr`` -- max number of crorssing to stop searching
        -  ``knot`` -- instance of :class:`~sage.knots.knot.Knot`
        -  ``hpoly`` -- Homfly polynomial to search for a component

        OUTPUT:

        A tuple of elements of ``self`` that match a (not necessarily prime or
        proper) component of the given knot having the given Homfly polynomial.

        EXAMPLES::

            sage: from sage.knots.free_knotinfo_monoid import FreeKnotInfoMonoid
            sage: FKIM =  FreeKnotInfoMonoid()
            sage: FKIM.inject_variables(select=3)
            Defining K3_1
            Defining K3_1m
            sage: KI = K3_1 * K3_1m
            sage: K = KI.as_knot()
            sage: h = K3_1.to_knotinfo()[0][0].homfly_polynomial()
            sage: FKIM._search_composition(3, K, h)
            (KnotInfo['K3_1'],)
        """
        from sage.knots.knotinfo import KnotInfo

        def hp_mirr(hp):
            v, z = hp.parent().gens()
            return hp.subs({v: ~v, z: z})

        former_cr = 3
        res = []
        for K in KnotInfo:
            if not K.is_knot():
                break
            c = K.crossing_number()
            if c < 3:
                continue
            if c > max_cr:
                break
            hp = K.homfly_polynomial()
            hp_sym = {s: hp for s in SymmetryMutant if s.is_minimal(K)}
            hpm = hp_mirr(hp)
            if hp != hpm:
                hp_sym[SymmetryMutant.mirror_image] = hpm
                if SymmetryMutant.concordance_inverse in hp_sym.keys():
                    hp_sym[SymmetryMutant.concordance_inverse] = hpm

            for sym_mut in hp_sym.keys():
                hps = hp_sym[sym_mut]
                if hps.divides(hpoly):
                    Kgen = self((K, sym_mut))
                    h = hpoly // hps
                    if h.is_unit():
                        res += [Kgen]
                    else:
                        res_rec = self._search_composition(max_cr - c, knot, h)
                        if res_rec:
                            res += [Kgen * k for k in res_rec]
            if c > former_cr and res:
                k = self._check_elements(knot, tuple(res))
                if k:
                    # matching item found
                    return tuple([k])
                former_cr = c

        return tuple(sorted(set(res)))

    @cached_method
    def _from_knot(self, knot):
        """
        Create a tuple of element of this abelian monoid which possibly
        represent ``knot``. This method caches the performance relevant
        part of :meth:`from_knot`.

        INPUT:

        - ``knot`` -- an instance of :class:`~sage.knots.knot.Knot`

        EXAMPLES::

            sage: from sage.knots.free_knotinfo_monoid import FreeKnotInfoMonoid
            sage: FKIM =  FreeKnotInfoMonoid()
            sage: K = KnotInfo.K5_1.link().mirror_image()
            sage: FKIM._from_knot(K)
            (KnotInfo['K5_1m'],)
        """
        hp = knot.homfly_polynomial(normalization='vz')
        return self._search_composition(13, knot, hp)

    def from_knot(self, knot, unique=True):
        """
        Create an element of this abelian monoid from ``knot``.

        INPUT:

        - ``knot`` -- an instance of :class:`~sage.knots.knot.Knot`

        - ``unique`` -- boolean (default is ``True``). This only affects the case
          where a unique identification is not possible. If set to ``False`` you
          can obtain a matching list (see explanation of the output below)

        OUTPUT:

        An instance of the element class of ``self`` per default. If the keyword
        argument ``unique`` then a list of such instances is returned.

        EXAMPLES::

            sage: from sage.knots.free_knotinfo_monoid import FreeKnotInfoMonoid
            sage: FKIM =  FreeKnotInfoMonoid()
            sage: K = KnotInfo.K5_1.link().mirror_image()
            sage: FKIM.from_knot(K)
            KnotInfo['K5_1m']

            sage: # optional - database_knotinfo
            sage: K = Knot(KnotInfo.K9_12.braid())
            sage: FKIM.from_knot(K)                   # long time
            Traceback (most recent call last):
            ...
            NotImplementedError: this (possibly non prime) knot cannot be
            identified uniquely by KnotInfo
            use keyword argument `unique` to obtain more details
            sage: FKIM.from_knot(K, unique=False)     # long time
            [KnotInfo['K4_1']*KnotInfo['K5_2'], KnotInfo['K9_12']]
        """
        hp = knot.homfly_polynomial(normalization='vz')
        num_summands = sum(e for _, e in hp.factor())
        if num_summands == 1:
            return knot.get_knotinfo()

        res = self._from_knot(knot)
        if res:
            if len(res) == 1:
                if unique:
                    return res[0]
                return [res[0]]  # to be consistent with get_knotinfo
            k = self._check_elements(knot, res)
            if k:
                if unique:
                    return k
                return [k]  # to be consistent with get_knotinfo

        if res and not unique:
            return sorted(set(res))
        if unique and len(res) > 1:
            non_unique_hint = '\nuse keyword argument `unique` to obtain more details'
            raise NotImplementedError('this (possibly non prime) knot cannot be identified uniquely by KnotInfo%s' % non_unique_hint)
        raise NotImplementedError('this (possibly non prime) knot cannot be identified by KnotInfo')

    def inject_variables(self, select=None, verbose=True):
        """
        Inject ``self`` with its name into the namespace of the
        Python code from which this function is called.

        INPUT:

        - ``select`` -- instance of :class:`~sage.knots.knotinfo.KnotInfoBase`,
          :class:`~sage.knots.knotinfo.KnotInfoSeries` or an integer. In all
          cases the input is used to restrict the injected generators to the
          according subset (number of crossings in the case of integer)
        - ``verbose`` -- boolean (optional, default ``True``) to suppress
          the message printed on the invocation

        EXAMPLES::

          sage: from sage.knots.free_knotinfo_monoid import FreeKnotInfoMonoid
          sage: FKIM = FreeKnotInfoMonoid(5)
          sage: FKIM.inject_variables(select=3)
          Defining K3_1
          Defining K3_1m
          sage: FKIM.inject_variables(select=KnotInfo.K5_2)
          Defining K5_2
          Defining K5_2m
          sage: FKIM.inject_variables(select=KnotInfo.K5_2.series())
          Defining K5_1
          Defining K5_1m
          sage: FKIM.inject_variables()
          Defining K0_1
          Defining K4_1
        """
        from sage.knots.knotinfo import KnotInfoBase, KnotInfoSeries
        from sage.rings.integer import Integer
        gen_list = []
        idx_dict = self._index_dict
        max_crn = self._max_crossing_number
        gens = self.gens()
        if select:
            if isinstance(select, KnotInfoBase):
                crn = select.crossing_number()
                if crn > max_crn:
                    self._set_index_dictionary(max_crossing_number=crn)
                gen_list += [k for k, v in idx_dict.items() if v[0] == select]
            elif isinstance(select, KnotInfoSeries):
                for v in select:
                    self.inject_variables(select=v)
                return
            elif type(select) is int or isinstance(select, Integer):
                crn = select
                if crn > max_crn:
                    self._set_index_dictionary(max_crossing_number=crn)
                gen_list += [k for k, v in idx_dict.items()
                             if v[0].crossing_number() == crn]
            else:
                raise TypeError('cannot select generators by %s' % select)
        else:
            gen_list = list(idx_dict.keys())

        from sage.repl.user_globals import set_global, get_globals
        for name in gen_list:
            if name not in get_globals().keys():
                set_global(name, gens[name])
                if verbose:
                    print("Defining %s" % (name))
