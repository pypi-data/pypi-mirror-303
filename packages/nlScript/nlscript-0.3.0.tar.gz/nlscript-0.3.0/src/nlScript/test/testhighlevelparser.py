from typing import cast, List

from nlScript.core import graphviz
from nlScript.core.bnf import BNF
from nlScript.core.lexer import Lexer
from nlScript.core.named import Named
from nlScript.core.nonterminal import NonTerminal
from nlScript.core.parsingstate import ParsingState
from nlScript.core.rdparser import RDParser
from nlScript.core.symbol import Symbol
from nlScript.core.terminal import characterClass, Literal, Terminal, CharacterClass, DIGIT
from nlScript.ebnf import ebnfparsednodefactory
from nlScript.ebnf.ebnf import EBNF
from nlScript.ebnf.join import Join
from nlScript.ebnf.plus import Plus

from nlScript.ebnf.repeat import Repeat
from nlScript.ebnf.star import Star
from nlScript.evaluator import Evaluator
from nlScript.parsednode import ParsedNode
from nlScript.parseexception import ParseException
from nlScript.parser import Parser
from nlScript.util.range import OPTIONAL, STAR, PLUS, Range


def assertEquals(exp, real):
    if exp != real:
        raise Exception("Expected " + str(exp) + ", but got " + str(real))


def assertNotEquals(exp, real):
    if exp == real:
        raise Exception("Expected " + str(exp) + ", but got " + str(real))


def evaluate(grammar: EBNF, input: str) -> object:
    lexer = Lexer(input)
    parser = RDParser(grammar.getBNF(), lexer, ebnfparsednodefactory.INSTANCE)
    p = parser.parse()
    print(graphviz.toVizDotLink(p))

    return p.evaluate()


def checkFailed(grammar: BNF, input: str) -> None:
    lexer = Lexer(input)
    parser = RDParser(grammar, lexer, ebnfparsednodefactory.INSTANCE)
    try:
        p = parser.parse()
        if p.matcher.state == ParsingState.SUCCESSFUL:
            raise Exception("Expected failure")
    except ParseException:
        pass



def testQuantifier():
    print("Test Quantifier")
    hlp = Parser()
    grammar = hlp.grammar
    grammar.compile(hlp.QUANTIFIER.tgt)

    assertEquals(OPTIONAL, evaluate(grammar, "?"))
    assertEquals(STAR, evaluate(grammar, "*"))
    assertEquals(PLUS, evaluate(grammar, "+"))
    assertEquals(Range(1, 5), evaluate(grammar, "1-5"))
    assertEquals(Range(3), evaluate(grammar, "3"))


def testIdentifier():
    print("Test Identifier")
    hlp = Parser()
    grammar = hlp.grammar
    grammar.compile(hlp.IDENTIFIER.tgt)
    print(grammar)

    positives = ["bla", "_1-lkj", "A", "_"]
    negatives = ["-abc", "abc-"]

    for test in positives:
        print("Testing " + test)
        assertEquals(test, evaluate(grammar, test))

    for test in negatives:
        print("Testing " + test)
        checkFailed(grammar.getBNF(), test)


def evaluateHighlevelParser(hlp: Parser, input: str) -> object:
    lexer = Lexer(input)
    parser = RDParser(hlp.grammar.getBNF(), lexer, ebnfparsednodefactory.INSTANCE)
    p = parser.parse()
    if p.matcher.state is not ParsingState.SUCCESSFUL:
        raise Exception("Parsing failed")
    return p.evaluate()


def testList():
    print("Test List")
    hlp = Parser()
    grammar = hlp.grammar
    grammar.compile(hlp.LIST.tgt)

    test = "list<int>"
    list = cast(Join, evaluateHighlevelParser(hlp, test))

    # now parse and evaluate the generated grammar:
    tgt = hlp.targetGrammar
    tgt.compile(list.tgt)
    rdParser = RDParser(tgt.getBNF(), Lexer("1, 2, 3"), ebnfparsednodefactory.INSTANCE)
    pn = rdParser.parse()
    assertEquals(ParsingState.SUCCESSFUL, pn.matcher.state)
    result = cast(List[int], pn.evaluate())

    assertEquals(1, result[0])
    assertEquals(2, result[1])
    assertEquals(3, result[2])


def testTuple():
    print("Test Tuple")
    hlp = Parser()
    grammar = hlp.grammar
    grammar.compile(hlp.TUPLE.tgt)

    test = "tuple<int,x, y>"
    tuple = cast(NonTerminal, evaluateHighlevelParser(hlp, test))

    # now parse and evaluate the generated grammar:
    tgt = hlp.targetGrammar
    tgt.compile(tuple)
    rdParser = RDParser(tgt.getBNF(), Lexer("(1, 2)"), ebnfparsednodefactory.INSTANCE)

    pn = rdParser.parse()
    print(graphviz.toVizDotLink(pn))

    assertEquals(ParsingState.SUCCESSFUL, pn.matcher.state)
    result = cast(List[int], pn.evaluate())

    assertEquals(1, result[0])
    assertEquals(2, result[1])


def testCharacterClass():
    print("Test Character Class")
    hlp = Parser()
    grammar = hlp.grammar
    grammar.compile(hlp.CHARACTER_CLASS.tgt)

    nt: CharacterClass = cast(CharacterClass, evaluate(grammar, "[a-zA-Z]"))
    assertEquals(characterClass("[a-zA-Z]"), nt)


def testType():
    hlp = Parser()
    grammar = hlp.grammar
    grammar.compile(hlp.TYPE.tgt)

    # test tuple
    test = "tuple<int,x,y,z>"
    tuple = cast(NonTerminal, evaluateHighlevelParser(hlp, test))

    # now parse and evaluate the generated grammar:
    tgt = hlp.targetGrammar
    tgt.compile(tuple)
    rdParser = RDParser(tgt.getBNF(), Lexer("(1, 2, 3)"), ebnfparsednodefactory.INSTANCE)
    pn = rdParser.parse()
    assertEquals(ParsingState.SUCCESSFUL, pn.matcher.state)
    print(graphviz.toVizDotLink(pn))
    result = cast(List[int], pn.evaluate())

    assertEquals(1, result[0])
    assertEquals(2, result[1])

    # test list
    hlp = Parser()
    grammar = hlp.grammar
    grammar.compile(hlp.TYPE.tgt)
    test = "list<int>"
    list = cast(Join, evaluateHighlevelParser(hlp, test))

    # now parse and evaluate the generated grammar:
    tgt = hlp.targetGrammar
    tgt.compile(list.tgt)
    rdParser = RDParser(tgt.getBNF(), Lexer("1, 2, 3"), ebnfparsednodefactory.INSTANCE)
    pn = rdParser.parse()
    print(graphviz.toVizDotLink(pn))
    assertEquals(ParsingState.SUCCESSFUL, pn.matcher.state)
    result = cast(List[int], pn.evaluate())

    assertEquals(1, result[0])
    assertEquals(2, result[1])
    assertEquals(3, result[2])

    # test identifier
    hlp = Parser()
    grammar = hlp.grammar
    grammar.compile(hlp.TYPE.tgt)
    test = "int"
    identifier = cast(NonTerminal, evaluateHighlevelParser(hlp, test))

    # now parse and evaluate the generated grammar:
    tgt = hlp.targetGrammar
    tgt.compile(identifier)
    rdParser = RDParser(tgt.getBNF(), Lexer("3"), ebnfparsednodefactory.INSTANCE)
    pn = rdParser.parse()
    print(graphviz.toVizDotLink(pn))
    assertEquals(ParsingState.SUCCESSFUL, pn.matcher.state)
    assertEquals(3, pn.evaluate())


def testVariable():
    print("Test Variable")
    hlp = Parser()
    grammar = hlp.grammar
    grammar.compile(hlp.VARIABLE.tgt)

    test = "{bla:int:3-5}"
    evaluatedNonTerminal = cast(Named[NonTerminal], evaluateHighlevelParser(hlp, test))
    assertEquals("bla", evaluatedNonTerminal.name)
    rule = hlp.targetGrammar.getRules(evaluatedNonTerminal.get())[0]
    assertEquals(Repeat, type(rule))
    repeat = cast(Repeat, rule)
    assertEquals(3, repeat.rfrom)
    assertEquals(5, repeat.rto)
    assertEquals(EBNF.INTEGER_NAME, repeat.getEntry().symbol)

    test = "{blubb:digit}"
    evaluatedNonTerminal = cast(Named[NonTerminal], evaluateHighlevelParser(hlp, test))
    assertEquals("blubb", evaluatedNonTerminal.name)
    assertEquals(DIGIT.symbol, evaluatedNonTerminal.getSymbol().symbol)

    test = "{blubb:int:*}"
    evaluatedNonTerminal = cast(Named[NonTerminal], evaluateHighlevelParser(hlp, test))
    assertEquals("blubb", evaluatedNonTerminal.name)
    rule = hlp.targetGrammar.getRules(evaluatedNonTerminal.get())[0]
    assertEquals(Star, type(rule))
    star = cast(Star, rule)
    assertEquals(EBNF.INTEGER_NAME, star.getEntry().symbol)

    test = "{blubb:[A-Z]:+}"
    evaluatedNonTerminal = cast(Named[NonTerminal], evaluateHighlevelParser(hlp, test))
    assertEquals("blubb", evaluatedNonTerminal.name)
    rule = hlp.targetGrammar.getRules(evaluatedNonTerminal.get())[0]
    assertEquals(Plus, type(rule))
    plus = cast(Plus, rule)
    chclass: Symbol = plus.getEntry()
    assertEquals("[A-Z]", chclass.symbol)

    test = "{blubb , alkjad asd 4. <>l}"
    evaluatedTerminal = cast(Named[Terminal], evaluateHighlevelParser(hlp, test))
    literal: Literal = cast(Literal, evaluatedTerminal.get())
    assertEquals("blubb , alkjad asd 4. <>l", literal.getLiteral())
    assertEquals("blubb , alkjad asd 4. <>l", evaluatedTerminal.name)

    test = "{heinz}"
    evaluatedTerminal = cast(Named[Terminal], evaluateHighlevelParser(hlp, test))
    literal: Literal = cast(Literal, evaluatedTerminal.get())
    assertEquals("heinz", literal.getLiteral())
    assertEquals("heinz", evaluatedTerminal.name)

    test = "{heinz:+}"
    evaluatedNonTerminal = cast(Named[NonTerminal], evaluateHighlevelParser(hlp, test))
    assertEquals("heinz", evaluatedNonTerminal.name)
    rule = hlp.targetGrammar.getRules(evaluatedNonTerminal.get())[0]
    assertEquals(Plus, type(rule))
    plus = cast(Plus, rule)
    literal: Literal = cast(Literal, plus.getEntry())
    assertEquals("heinz", literal.getLiteral())

    test = "{heinz:3-5}"
    evaluatedNonTerminal = cast(Named[NonTerminal], evaluateHighlevelParser(hlp, test))
    assertEquals("heinz", evaluatedNonTerminal.name)
    rule = hlp.targetGrammar.getRules(evaluatedNonTerminal.get())[0]
    assertEquals(Repeat, type(rule))
    repeat = cast(Repeat, rule)
    assertEquals(3, repeat.rfrom)
    assertEquals(5, repeat.rto)
    literal: Literal = cast(Literal, repeat.getEntry())
    assertEquals("heinz", literal.getLiteral())

    test = "{, }"
    evaluatedTerminal = cast(Named[Terminal], evaluateHighlevelParser(hlp, test))
    literal: Literal = cast(Literal, evaluatedTerminal.get())
    assertEquals(", ", literal.getLiteral())
    assertEquals(", ", evaluatedTerminal.name)

    test = "{,\n }"
    evaluatedTerminal = cast(Named[Terminal], evaluateHighlevelParser(hlp, test))
    literal: Literal = cast(Literal, evaluatedTerminal.get())
    assertEquals(",\n ", literal.getLiteral())
    assertEquals(",\n ", evaluatedTerminal.name)


def testNoVariable():
    print("Test NoVariable")
    hlp = Parser()
    grammar = hlp.grammar
    grammar.compile(hlp.NO_VARIABLE.tgt)

    test = "lk345}.-"
    evaluatedTerminal = cast(Named[Terminal], evaluateHighlevelParser(hlp, test))
    assertEquals(Literal, type(evaluatedTerminal.get()))
    literal: Literal = cast(Literal, evaluatedTerminal.get())
    assertEquals(test, literal.getLiteral())
    assertEquals(test, evaluatedTerminal.name)

    test = "--1'x}"
    evaluatedTerminal = cast(Named[Terminal], evaluateHighlevelParser(hlp, test))
    assertEquals(Literal, type(evaluatedTerminal.get()))
    literal: Literal = cast(Literal, evaluatedTerminal.get())
    assertEquals(test, literal.getLiteral())
    assertEquals(test, evaluatedTerminal.name)

    test = "."
    evaluatedTerminal = cast(Named[Terminal], evaluateHighlevelParser(hlp, test))
    assertEquals(Literal, type(evaluatedTerminal.get()))
    literal: Literal = cast(Literal, evaluatedTerminal.get())
    assertEquals(test, literal.getLiteral())
    assertEquals(test, evaluatedTerminal.name)

    testToFail = "lj{l"
    hlp2 = hlp
    # make sure it fails
    # assertThrows(RuntimeException.class, () -> { evaluateHighlevelParser(hlp2, testToFail); }, "Parsing failed");
    try:
        evaluateHighlevelParser(hlp2, testToFail)
        raise Exception()  # throw if it did not fail
    except ParseException:
        pass


def testExpression():
    print("Test Expression")
    hlp = Parser()
    grammar = hlp.grammar
    grammar.compile(hlp.EXPRESSION.tgt)

    test = "Today, let's wait for {time:int} minutes."
    rhs = cast(List[Named], evaluateHighlevelParser(hlp, test))
    tgt = hlp.targetGrammar
    myType = tgt.sequence("mytype", rhs)

    # now parse and evaluate the generated grammar:
    tgt.compile(myType.tgt)
    rdParser = RDParser(tgt.getBNF(), Lexer("Today, let's wait for 5 minutes."), ebnfparsednodefactory.INSTANCE)
    pn = rdParser.parse()
    assertEquals(ParsingState.SUCCESSFUL, pn.matcher.state)
    print(graphviz.toVizDotLink(pn))


def testDefineType():
    print("Test define type")
    hlp = Parser()
    hlp.defineType("percentage", "{p:int} %", lambda pn: pn.evaluate("p"))

    def evaluate(pn: ParsedNode) -> object or None:
        percentage = cast(int, pn.evaluate("p"))
        assertEquals(5, percentage)
        print(percentage, " % left")
        return None
    hlp.defineSentence("Now it is only {p:percentage}.", evaluate)

    def evaluate(pn: ParsedNode) -> object or None:
        percentage = cast(int, pn.evaluate("p"))
        assertEquals(38, percentage)
        print(percentage, " % left.")
        return None
    hlp.defineSentence("There is still {p:percentage} left.", evaluate)

    pn = hlp.parse(
            "There is still 38 % left.\n" +
            "Now it is only 5 %.", None)
    assertEquals(pn.matcher.state, ParsingState.SUCCESSFUL)
    pn.evaluate()


if __name__ == "__main__":
    testQuantifier()
    testIdentifier()
    testList()
    testTuple()
    testCharacterClass()
    testType()
    testVariable()
    testNoVariable()
    testExpression()
    testDefineType()
