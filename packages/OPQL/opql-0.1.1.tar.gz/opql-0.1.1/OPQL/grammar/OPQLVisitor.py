# Generated from OPQL.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .OPQLParser import OPQLParser
else:
    from OPQLParser import OPQLParser

# This class defines a complete generic visitor for a parse tree produced by OPQLParser.

class OPQLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by OPQLParser#r_TIMESTAMP.
    def visitR_TIMESTAMP(self, ctx:OPQLParser.R_TIMESTAMPContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OPQLParser#r_PROPERTYTIMESTAMP.
    def visitR_PROPERTYTIMESTAMP(self, ctx:OPQLParser.R_PROPERTYTIMESTAMPContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OPQLParser#r_EO_PROPERTY.
    def visitR_EO_PROPERTY(self, ctx:OPQLParser.R_EO_PROPERTYContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OPQLParser#r_RV_FUNCTION_ARG.
    def visitR_RV_FUNCTION_ARG(self, ctx:OPQLParser.R_RV_FUNCTION_ARGContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OPQLParser#r_RV_FUNCTION_CALL.
    def visitR_RV_FUNCTION_CALL(self, ctx:OPQLParser.R_RV_FUNCTION_CALLContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OPQLParser#r_PROPOSITIONAL_RULE.
    def visitR_PROPOSITIONAL_RULE(self, ctx:OPQLParser.R_PROPOSITIONAL_RULEContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OPQLParser#r_ORDER_ITEM.
    def visitR_ORDER_ITEM(self, ctx:OPQLParser.R_ORDER_ITEMContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OPQLParser#r_ORDER.
    def visitR_ORDER(self, ctx:OPQLParser.R_ORDERContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OPQLParser#r_INT.
    def visitR_INT(self, ctx:OPQLParser.R_INTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OPQLParser#r_LIMIT.
    def visitR_LIMIT(self, ctx:OPQLParser.R_LIMITContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OPQLParser#r_INTERVAL_LIMIT.
    def visitR_INTERVAL_LIMIT(self, ctx:OPQLParser.R_INTERVAL_LIMITContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OPQLParser#r_INTERVAL_TARGET.
    def visitR_INTERVAL_TARGET(self, ctx:OPQLParser.R_INTERVAL_TARGETContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OPQLParser#r_BIN_INTERVAL.
    def visitR_BIN_INTERVAL(self, ctx:OPQLParser.R_BIN_INTERVALContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OPQLParser#r_BINNING.
    def visitR_BINNING(self, ctx:OPQLParser.R_BINNINGContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OPQLParser#r_SNAME.
    def visitR_SNAME(self, ctx:OPQLParser.R_SNAMEContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OPQLParser#r_PROJECTION_ITEM.
    def visitR_PROJECTION_ITEM(self, ctx:OPQLParser.R_PROJECTION_ITEMContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OPQLParser#r_PROJECTION.
    def visitR_PROJECTION(self, ctx:OPQLParser.R_PROJECTIONContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OPQLParser#r_KEEP_RULE.
    def visitR_KEEP_RULE(self, ctx:OPQLParser.R_KEEP_RULEContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OPQLParser#r_RETURN_RULE.
    def visitR_RETURN_RULE(self, ctx:OPQLParser.R_RETURN_RULEContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OPQLParser#r_FILTER_RULE.
    def visitR_FILTER_RULE(self, ctx:OPQLParser.R_FILTER_RULEContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OPQLParser#r_ENTRY_POINT.
    def visitR_ENTRY_POINT(self, ctx:OPQLParser.R_ENTRY_POINTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OPQLParser#r_FULLQUERY.
    def visitR_FULLQUERY(self, ctx:OPQLParser.R_FULLQUERYContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OPQLParser#r_CONTEXT_RULE.
    def visitR_CONTEXT_RULE(self, ctx:OPQLParser.R_CONTEXT_RULEContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OPQLParser#r_PATTERN_RULE.
    def visitR_PATTERN_RULE(self, ctx:OPQLParser.R_PATTERN_RULEContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OPQLParser#r_GRAPHPATTERNLIST.
    def visitR_GRAPHPATTERNLIST(self, ctx:OPQLParser.R_GRAPHPATTERNLISTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OPQLParser#r_GRAPH.
    def visitR_GRAPH(self, ctx:OPQLParser.R_GRAPHContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OPQLParser#r_GRAPH_WITHOUT_EVENT.
    def visitR_GRAPH_WITHOUT_EVENT(self, ctx:OPQLParser.R_GRAPH_WITHOUT_EVENTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OPQLParser#r_EVENT.
    def visitR_EVENT(self, ctx:OPQLParser.R_EVENTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OPQLParser#r_OBJECT.
    def visitR_OBJECT(self, ctx:OPQLParser.R_OBJECTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OPQLParser#r_RELATION_ANY.
    def visitR_RELATION_ANY(self, ctx:OPQLParser.R_RELATION_ANYContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OPQLParser#r_RELATION_RD.
    def visitR_RELATION_RD(self, ctx:OPQLParser.R_RELATION_RDContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OPQLParser#r_RELATION_LD.
    def visitR_RELATION_LD(self, ctx:OPQLParser.R_RELATION_LDContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OPQLParser#r_TAG.
    def visitR_TAG(self, ctx:OPQLParser.R_TAGContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OPQLParser#r_NAME.
    def visitR_NAME(self, ctx:OPQLParser.R_NAMEContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OPQLParser#r_VALUE_TYPE.
    def visitR_VALUE_TYPE(self, ctx:OPQLParser.R_VALUE_TYPEContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OPQLParser#r_EXPRESSION.
    def visitR_EXPRESSION(self, ctx:OPQLParser.R_EXPRESSIONContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OPQLParser#r_XOR.
    def visitR_XOR(self, ctx:OPQLParser.R_XORContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OPQLParser#r_AND.
    def visitR_AND(self, ctx:OPQLParser.R_ANDContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OPQLParser#r_NOT.
    def visitR_NOT(self, ctx:OPQLParser.R_NOTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OPQLParser#r_COMPARISON.
    def visitR_COMPARISON(self, ctx:OPQLParser.R_COMPARISONContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OPQLParser#r_COMPARE_SIGN.
    def visitR_COMPARE_SIGN(self, ctx:OPQLParser.R_COMPARE_SIGNContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OPQLParser#r_PLUSSUBSIGN.
    def visitR_PLUSSUBSIGN(self, ctx:OPQLParser.R_PLUSSUBSIGNContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OPQLParser#r_ADDSUB.
    def visitR_ADDSUB(self, ctx:OPQLParser.R_ADDSUBContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OPQLParser#r_MULDIVMODSIGN.
    def visitR_MULDIVMODSIGN(self, ctx:OPQLParser.R_MULDIVMODSIGNContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OPQLParser#r_MULDIV.
    def visitR_MULDIV(self, ctx:OPQLParser.R_MULDIVContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OPQLParser#r_POWER.
    def visitR_POWER(self, ctx:OPQLParser.R_POWERContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OPQLParser#r_UNARY_ADDSUB.
    def visitR_UNARY_ADDSUB(self, ctx:OPQLParser.R_UNARY_ADDSUBContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OPQLParser#r_ATOMIC.
    def visitR_ATOMIC(self, ctx:OPQLParser.R_ATOMICContext):
        return self.visitChildren(ctx)



del OPQLParser