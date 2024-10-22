from __future__ import annotations

from typing import TYPE_CHECKING

import urllib.parse

from nlScript.core.named import Named
from nlScript.core.parsingstate import ParsingState

if TYPE_CHECKING:
    from nlScript.core.defaultparsednode import DefaultParsedNode


def toVizDotLink(root: DefaultParsedNode) -> str:
    return "https://edotor.net/?s=%22bla%22?engine=dot#" + urllib.parse.quote(toVizDot(root)). \
        replace("+", "%20"). \
        replace("*", "%2A")


def toVizDot(root: DefaultParsedNode) -> str:
    return \
            'digraph parsed_tree {\n' + \
            '  # rankdir=LR;\n' + \
            '  size="8,5"\n' + \
            '  node [shape=circle];\n\n' + \
            vizDotNodes(root) + \
            '\n' + \
            vizDotLinks(root) + \
            '}\n'


def vizDotNodes(root: DefaultParsedNode) -> str:
    color = 'black'
    matcher = root.matcher
    if matcher is not None:
        if matcher.state == ParsingState.SUCCESSFUL:
            color = 'green'
        elif matcher.state == ParsingState.END_OF_INPUT:
            color = 'orange'
        elif matcher.state == ParsingState.FAILED:
            color = 'red3'

    parsed = root.getParsedString()
    parsed = parsed.replace("\n", "\\n")
    name = root.name
    if name == Named.UNNAMED:
        name = root.symbol.symbol
    name = name.replace("\n", "\\n")
    sb = '  ' + \
        str(hash(root)) + \
        '[label="' + name + '" color=' + color + \
        ', tooltip="' + parsed + '(' + str(matcher.pos) + ')"' + \
        ']\n'
    for pn in root.children:
        sb += vizDotNodes(pn)
    return sb


def vizDotLinks(root: DefaultParsedNode) -> str:
    sb = ""
    h = hash(root)
    for child in root.children:
        sb += "  " + str(h) + " -> " + str(hash(child)) + ";\n"
        sb += vizDotLinks(child)
    return sb
