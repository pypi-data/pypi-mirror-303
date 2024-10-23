import antlr4

import OPQL.grammar.OPQLLexer
import OPQL.grammar.OPQLParser

import OPQL.query
import OPQL.visitor


def scan_query(query_string: str) -> OPQL.query.FullQuery:
    lex = OPQL.grammar.OPQLLexer.OPQLLexer(antlr4.InputStream(query_string))
    token_stream = antlr4.CommonTokenStream(lex)
    token_stream.fill()

    parser = OPQL.grammar.OPQLParser.OPQLParser(token_stream)

    fullqueryctx = parser.r_ENTRY_POINT()

    stringtree = fullqueryctx.toStringTree(recog=parser)
    print('tree:')
    print(stringtree)

    visitor = OPQL.visitor.Visitor()
    query_ir = visitor.visitR_ENTRY_POINT(fullqueryctx)
    return query_ir

def scan_tree(query_string: str):
    lex = OPQL.grammar.OPQLLexer.OPQLLexer(antlr4.InputStream(query_string))
    token_stream = antlr4.CommonTokenStream(lex)
    token_stream.fill()

    parser = OPQL.grammar.OPQLParser.OPQLParser(token_stream)

    return parser.r_ENTRY_POINT()

