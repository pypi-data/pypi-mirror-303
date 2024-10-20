"""Expressions rationnelles simples"""


def parenthese(e, base):
    """Ajoute des parenthèses autour de [e] si la priorité le requiert"""
    if e.prio < base:
        return f"({e})"
    else:
        return f"{e}"


class Expression:
    def __lt__(self, other):
        return repr(self) < repr(other)

    def __gt__(self, other):
        return repr(self) > repr(other)

    def __eq__(self, other):
        return repr(self) == repr(other)

    def __hash__(self):
        return hash(repr(self))


class Lettre(Expression):
    """Mot d'une lettre"""

    __match_args__ = ("symbole",)

    def __init__(self, sym, meta=None):
        self.symbole = sym
        self.meta = meta
        self.prio = 99

    def __repr__(self):
        return f"Lettre({repr(self.symbole)}{', ' + repr(self.meta) if self.meta is not None else ''})"

    def __str__(self):
        return f"{self.symbole}"

    def arbre(self):
        return f"{self.symbole}"


class Epsilon(Expression):
    """Le mot vide"""

    def __init__(self, meta=None):
        self.meta = meta
        self.prio = 99

    def __repr__(self):
        return f"Epsilon({repr(self.meta) if self.meta is not None else ''})"

    def __str__(self):
        return f"1"

    def arbre(self):
        return f"1"


class EnsembleVide(Expression):
    """L'ensemble vide"""

    def __init__(self, meta=None):
        self.meta = meta
        self.prio = 99

    def __repr__(self):
        return f"EnsembleVide({repr(self.meta) if self.meta is not None else ''})"

    def __str__(self):
        return f"0"

    def arbre(self):
        return f"0"


class Somme(Expression):
    """Somme d'une expression [gauche] et d'une expression [droite]"""

    __match_args__ = ("gauche", "droite")

    def __init__(self, gauche, droite, meta=None):
        self.gauche = gauche
        self.droite = droite
        self.meta = meta
        self.prio = 1

    def __repr__(self):
        return f"Somme({repr(self.gauche)}, {repr(self.droite)}{', ' + repr(self.meta) if self.meta is not None else ''})"

    def __str__(self):
        return (
            f"{parenthese(self.gauche, self.prio)}+{parenthese(self.droite, self.prio)}"
        )

    def arbre(self):
        return ("+", self.gauche.arbre(), self.droite.arbre())


class Concat(Expression):
    """Concaténation d'une expression [gauche] et d'une expression [droite]"""

    __match_args__ = ("gauche", "droite")

    def __init__(self, gauche, droite, meta=None):
        self.gauche = gauche
        self.droite = droite
        self.meta = meta
        self.prio = 2

    def __repr__(self):
        return f"Concat({repr(self.gauche)}, {repr(self.droite)}{', ' + repr(self.meta) if self.meta is not None else ''})"

    def __str__(self):
        return (
            f"{parenthese(self.gauche, self.prio)}{parenthese(self.droite, self.prio)}"
        )

    def arbre(self):
        return ("·", self.gauche.arbre(), self.droite.arbre())


class Etoile(Expression):
    """Étoile de Kleene d'une expression [expr]"""

    __match_args__ = ("expr",)

    def __init__(self, expr, meta=None):
        self.expr = expr
        self.meta = meta
        self.prio = 3

    def __repr__(self):
        return f"Etoile({repr(self.expr)})"

    def __str__(self):
        return f"{parenthese(self.expr, self.prio)}*"

    def arbre(self):
        return ("*", self.expr.arbre())


class ErreurDeSyntaxe(Exception):
    def __init__(self, message):
        self.message = message


class Analyseur:
    """Analyseur syntaxique simple pour les expressions rationnelles suivant la grammaire ci-dessous.
     E, F ::= 0     # ensemble vide
            | 1     # mot vide
            | a     # lettre a
            | E + F # somme
            | EF    # produit
            | E*    # étoile de Kleene
            | (E)   # parenthèses
    exemple: a(b+c)*a
    """

    def __init__(self, annote=False):
        self.ops = ["("]
        self.exs = []
        self.pos = 0
        self.oprio = {"(": 0, "+": 1, "_": 2, "*": 3}
        self.inside = False
        self.annote = annote

    def pritop(self):
        if self.ops:
            return self.oprio[self.ops[-1]]
        else:
            return -99

    def popop(self):
        c = self.ops.pop()
        try:
            match c:
                case "+":
                    y = self.exs.pop()
                    x = self.exs.pop()
                    self.exs.append(Somme(x, y))
                case "_":
                    y = self.exs.pop()
                    x = self.exs.pop()
                    self.exs.append(Concat(x, y))
                case "*":
                    x = self.exs.pop()
                    self.exs.append(Etoile(x))
                case _:
                    raise ErreurDeSyntaxe(f"Opérateur {c} inconnu")
        except IndexError as exc:
            raise ErreurDeSyntaxe(
                f"Expression mal formée, opérateur en manque d'arguments"
            ) from exc

    def pushop(self, op):
        while self.oprio[op] < self.pritop():
            self.popop()
        self.ops.append(op)

    def poptopar(self):
        try:
            while self.pritop() != 0:
                self.popop()
            assert self.ops.pop() == "("
        except IndexError as exc:
            raise ErreurDeSyntaxe(f"Expression mal parenthésée") from exc

    def terminate(self):
        try:
            self.poptopar()
            assert not self.ops
            res = self.exs.pop()
            assert not self.exs
            return res
        except IndexError as exc:
            raise ErreurDeSyntaxe(f"Expression vide ?") from exc

    def read(self, c):
        match c:
            case " " | "\t":
                pass
            case "0":
                if self.inside:
                    self.pushop("_")
                self.exs.append(EnsembleVide())
                self.inside = True
            case "1":
                if self.inside:
                    self.pushop("_")
                self.exs.append(Epsilon())
                self.inside = True
            case "(":
                if self.inside:
                    self.pushop("_")
                self.ops.append("(")
                self.inside = False
            case ")":
                self.poptopar()
                self.inside = True
            case "+":
                self.pushop("+")
                self.inside = False
            case "*":
                self.pushop("*")
                self.inside = True
            case _:
                if self.inside:
                    self.pushop("_")
                self.pos += 1
                self.exs.append(Lettre(c, self.pos if self.annote else None))
                self.inside = True


def analyse(s, annote_pos=False):
    """Analyse la chaîne [s] et produit l'expression rationnelle qu'elle représente.
    Annote les lettres avec leur position si [annote_pos] vaut True"""
    ana = Analyseur(annote_pos)
    for c in s:
        ana.read(c)
    return ana.terminate()


def arbre(e):
    """Affiche l'arbre syntaxique de l'expression [e] grâce au module [svgling]"""
    import svgling

    return svgling.draw_tree(e.arbre())


def table_des_positions(e):
    """Retourne la liste des lettres pour chaque position de [e]"""
    match e:
        case Lettre(symbole=x):
            return [x]
        case EnsembleVide() | Epsilon():
            return []
        case Somme(gauche=e, droite=f):
            return table_des_positions(e) + table_des_positions(f)
        case Concat(gauche=e, droite=f):
            return table_des_positions(e) + table_des_positions(f)
        case Etoile(expr=e):
            return table_des_positions(e)


def alphabet(e):
    """Retourne l'alphabetbet d'une expression [e]"""
    match e:
        case Lettre(symbole=x):
            return set([x])
        case EnsembleVide() | Epsilon():
            return set()
        case Somme(gauche=e, droite=f):
            return alphabet(e).union(alphabet(f))
        case Concat(gauche=e, droite=f):
            return alphabet(e).union(alphabet(f))
        case Etoile(expr=e):
            return alphabet(e)
