from __future__ import annotations

from nlScript.core.bnf import BNF
from nlScript.core.lexer import Lexer
from nlScript.core.parsingstate import ParsingState
from nlScript.core.rdparser import RDParser
from nlScript.core.terminal import DIGIT, literal
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
    rule = grammar.orrule("or", [
        grammar.sequence("seq1", [
                literal("y").withName(),
                DIGIT.withName()
        ]).withName("seq"),
        grammar.sequence("seq2", [
                literal("n").withName(),
                DIGIT.withName()
        ]).withName("seq")
    ])
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
    assertEquals(1, parsed.numChildren())

    child = parsed.getChild(0)
    assertEquals(input, child.getParsedString())
    assertEquals(2, child.numChildren())

    # test evaluate
    evaluated = parsed.evaluateSelf()
    assertEquals(input, evaluated)

    # test names
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
    print("test1")
    testSuccess("y1")


def test2():
    print("test2")
    testSuccess("n3")


def test3():
    print("test3")
    testFailure("")


def test4():
    print("test4")
    testFailure("s")


if __name__ == "__main__":
    test1()
    test2()
    test3()
    test4()
