"""Automates finis"""


class PasDEtatInitial(Exception):
    pass


class TransitionNonDefinie(Exception):
    pass


class LettreNonValide(Exception):
    pass


class AFD:
    """Automates finis déterministes partiels"""

    def __init__(self, alpha):
        """Crée un automate déterministe sur l'alphabet [alpha]"""
        self.etats = set()  # Q
        self.alpha = alpha  # A
        self.delta = dict()  # \delta
        self.initial = None  # q0
        self.acceptants = set()  # F

    def nouvel_etat(self, q, initial=False, acceptant=False):
        """Ajoute un nouvel état [q], éventuellement [initial] et/ou [acceptant]"""
        self.etats.add(q)
        if initial:
            self.initial = q
        if acceptant:
            self.acceptants.add(q)

    def marque_initial(self, q):
        """L'état [q] est dorénavant l'état initial"""
        assert q in self.etats
        self.initial = q

    def est_acceptant(self, q):
        """Teste si l'état [q] est acceptant"""
        return q in self.acceptants

    def marque_acceptant(self, q):
        """L'état [q] est dorénavant acceptant"""
        assert q in self.etats
        self.acceptants.add(q)

    def marque_non_acceptant(self, q):
        """L'état [q] est dorénavant non-acceptant"""
        assert q in self.etats
        self.acceptants.discard(q)

    def nouvelle_transition(self, p, a, q):
        """Ajoute la transition \delta(p,a)=q"""
        self.delta[(p, a)] = q

    def transition(self, q, u):
        """Retourne la transition \delta(q,u), peut retourner None"""
        cur = q
        for x in u:
            if cur is None:
                return None
            if x not in self.alpha:
                raise LettreNonValide
            cur = self.delta.get((cur, x), None)
        return cur

    def accepte(self, u):
        """Teste si le mot [u] est accepté par l'automate"""
        if self.initial is None:
            raise PasDEtatInitial
        q0 = self.initial
        dst = self.transition(q0, u)
        return self.est_acceptant(dst)

    def dessine(self, nommage=str):
        """Dessine l'automate à l'aide de graphviz, nomme les états avec [nommage]"""
        import graphviz

        dot = graphviz.Digraph(graph_attr={"rankdir": "LR"})
        if self.initial is not None:
            dot.node("0", shape="point")
        cur = 0
        m = dict()
        for q in self.etats:
            cur += 1
            s = str(cur)
            m[q] = s
            dot.node(
                s,
                nommage(q),
                shape="doublecircle" if q in self.acceptants else "circle",
            )
        arcs = {}
        for (p, a), q in self.delta.items():
            parcs = arcs.get(p, {})
            lq = parcs.get(q, [])
            lq.append(a)
            parcs[q] = lq
            arcs[p] = parcs
        for p, parcs in arcs.items():
            for q, lq in parcs.items():
                dot.edge(m[p], m[q], label=", ".join(map(str, lq)))
        if self.initial is not None:
            dot.edge("0", m[self.initial])
        return dot


class AFN:
    """Automates finis non-déterministes"""

    def __init__(self, alpha):
        """Crée un automate déterministe sur l'alphabet [alpha]"""
        self.etats = set()  # Q
        self.alpha = alpha  # A
        self.trans = dict()  # T
        self.initiaux = set()  # I
        self.acceptants = set()  # F

    def nouvel_etat(self, q, initial=False, acceptant=False):
        """Ajoute un nouvel état [q], éventuellement [initial] et/ou [acceptant]"""
        self.etats.add(q)
        if initial:
            self.initiaux.add(q)
        if acceptant:
            self.acceptants.add(q)

    def marque_initial(self, q):
        """L'état [q] est dorénavant initial"""
        assert q in self.etats
        self.initiaux.add(q)

    def marque_non_initial(self, q):
        """L'état [q] est dorénavant non initial"""
        assert q in self.etats
        self.initiaux.discard(q)

    def est_initial(self, q):
        """Teste si l'état [q] est initial"""
        return q in self.initiaux

    def est_acceptant(self, q):
        """Teste si l'état [q] est acceptant"""
        return q in self.acceptants

    def marque_acceptant(self, q):
        """L'état [q] est dorénavant acceptant"""
        assert q in self.etats
        self.acceptants.add(q)

    def marque_non_acceptant(self, q):
        """L'état [q] est dorénavant non-acceptant"""
        assert q in self.etats
        self.acceptants.discard(q)

    def nouvelle_transition(self, p, a, q):
        """Ajoute la transition \delta(p,a)=q"""
        d = self.trans.get((p, a), set())
        d.add(q)
        self.trans[(p, a)] = d

    def transition(self, X, u):
        """Retourne l'ensemble des états accessibles depuis l'ensemble d'états [X] ou l'état [X] en lisant [u]"""
        if isinstance(X, set):
            cur = set(X)
        else:
            cur = set([X])
        for x in u:
            if not cur:
                return set()
            if x not in self.alpha:
                raise LettreNonValide
            nxt = set()
            for p in cur:
                for q in self.trans.get((p, x), []):
                    nxt.add(q)
            cur = nxt
        return cur

    def accepte(self, u):
        """Teste si le mot [u] est accepté par l'automate"""
        for q in self.transition(self.initiaux, u):
            if self.est_acceptant(q):
                return True
        return False

    def dessine(self, nommage=str):
        """Dessine l'automate à l'aide de graphviz, nomme les états avec [nommage]"""
        import graphviz

        dot = graphviz.Digraph(graph_attr={"rankdir": "LR"})
        cur = 0
        m = dict()
        for q in self.etats:
            cur += 1
            s = str(cur)
            m[q] = s
            dot.node(
                s,
                nommage(q),
                shape="doublecircle" if q in self.acceptants else "circle",
            )
            if self.est_initial(q):
                dot.node("_" + s, str(q), shape="point")
                dot.edge("_" + s, s)
        arcs = {}
        for (p, a), l in self.trans.items():
            parcs = arcs.get(p, {})
            arcs[p] = parcs
            for q in l:
                lq = parcs.get(q, [])
                lq.append(a)
                parcs[q] = lq
        for p, parcs in arcs.items():
            for q, lq in parcs.items():
                dot.edge(m[p], m[q], label=", ".join(map(str, lq)))
        return dot
