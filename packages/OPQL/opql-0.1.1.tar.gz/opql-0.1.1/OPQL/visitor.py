from OPQL.grammar.OPQLParser import *
from OPQL.grammar.OPQLVisitor import OPQLVisitor
import OPQL.query

import datetime
import OPQL.util


class Visitor(OPQLVisitor):
    def __init__(self):
        self.running_event_id = OPQL.util.RunningId("__ev", 0)
        self.running_object_id = OPQL.util.RunningId("__ob", 0)
        self.running_relation_id = OPQL.util.RunningId("__rel", 0)
        self.running_graph_id = OPQL.util.RunningId("__gr", 0)

    # Visit a parse tree produced by OPQLParser#r_EO_PROPERTY.
    def visitR_EO_PROPERTY(self, ctx:OPQLParser.R_EO_PROPERTYContext):
        valref = OPQL.query.ValueReference()
        valref.name = ctx.SYMBOLICNAME()[0].getText()
        valref.property = ctx.SYMBOLICNAME()[1].getText()

        if ctx.r_PROPERTYTIMESTAMP():
            valref.timestamp = self.visitR_PROPERTYTIMESTAMP(ctx.r_PROPERTYTIMESTAMP())

        return valref

    # Visit a parse tree produced by OPQLParser#r_TIMESTAMP.
    def visitR_TIMESTAMP(self, ctx:OPQLParser.R_TIMESTAMPContext):
        time_stamp = ctx.STRING().getText()[1:-1]
        rv = datetime.datetime.strptime(time_stamp, "%Y-%m-%dT%H:%M:%S.%f%z")
        return rv

    # Visit a parse tree produced by OPQLParser#r_PROPERTYTIMESTAMP.
    def visitR_PROPERTYTIMESTAMP(self, ctx:OPQLParser.R_PROPERTYTIMESTAMPContext):
        # reference to some event
        if ctx.SYMBOLICNAME():
            return ctx.SYMBOLICNAME().getText()

        # if not a symbolic name, try to parse datetime from string
        if ctx.r_TIMESTAMP():
            # ignore leading and trailing quotation marks
            # TODO: try for some more timestamp formattings to make usage more lenient
            timestamp_str = ctx.r_TIMESTAMP().getText()[1:-1]
            timestamp = datetime.datetime.strptime(timestamp_str, "%Y-%m-%dT%H:%M:%S.%f%z")
            return timestamp

        print("ERROR: failed to correctly parse PROPERTYTIMESTAMP")
        return self.visitChildren(ctx)

    # Visit a parse tree produced by OPQLParser#r_RV_FUNCTION_ARG.
    def visitR_RV_FUNCTION_ARG(self, ctx:OPQLParser.R_RV_FUNCTION_ARGContext):
        f_arg = OPQL.query.FunctionArgument()
        if ctx.r_EXPRESSION():
            f_arg.arg = self.visitR_EXPRESSION(ctx.r_EXPRESSION())
        elif ctx.r_FULLQUERY():
            f_arg.arg = self.visitR_FULLQUERY(ctx.r_FULLQUERY())

        return f_arg

    # Visit a parse tree produced by OPQLParser#r_RV_FUNCTION.
    def visitR_RV_FUNCTION_CALL(self, ctx:OPQLParser.R_RV_FUNCTION_CALLContext):
        queryfunction = OPQL.query.Function()
        queryfunction.name = ctx.SYMBOLICNAME().getText()
        queryfunction.arguments = [self.visitR_RV_FUNCTION_ARG(f_arg) for f_arg in ctx.r_RV_FUNCTION_ARG()]

        return queryfunction

    def visitR_PATTERN_RULE(self, ctx:OPQLParser.R_PATTERN_RULEContext):
        graph = OPQL.query.Graph()
        graph.patterns = self.visitR_GRAPHPATTERNLIST(ctx.r_GRAPHPATTERNLIST())

        # if ctx.SYMBOLICNAME():
        #     graph.tag = ctx.SYMBOLICNAME().getText()

        if ctx.r_PROPOSITIONAL_RULE():
            graph.filter = self.visitR_PROPOSITIONAL_RULE(ctx.r_PROPOSITIONAL_RULE())

        return graph

    # Visit a parse tree produced by OPQLParser#r_VALUE_TYPE.
    def visitR_VALUE_TYPE(self, ctx:OPQLParser.R_VALUE_TYPEContext):
        if ctx.r_EO_PROPERTY():
            return self.visitR_EO_PROPERTY(ctx.r_EO_PROPERTY())

        if ctx.r_TIMESTAMP():
            return self.visitR_TIMESTAMP(ctx.r_TIMESTAMP())

        if ctx.STRING():
            return ctx.STRING().getText()[1:-1]

        if ctx.SYMBOLICNAME():
            val_ref = OPQL.query.ValueReference()
            val_ref.name = ctx.SYMBOLICNAME().getText()
            return val_ref

        if ctx.r_INT():
            return int(self.visitR_INT(ctx.r_INT()))

        if ctx.CONSTANTNUM():
            # TODO check for comma and cast to int or float respectively
            print("Warning: constantnum ignorantly cast to float")
            return float(ctx.CONSTANTNUM().getText())

        if ctx.r_RV_FUNCTION_CALL():
            return self.visitR_RV_FUNCTION_CALL(ctx.r_RV_FUNCTION_CALL())

        print(f"OPQLV: Error parsing {ctx.getText()}")
        return None

    # Visit a parse tree produced by OPQLParser#r_EXPRESSION.
    def visitR_EXPRESSION(self, ctx: OPQLParser.R_EXPRESSIONContext):
        expression = OPQL.query.GraphExpression()
        expression.XORs = [self.visitR_XOR(xor) for xor in ctx.r_XOR()]
        return expression

        # Visit a parse tree produced by OPQLParser#r_XOR.

    def visitR_XOR(self, ctx: OPQLParser.R_XORContext):
        g_ex_xor = OPQL.query.GraphExXOR()
        g_ex_xor.ANDs = [self.visitR_AND(r_and) for r_and in ctx.r_AND()]
        return g_ex_xor

        # Visit a parse tree produced by OPQLParser#r_AND.

    def visitR_AND(self, ctx: OPQLParser.R_ANDContext):
        g_ex_and = OPQL.query.GraphExAND()
        g_ex_and.NOTs = [self.visitR_NOT(r_not) for r_not in ctx.r_NOT()]
        return g_ex_and

        # Visit a parse tree produced by OPQLParser#r_NOT.

    def visitR_NOT(self, ctx: OPQLParser.R_NOTContext):
        g_not = OPQL.query.GraphExNOT()
        g_not.invert = True if ctx.NOT() else False
        g_not.comparison = self.visitR_COMPARISON(ctx.r_COMPARISON())
        return g_not

        # Visit a parse tree produced by OPQLParser#r_COMPARISON.

    def visitR_COMPARISON(self, ctx: OPQLParser.R_COMPARISONContext):
        g_comp = OPQL.query.Comparison()
        signs = [self.visitR_COMPARE_SIGN(cs) for cs in ctx.r_COMPARE_SIGN()]
        addsubs = [self.visitR_ADDSUB(addsub) for addsub in ctx.r_ADDSUB()]

        g_comp.addsub = addsubs[0]
        if len(addsubs) > 1:
            # remove first element since it is already stored as g_comp.addsub
            addsubs.pop(0)
            g_comp.further_addsubs = list(zip(signs, addsubs))

        return g_comp

        # Visit a parse tree produced by OPQLParser#r_COMPARE_SIGN.

    def visitR_COMPARE_SIGN(self, ctx: OPQLParser.R_COMPARE_SIGNContext):
        if ctx.EQUAL_TO():
            return OPQL.query.ComparisonSign.EQUAL_TO

        if ctx.LE():
            return OPQL.query.ComparisonSign.LE

        if ctx.GE():
            return OPQL.query.ComparisonSign.GE

        if ctx.GT():
            return OPQL.query.ComparisonSign.GT

        if ctx.LT():
            return OPQL.query.ComparisonSign.LT

        if ctx.NOT_EQUAL():
            return OPQL.query.ComparisonSign.NOT_EQUAL

        print(f"Failed to parse compare sign {ctx.getText()}")
        return None

        # Visit a parse tree produced by OPQLParser#r_PLUSSUBSIGN.
    def visitR_PLUSSUBSIGN(self, ctx: OPQLParser.R_PLUSSUBSIGNContext):
        if ctx.PLUS():
            return OPQL.query.SignAddSub.ADD

        if ctx.SUB():
            return OPQL.query.SignAddSub.SUB

        print(f"Error parsing {ctx.getText()}")
        return None

        # Visit a parse tree produced by OPQLParser#r_ADDSUB.

    def visitR_ADDSUB(self, ctx: OPQLParser.R_ADDSUBContext):
        g_as = OPQL.query.AddSub()

        signs = [self.visitR_PLUSSUBSIGN(ass) for ass in ctx.r_PLUSSUBSIGN()]
        muldivs = [self.visitR_MULDIV(md) for md in ctx.r_MULDIV()]

        g_as.muldiv = muldivs[0]
        if len(muldivs) > 1:
            # remove first element since it is already stored as g_comp.addsub
            muldivs.pop(0)
            g_as.further_muldivs = list(zip(signs, muldivs))

        return g_as

        # Visit a parse tree produced by OPQLParser#r_MULDIVMODSIGN.
    def visitR_MULDIVMODSIGN(self, ctx: OPQLParser.R_MULDIVMODSIGNContext):
        if ctx.MULT():
            return OPQL.query.SignMulDivMod.MUL

        if ctx.DIV():
            return OPQL.query.SignMulDivMod.DIV

        if ctx.MOD():
            return OPQL.query.SignMulDivMod.MOD

        print(f"Error failed to parse {ctx.getText()}")

        # Visit a parse tree produced by OPQLParser#r_MULDIV.

    def visitR_MULDIV(self, ctx: OPQLParser.R_MULDIVContext):
        g_md = OPQL.query.MulDiv()

        signs = [self.visitR_MULDIVMODSIGN(mdm_s) for mdm_s in ctx.r_MULDIVMODSIGN()]
        powers = [self.visitR_POWER(pwr) for pwr in ctx.r_POWER()]

        g_md.power = powers[0]
        if len(powers) > 1:
            # remove first element since it is already stored as g_comp.addsub
            powers.pop(0)
            g_md.further_powers = list(zip(signs, powers))

        return g_md

        # Visit a parse tree produced by OPQLParser#r_POWER.

    def visitR_POWER(self, ctx: OPQLParser.R_POWERContext):
        g_p = OPQL.query.Power()
        g_p.unary_addsubs = [self.visitR_UNARY_ADDSUB(uas) for uas in ctx.r_UNARY_ADDSUB()]

        return g_p

        # Visit a parse tree produced by OPQLParser#r_UNARY_ADDSUB.

    def visitR_UNARY_ADDSUB(self, ctx: OPQLParser.R_UNARY_ADDSUBContext):
        g_uas = OPQL.query.UnaryAddSub()
        g_uas.sign = None

        if ctx.PLUS():
            g_uas.sign = OPQL.query.SignAddSub.ADD

        if ctx.SUB():
            g_uas.sign = OPQL.query.SignAddSub.SUB

        g_uas.atomic = self.visitR_ATOMIC(ctx.r_ATOMIC())

        return g_uas

        # Visit a parse tree produced by OPQLParser#r_ATOMIC.

    def visitR_ATOMIC(self, ctx: OPQLParser.R_ATOMICContext):
        # atomic currently only has valuetype
        atomic = OPQL.query.Atomic()
        atomic.value = self.visitR_VALUE_TYPE(ctx.r_VALUE_TYPE())
        return atomic

    def visitR_PROPOSITIONAL_RULE(self, ctx:OPQLParser.R_PROPOSITIONAL_RULEContext):
        if ctx.r_EXPRESSION():
            return self.visitR_EXPRESSION(ctx.r_EXPRESSION())

        return None

    def visitR_RETURN_RULE(self, ctx:OPQLParser.R_RETURN_RULEContext):
        ret_rule = OPQL.query.Return()

        if ctx.OCEL_TKN():
            ret_rule.ocel = True
            return ret_rule

        ret_rule.projection = self.visitR_PROJECTION(ctx.r_PROJECTION())

        if ctx.r_PROPOSITIONAL_RULE():
            ret_rule.filter = self.visitR_PROJECTION(ctx.r_PROPOSITIONAL_RULE())

        return ret_rule

    # Visit a parse tree produced by OPQLParser#r_FILTER_RULE.
    def visitR_FILTER_RULE(self, ctx:OPQLParser.R_FILTER_RULEContext):
        filter_s = OPQL.query.Filter()
        filter_s.entities_to_remove = [symname_ctx.getText() for symname_ctx in ctx.SYMBOLICNAME()]
        return filter_s

    # Visit a parse tree produced by OPQLParser#r_SNAME.
    def visitR_SNAME(self, ctx:OPQLParser.R_SNAMEContext):
        tag = None
        if ctx.SYMBOLICNAME():
            tag = ctx.SYMBOLICNAME().getText()
        evaluatable = self.visitR_EXPRESSION(ctx.r_EXPRESSION())

        return tag, evaluatable

    # Visit a parse tree produced by OPQLParser#r_ORDER_ITEM.
    def visitR_ORDER_ITEM(self, ctx:OPQLParser.R_ORDER_ITEMContext):
        oi = OPQL.query.OrderItem()
        oi.expression = self.visitR_EXPRESSION(ctx.r_EXPRESSION())
        oi.direction = None
        if ctx.ASC_TKN():
            oi.direction = OPQL.query.OrderDirection.ASC
        if ctx.DESC_TKN():
            oi.direction = OPQL.query.OrderDirection.DESC

        return oi

    # Visit a parse tree produced by OPQLParser#r_ORDER.
    def visitR_ORDER(self, ctx:OPQLParser.R_ORDERContext):
        return [self.visitR_ORDER_ITEM(oi_ctx) for oi_ctx in ctx.r_ORDER_ITEM()]

    # Visit a parse tree produced by OPQLParser#r_INT.
    def visitR_INT(self, ctx:OPQLParser.R_INTContext):
        return int(float(ctx.getText()))

    # Visit a parse tree produced by OPQLParser#r_LIMIT.
    def visitR_LIMIT(self, ctx:OPQLParser.R_LIMITContext):
        return self.visitR_INT(ctx.r_INT())

    # Visit a parse tree produced by OPQLParser#r_INTERVAL_LIMIT.
    def visitR_INTERVAL_LIMIT(self, ctx:OPQLParser.R_INTERVAL_LIMITContext):
        if ctx.NEG_INF_TKN():
            return OPQL.query.BinningInfinity.NEGATIVE_INFINITY

        if ctx.POS_INF_TKN():
            return OPQL.query.BinningInfinity.POSITIVE_INFINITY

        if ctx.r_INT():
            return self.visitR_INT(ctx.r_INT())

        if ctx.CONSTANTNUM():
            return float(ctx.getText())

        print(f"Error parsing interval limit: {ctx.getText()}")
        return None

    # Visit a parse tree produced by OPQLParser#r_INTERVAL_TARGET.
    def visitR_INTERVAL_TARGET(self, ctx:OPQLParser.R_INTERVAL_TARGETContext):
        if ctx.r_INT():
            return self.visitR_INT(ctx.r_INT())
        if ctx.STRING():
            return ctx.getText()[1:-1]
        if ctx.CONSTANTNUM():
            return float(ctx.getText())

        print(f"Error parsing interval target: {ctx.getText()}")
        return None

    # Visit a parse tree produced by OPQLParser#r_BIN_INTERVAL.
    def visitR_BIN_INTERVAL(self, ctx:OPQLParser.R_BIN_INTERVALContext):
        bin_int = OPQL.query.BinningInterval()
        bin_int.include_begin = True if ctx.LEFT_SBR() else False
        bin_int.include_end = True if ctx.RIGHT_SBR() else False
        bin_int.begin = self.visitR_INTERVAL_LIMIT(ctx.r_INTERVAL_LIMIT(0))
        bin_int.end = self.visitR_INTERVAL_LIMIT(ctx.r_INTERVAL_LIMIT(1))
        bin_int.target = self.visitR_INTERVAL_TARGET(ctx.r_INTERVAL_TARGET())
        return bin_int

    # Visit a parse tree produced by OPQLParser#r_BINNING.
    def visitR_BINNING(self, ctx:OPQLParser.R_BINNINGContext):
        return [self.visitR_BIN_INTERVAL(bin_interval) for bin_interval in ctx.r_BIN_INTERVAL()]

    # Visit a parse tree produced by OPQLParser#r_PROJECTION_ITEM.
    def visitR_PROJECTION_ITEM(self, ctx:OPQLParser.R_PROJECTION_ITEMContext):
        pi = OPQL.query.ProjectionItem()

        pi.tag, pi.evaluatable = self.visitR_SNAME(ctx.r_SNAME())

        if ctx.r_BINNING():
            pi.binning = self.visitR_BINNING(ctx.r_BINNING())

        return pi

    # Visit a parse tree produced by OPQLParser#r_PROJECTION.
    def visitR_PROJECTION(self, ctx:OPQLParser.R_PROJECTIONContext):
        projection = OPQL.query.Projection()
        projection.wildcard = True if ctx.ASTERISK() else False
        projection.distinct = True if ctx.DISTINCT_TKN() else False
        projection.ctx_expansions = [self.visitR_PROJECTION_ITEM(pi_ctx) for pi_ctx in ctx.r_PROJECTION_ITEM()]

        if ctx.r_ORDER():
            projection.order = self.visitR_ORDER(ctx.r_ORDER())

        if ctx.r_LIMIT():
            projection.limit = self.visitR_LIMIT(ctx.r_LIMIT())

        return projection

    # Visit a parse tree produced by OPQLParser#r_KEEP_RULE.
    def visitR_KEEP_RULE(self, ctx:OPQLParser.R_KEEP_RULEContext):
        keep_r = OPQL.query.Keep()
        keep_r.projection = self.visitR_PROJECTION(ctx.r_PROJECTION())

        if ctx.r_PROPOSITIONAL_RULE():
            keep_r.filter = self.visitR_PROPOSITIONAL_RULE(ctx.r_PROPOSITIONAL_RULE())

        return keep_r

    # Visit a parse tree produced by OPQLParser#r_CONTEXT_RULE.
    def visitR_CONTEXT_RULE(self, ctx:OPQLParser.R_CONTEXT_RULEContext):
        if ctx.r_PATTERN_RULE():
            return self.visitR_PATTERN_RULE(ctx.r_PATTERN_RULE())
        elif ctx.r_FILTER_RULE():
            return self.visitR_FILTER_RULE(ctx.r_FILTER_RULE())
        elif ctx.r_KEEP_RULE():
            return self.visitR_KEEP_RULE(ctx.r_KEEP_RULE())
        else:
            print("ERROR: encountered unknown rule in visitor r_CONTEXT_RULE")

    def visitR_ENTRY_POINT(self, ctx:OPQLParser.R_ENTRY_POINTContext):
        return self.visitR_FULLQUERY(ctx.r_FULLQUERY())

    # Visit a parse tree produced by OPQLParser#r_FULLQUERY.
    def visitR_FULLQUERY(self, ctx: OPQLParser.R_FULLQUERYContext):
        fullquery: OPQL.query.FullQuery = OPQL.query.FullQuery()

        fullquery.graphsAndFilters = [self.visitR_CONTEXT_RULE(ctx_r) for ctx_r in ctx.r_CONTEXT_RULE()]
        fullquery.return_rule = self.visitR_RETURN_RULE(ctx.r_RETURN_RULE())
        return fullquery

    # Visit a parse tree produced by OPQLParser#r_GRAPH.
    def visitR_GRAPH(self, ctx: OPQLParser.R_GRAPHContext):
        resultlist = []

        if ctx.r_EVENT():
            resultlist.append(self.visitR_EVENT(ctx.r_EVENT()))

        if ctx.r_OBJECT():
            resultlist.append(self.visitR_OBJECT(ctx.r_OBJECT()))

        if ctx.r_RELATION_ANY():
            resultlist.append(self.visitR_RELATION_ANY(ctx.r_RELATION_ANY()))
        elif ctx.r_RELATION_LD():
            resultlist.append(self.visitR_RELATION_LD(ctx.r_RELATION_LD()))
        elif ctx.r_RELATION_RD():
            resultlist.append(self.visitR_RELATION_RD(ctx.r_RELATION_RD()))

        graphctx = ctx.r_GRAPH()
        if graphctx:
            subgraphlist = self.visitR_GRAPH(graphctx)
            for graphentity in subgraphlist:
                resultlist.append(graphentity)

        if ctx.r_GRAPH_WITHOUT_EVENT():
            subgraphlist = self.visitR_GRAPH_WITHOUT_EVENT(ctx.r_GRAPH_WITHOUT_EVENT())
            for graphentity in subgraphlist:
                resultlist.append(graphentity)

        return resultlist

    # Visit a parse tree produced by OPQLParser#r_GRAPH_WITHOUT_EVENT.
    def visitR_GRAPH_WITHOUT_EVENT(self, ctx: OPQLParser.R_GRAPH_WITHOUT_EVENTContext):
        resultlist = [self.visitR_OBJECT(ctx.r_OBJECT())]

        if ctx.r_RELATION_ANY():
            resultlist.append(self.visitR_RELATION_ANY(ctx.r_RELATION_ANY()))
        elif ctx.r_RELATION_LD():
            resultlist.append(self.visitR_RELATION_LD(ctx.r_RELATION_LD()))

        if ctx.r_GRAPH():
            sublist = self.visitR_GRAPH(ctx.r_GRAPH())
            for graphEntity in sublist:
                resultlist.append(graphEntity)

        return resultlist

    # Visit a parse tree produced by OPQLParser#r_GRAPHPATTERNLIST.
    def visitR_GRAPHPATTERNLIST(self, ctx: OPQLParser.R_GRAPHPATTERNLISTContext):
        resultlist = []
        g = ctx.r_GRAPH()
        for graph in g:
            result_graph = self.visitR_GRAPH(graph)
            #TODO: is checking for None correct here?
            if result_graph is not None:
                resultlist.append(result_graph)

        return resultlist

    # Visit a parse tree produced by OPQLParser#r_EVENT.
    def visitR_EVENT(self, ctx: OPQLParser.R_EVENTContext):
        event = OPQL.query.GraphEvent()

        if ctx.r_TAG():
            event.tag = self.visitR_TAG(ctx.r_TAG())
        else:
            event.tag = self.running_event_id.get_next_id()

        if ctx.r_NAME():
            event.type = self.visitR_NAME(ctx.r_NAME())

        return event

    # Visit a parse tree produced by OPQLParser#r_OBJECT.
    def visitR_OBJECT(self, ctx: OPQLParser.R_OBJECTContext):
        object = OPQL.query.GraphObject()

        if ctx.r_TAG():
            object.tag = self.visitR_TAG(ctx.r_TAG())
        else:
            object.get = self.running_object_id.get_next_id()

        if ctx.r_NAME():
            object.type = self.visitR_NAME(ctx.r_NAME())

        # return self.visitChildren(ctx)
        return object

    # Visit a parse tree produced by OPQLParser#r_RELATION.
    def visitR_RELATION_ANY(self, ctx: OPQLParser.R_RELATION_ANYContext):
        relation = OPQL.query.GraphRelation()

        relation.tag = self.visitR_TAG(ctx.r_TAG()) if ctx.r_TAG() else self.running_relation_id.get_next_id()

        if ctx.r_NAME():
            relation.type = self.visitR_NAME(ctx.r_NAME())

        relation.direction = OPQL.query.GraphRelationDirection.ANY
        return relation

    def visitR_RELATION_LD(self, ctx: OPQLParser.R_RELATION_LDContext):
        relation = OPQL.query.GraphRelation()

        relation.tag = self.visitR_TAG(ctx.r_TAG()) if ctx.r_TAG() else self.running_relation_id.get_next_id()

        if ctx.r_NAME():
            relation.type = self.visitR_NAME(ctx.r_NAME())

        relation.direction = OPQL.query.GraphRelationDirection.LEFT
        return relation

    def visitR_RELATION_RD(self, ctx:OPQLParser.R_RELATION_RDContext):
        relation = OPQL.query.GraphRelation()

        relation.tag = self.visitR_TAG(ctx.r_TAG()) if ctx.r_TAG() else self.running_relation_id.get_next_id()

        if ctx.r_NAME():
            relation.type = self.visitR_NAME(ctx.r_NAME())

        relation.direction = OPQL.query.GraphRelationDirection.RIGHT
        return relation

    # Visit a parse tree produced by OPQLParser#r_NAME.
    def visitR_NAME(self, ctx: OPQLParser.R_NAMEContext):
        # removes leading and trailing quotes "
        return ctx.getText()[1:-1]

    # Visit a parse tree produced by OPQLParser#r_TAG.
    def visitR_TAG(self, ctx: OPQLParser.R_TAGContext):
        return ctx.getText()


