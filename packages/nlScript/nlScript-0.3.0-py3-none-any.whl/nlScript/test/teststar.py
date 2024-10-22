from __future__ import annotations

from typing import List, cast

from nlScript.core.bnf import BNF
from nlScript.core.lexer import Lexer
from nlScript.core.parsingstate import ParsingState
from nlScript.core.rdparser import RDParser
from nlScript.core.terminal import DIGIT, LETTER
from nlScript.ebnf import ebnfparsednodefactory
from nlScript.ebnf.ebnfcore import EBNFCore
from nlScript.core import graphviz
from nlScript.parsednode import ParsedNode
from nlScript.parseexception import ParseException


def assertEquals(exp, real):
    if exp != real:
        raise Exception("Expected " + str(exp) + ", but got " + str(real))


def assertNotEquals(exp, real):
    if exp == real:
        raise Exception("Expected " + str(exp) + ", but got " + str(real))


def makeGrammar() -> BNF:
    grammar = EBNFCore()
    rule = grammar.star("star",
        grammar.sequence("seq", [
                DIGIT.withName(),
                LETTER.withName()
        ]).withName("seq"))
    grammar.compile(rule.tgt)
    return grammar.getBNF()


def testSuccess(input: str):
    grammar = makeGrammar()
    lexer = Lexer(input)
    parser = RDParser(grammar, lexer, ebnfparsednodefactory.INSTANCE)
    root = parser.parse()
    print(graphviz.toVizDotLink(root))

    assertEquals(ParsingState.SUCCESSFUL, root.matcher.state)

    parsed: ParsedNode = root.children[0]
    assertEquals(len(input) // 2, parsed.numChildren())

    idx = 0
    for child in parsed.children:
        assertEquals(input[idx:idx+2], child.getParsedString())
        assertEquals(2, child.numChildren())
        idx += 2

    # test evaluate
    evaluated = cast(List, parsed.evaluateSelf())
    for idx, ev in enumerate(evaluated):
        assertEquals(input[2 * idx: 2 * idx + 2], ev)

    # test names
    for child in parsed.children:
        assertEquals("seq", child.name)


def testFailure(input: str):
    grammar = makeGrammar()
    lexer = Lexer(input)
    parser = RDParser(grammar, lexer, ebnfparsednodefactory.INSTANCE)
    try:
        root = parser.parse()
        assertNotEquals(ParsingState.SUCCESSFUL, root.matcher.state)
    except ParseException:
        pass


def test1():
    testSuccess("1a2b3c")


def test2():
    testSuccess("1a")


def test3():
    testSuccess("")


def test4():
    testFailure("s")


if __name__ == "__main__":
    test1()
    test2()
    test3()
    test4()
