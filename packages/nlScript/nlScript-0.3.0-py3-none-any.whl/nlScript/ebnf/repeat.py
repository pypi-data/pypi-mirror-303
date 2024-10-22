from __future__ import annotations
from typing import TYPE_CHECKING, List, cast

from nlScript.ebnf.rule import Rule
from nlScript.core.production import ExtensionListener, DEFAULT_ASTBUILDER
from nlScript.evaluator import ALL_CHILDREN_EVALUATOR
from nlScript.parsednode import ParsedNode

if TYPE_CHECKING:
    from nlScript.core.nonterminal import NonTerminal
    from nlScript.core.symbol import Symbol
    from nlScript.core.bnf import BNF
    from nlScript.core.defaultparsednode import DefaultParsedNode


class Repeat(Rule):
    def __init__(self, tgt: NonTerminal or None, child: Symbol, rfrom: int, rto: int):
        super().__init__("repeat", tgt, [child])
        self._rfrom = rfrom
        self._rto = rto
        self.setEvaluator(ALL_CHILDREN_EVALUATOR)

    @property
    def rfrom(self) -> int:
        return self._rfrom

    @property
    def rto(self) -> int:
        return self._rto

    def getEntry(self) -> Symbol:
        return self._children[0]

    def createBNF(self, grammar: BNF):
        for seqLen in range(self._rto, self._rfrom - 1, -1):
            rhs = seqLen * [self.getEntry()]
            p = self.addProduction(grammar, self, self.tgt, rhs)

            def onExtension(parent: DefaultParsedNode, children: List[DefaultParsedNode]) -> None:
                for idx, child in enumerate(children):
                    ch = cast(ParsedNode, child)
                    ch.nthEntryInParent = idx
                    ch.name = self.getNameForChild(idx)
            p.onExtension = ExtensionListener(onExtension)

            p.astBuilder = DEFAULT_ASTBUILDER
