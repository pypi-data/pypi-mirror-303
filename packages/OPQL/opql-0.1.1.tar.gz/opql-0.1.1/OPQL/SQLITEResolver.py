import pandas

import OPQL.ocellog
import OPQL.query
import OPQL.querycontext
import OPQL.contextoperations

import OPQL.query_pattern
import OPQL.query_expression

import OPQL.util


def solve(ocel: OPQL.ocellog.OCELLog,
          query: OPQL.query.FullQuery):
    if not sanity_check(query):
        return None

    return resolve_query(ocel, query)


def sanity_check(query: OPQL.query.FullQuery):
    print("TODO implement sanity check")

    # TODO check that all target values of bins are of same datatype (and as such comparable)
    # check that lower bound a and upper bound b of bins satisfy a <= b

    return True


def resolve_query(ocel: OPQL.ocellog.OCELLog,
                  query: OPQL.query.FullQuery,
                  root_context=OPQL.querycontext.QueryContext(),
                  keep_context=False):
    # store root context name so it can be restored later
    root_ctx_cs = root_context.childrenSymbol

    candidate_endpoints = [root_context]

    running_graph_id = OPQL.util.RunningId("g", 0)

    for graphOrFilter in query.graphsAndFilters:
        # remember where we started
        if type(graphOrFilter) == OPQL.query.Graph:
            # TODO explicit copy necessary here?
            graph_startpoints = candidate_endpoints[:]
            candidate_endpoints = OPQL.contextoperations.do_graph(ocel,
                                                                  graph_startpoints,
                                                                  running_graph_id,
                                                                  graphOrFilter,
                                                                  candidate_endpoints)
        elif type(graphOrFilter) == OPQL.query.Filter:
            OPQL.contextoperations.do_filter(ocel, graphOrFilter, candidate_endpoints)
            root_context.clearChildren()
            candidate_endpoints = [root_context]
        elif type(graphOrFilter) == OPQL.query.Keep:
            keep_rule: OPQL.query.Keep = graphOrFilter
            projection = keep_rule.projection
            keep_startpoints = candidate_endpoints

            new_endpoints = []
            for endpoint in candidate_endpoints:
                resulting_endpoints = OPQL.contextoperations.do_keep(ocel, projection, endpoint)
                new_endpoints += resulting_endpoints

            if keep_rule.filter:
                new_endpoints = [endpoint for endpoint in new_endpoints
                                 if OPQL.query_expression.evaluate_graphexpression(ocel, endpoint, keep_rule.filter)]

            if keep_rule.projection.order:
                for order_item in reversed(keep_rule.projection.order):
                    decorated = [(OPQL.query_expression.evaluate_graphexpression(ocel, endpoint, order_item.expression),
                                  i,
                                  endpoint)
                                 for i, endpoint in enumerate(new_endpoints)]

                    reverse_order = True if order_item.direction == OPQL.query.OrderDirection.DESC else False

                    # handle None types
                    exclude_from_ordering = [item for item in decorated if item[0] is None]
                    decorated = [item for item in decorated if item[0] is not None]

                    decorated.sort(reverse=reverse_order)

                    rlist = exclude_from_ordering + decorated
                    decorated = rlist

                    new_endpoints = [endpoint for val, i, endpoint in decorated]

            if not keep_rule.projection.wildcard:
                if keep_startpoints:
                    new_root_children_name = keep_startpoints[0].childrenSymbol

                    new_root_children = []
                    for ksp in keep_startpoints:
                        new_root_children += ksp.children

                    root_context.childrenSymbol = new_root_children_name
                    root_context.children = new_root_children

                    for child_ctx in root_context.children:
                        child_ctx.parent = root_context

            if keep_rule.projection.distinct:
                distinct_results = set()

                to_prune = []
                to_keep = []

                for endpoint in new_endpoints:
                    val_tpl = endpoint.getValueTuple()

                    if val_tpl in distinct_results:
                        to_prune.append(endpoint)
                    else:
                        distinct_results.add(val_tpl)
                        to_keep.append(endpoint)

                new_endpoints = to_keep

                # TODO actually prune

            if (keep_rule.projection.limit
                    and len(new_endpoints) > keep_rule.projection.limit):
                new_endpoints = new_endpoints[0:keep_rule.projection.limit]

                to_prune = new_endpoints[keep_rule.projection.limit:]
                print("TODO: prune context after limit clause!")

            candidate_endpoints = new_endpoints

    returnrows = []

    # result tree similar to contexttree
    # go from rootcontext
    # keep current context depth -what for again?
    # evaluate thing(list of evaluateables, current depth)
    # and add these as children to previous result

    # evaluate thing:
    # get current depth (or max depth?)
    # if thing is down the line: fan out tree, start with
    # if thing to look up is upwards: just look it up

    if query.return_rule.ocel:
        return ocel.dbconnection

    # TODO: this should actually be: evaluate a keep with wildcard (and with or without distinct) and return the last N context bindings (i.e. exactly those mentioned in the return statement)
    # TODO this would also introduce SUBJECTTO rules for RETURN statements
    for endpoint in candidate_endpoints:
        returnvalues: list = []
        for returnstatement in query.return_rule.projection.ctx_expansions:
            rval = OPQL.query_expression.evaluate_graphexpression(ocel, endpoint, returnstatement.evaluatable)
            returnvalues.append(rval)

        returnrows.append(returnvalues)

    cols = [str(returnstatement.tag) if returnstatement.tag is not None else str(returnstatement.evaluatable)
            for returnstatement in query.return_rule.projection.ctx_expansions]

    df = pandas.DataFrame(returnrows, columns=cols)

    if not keep_context:
        root_context.clearChildren()
        # needed because doing graph matching will rename this to whatever symbol was matched
        root_context.childrenSymbol = root_ctx_cs

    return df
