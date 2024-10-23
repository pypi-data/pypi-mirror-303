import OPQL.query
import OPQL.query_pattern
import OPQL.query_expression
import OPQL.querycontext
import OPQL.ocellog


def prune(context, depth):
    if depth <= 0:
        return

    deadends = []
    for ctx in context.children:
        # first prune children
        if depth > 1:
            prune(ctx, depth - 1)

            # if no children left
            if not ctx.children:
                deadends.append(ctx)

    for deadend in deadends:
        deadend.parent = None
        context.children.remove(deadend)


def do_graph(ocel: OPQL.ocellog.OCELLog,
             graph_startpoints,
             running_graph_id,
             graph: OPQL.query.Graph,
             candidate_endpoints):
    graph_tag = graph.tag
    context_length = 0
    new_endpoints = candidate_endpoints[:]
    for pattern in graph.patterns:
        context_length += len(pattern)
        # print("Solving for pattern: " + '-'.join([str(elem) for elem in pattern]))
        endpoints = []
        for context in new_endpoints:
            endpoints += OPQL.query_pattern.find_pattern_candidates(ocel, context, pattern)

        # print(f"Generated {len(endpoints)}")
        # set new candidate endpoints for newly generated contexts
        new_endpoints = endpoints

    # print(f"candidates before applying filter: {len(new_endpoints)}")
    # generate graphs
    if not new_endpoints:
        print("No candidates found, exiting.")
        return []

    subject_to: OPQL.query.GraphExpression = graph.filter

    if subject_to:
        endpoints = []
        for candidate_context in new_endpoints:
            if OPQL.query_expression.evaluate_graphexpression(ocel, candidate_context, subject_to):
                endpoints.append(candidate_context)
            else:
                # remove ctx
                if candidate_context.parent:
                    candidate_context.parent.children.remove(candidate_context)
                    candidate_context.parent = None
                else:
                    print("Error: tried to remove context without parent!")

        # prune subtrees that dont satisfy expression!
        for stp in graph_startpoints:
            prune(stp, context_length)

        new_endpoints = endpoints
        # print(f"candidates after applying filter: {len(new_endpoints)}")

    # generate graphs
    if not new_endpoints:
        print("No candidates found, exiting.")
        return []

    # remove graph startpoints that didnt generate any children
    graph_startpoints = [gsp for gsp in graph_startpoints if gsp.children]

    first_graph = OPQL.querycontext.ResultGraph(running_graph_id.get_next_id())
    first_graph.events, first_graph.objects, first_graph.eo_relations, first_graph.eo_relations \
        = OPQL.querycontext.get_bound_entitites(new_endpoints[0], context_length)
    resultgraphs: list[OPQL.querycontext.ResultGraph] = [first_graph]

    # better?: store graph index in hashmap with ocel id as key and graph index as value
    # print(f"collecting entities from {len(new_endpoints)} contexts")
    run_idx = 0
    for context in new_endpoints[1:]:
        run_idx += 1

        ev, ob, eo_rel, oo_rel = OPQL.querycontext.get_bound_entitites(context, context_length)

        in_graphs = []  # : set[ResultGraph] = set()
        for ctx_graph in resultgraphs:
            for event_id in ev:
                if event_id in ctx_graph.events:
                    in_graphs.append(ctx_graph)

            for object_id in ob:
                if object_id in ctx_graph.objects:
                    in_graphs.append(ctx_graph)

        # eliminate duplicates
        in_graphs = list(set(in_graphs))

        if len(in_graphs) == 0:
            new_graph = OPQL.querycontext.ResultGraph(running_graph_id.get_next_id())
            new_graph.events = ev
            new_graph.objects = ob
            new_graph.eo_relations = eo_rel
            new_graph.oo_relations = oo_rel
            resultgraphs.append(new_graph)
        else:
            connected_graph: OPQL.querycontext.ResultGraph = in_graphs[0]
            connected_graph.events |= ev
            connected_graph.objects |= ob
            connected_graph.eo_relations |= eo_rel
            connected_graph.oo_relations |= oo_rel
            # if there are intersections with more than one graphs, these shall be merged
            # add objects and events here first
            if len(in_graphs) == 1:
                for other_graph in in_graphs[1:]:
                    connected_graph.add_to_graph(other_graph)
                    resultgraphs.remove(other_graph)

    # print(f"resulting graphs: {len(resultgraphs)}")
    # for graph in resultgraphs:
    #     draw_graph(graph)

    id_to_graph_map = {}
    for res_graph in resultgraphs:
        for ev_id in res_graph.events:
            id_to_graph_map[ev_id] = res_graph

        for ob_id in res_graph.events:
            id_to_graph_map[ob_id] = res_graph

    # the great reparenting
    # for gsp in graph_startpoints:
    #     children = gsp.children
    #     children_tag = gsp.childrenSymbol
    #
    #     gsp.children = []
    #     gsp.childrenSymbol = graph_tag
    #
    #     for child_ctx in children:
    #         ctype = type(child_ctx.contextEntity)
    #         if ctype == OPQL.querycontext.ContextEvent or ctype == OPQL.querycontext.ContextObject:
    #             ocel_id = child_ctx.contextEntity.ocel_id
    #             associated_graph = id_to_graph_map[ocel_id]
    #             g_begin = OPQL.querycontext.ContextGraphBegin()
    #             g_begin.fullrep = associated_graph
    #
    #             begin_ctx = OPQL.querycontext.QueryContext()
    #             begin_ctx.parent = gsp
    #             begin_ctx.contextEntity = g_begin
    #             begin_ctx.childrenSymbol = children_tag
    #             begin_ctx.children = [child_ctx]
    #             child_ctx.parent = begin_ctx
    #
    #             gsp.children.append(begin_ctx)
    #         else:
    #             print("ERROR graph pattern didnt start with event or object")

    # todo: splice graphs into context end graph
    return new_endpoints


def do_filter(ocel: OPQL.ocellog.OCELLog, filter: OPQL.query.Filter, candidate_endpoints):

    for symbolic_name in filter.entities_to_remove:
        for ce in candidate_endpoints:
            entity = ce.lookupSymbol(symbolic_name)
            if type(entity) == OPQL.querycontext.ContextEvent:
                ocel.deleteEvent(entity.ocel_id)
            elif type(entity) == OPQL.querycontext.ContextObject:
                ocel.deleteObject(entity.ocel_id)
            elif type(entity) == OPQL.querycontext.ContextEORelation:
                if entity.direction == OPQL.querycontext.ContextRelationDirection.ANY:
                    print("ERROR ANY direction should bever be bound to context")
                    continue

                ctx = ce.lookupContext(symbolic_name)
                lhs = ctx.parent.contextEntity

                # this will lead to deleting this relation several times.
                # however, for a first implementation, its fine
                for rhs_ctx in ctx.children:
                    if entity.direction == OPQL.querycontext.ContextRelationDirection.LEFT:
                        ocel.deleteEORelation(rhs_ctx.contextEntity.ocel_id, lhs.ocel_id, entity.ocel_qualifier)
                    elif entity.direction == OPQL.querycontext.ContextRelationDirection.RIGHT:
                        ocel.deleteEORelation(lhs.ocel_id, rhs_ctx.contextEntity.ocel_id, entity.ocel_qualifier)

            elif type(entity) == OPQL.querycontext.ContextOORelation:
                if entity.direction == OPQL.querycontext.ContextRelationDirection.ANY:
                    print("ERROR ANY direction should bever be bound to context")
                    continue

                ctx = ce.lookupContext(symbolic_name)
                lhs = ctx.parent.contextEntity

                # this will lead to deleting this relation several times.
                # however, for a first implementation, its fine
                for rhs_ctx in ctx.children:
                    if entity.direction == OPQL.querycontext.ContextRelationDirection.LEFT:
                        ocel.deleteOORelation(rhs_ctx.contextEntity.ocel_id, lhs.ocel_id, entity.ocel_qualifier)
                    elif entity.direction == OPQL.querycontext.ContextRelationDirection.RIGHT:
                        ocel.deleteOORelation(lhs.ocel_id, rhs_ctx.contextEntity.ocel_id, entity.ocel_qualifier)


def is_in_bin(bin: OPQL.query.BinningInterval, value):
    # TODO properly check somewhere that binning interval limits (a,b) actually fulfill a < b
    if bin.begin is not OPQL.query.BinningInfinity.NEGATIVE_INFINITY:
        if bin.include_begin and value < bin.begin:
            return False

        if not bin.include_begin and value <= bin.begin:
            return False

    if bin.end is not OPQL.query.BinningInfinity.POSITIVE_INFINITY:
        if bin.include_end and value > bin.end:
            return False

        if not bin.include_end and value >= bin.end:
            return False

    return True


def bin_value(binning: list[OPQL.query.BinningInterval], value):
    for interval in binning:
        if is_in_bin(interval, value):
            return interval.target

    print(f"Binning: No suitable interval for value {value}")
    return None


def expand_ctx(ocel, context_ep, expansion: OPQL.query.ProjectionItem):

    ctx_evaluated = OPQL.query_expression.evaluate_graphexpression(ocel, context_ep, expansion.evaluatable)
    context_ep.childrenSymbol = expansion.tag if expansion.tag else str(expansion.evaluatable)

    # if its a solitary value, make this a list to unify handling of results
    if type(ctx_evaluated) != list:
        ctx_evaluated = [ctx_evaluated]

    for value in ctx_evaluated:
        new_ctx_ep = OPQL.querycontext.QueryContext()
        new_ctx_ep.parent = context_ep

        if expansion.binning:
            value = bin_value(expansion.binning, value)
        new_ctx_ep.contextEntity = value

        context_ep.children.append(new_ctx_ep)


def do_keep(ocel: OPQL.ocellog.OCELLog, projection: OPQL.query.Projection, context):
    ctx_eps = [context]

    for expansion in projection.ctx_expansions:
        new_children = []

        for ctx_ep in ctx_eps:
            expand_ctx(ocel, ctx_ep, expansion)

            new_children += ctx_ep.children

        ctx_eps = new_children


    return ctx_eps