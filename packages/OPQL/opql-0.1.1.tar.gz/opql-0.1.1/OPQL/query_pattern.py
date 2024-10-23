import OPQL.ocellog
import OPQL.query
import OPQL.querycontext

import itertools
import multiprocessing
import multiprocessing.pool


# returns a list of possible binding contexts
def resolve_event_single(ocel: OPQL.ocellog.OCELLog,
                         context: OPQL.querycontext.QueryContext,
                         event: OPQL.query.GraphEvent) -> list[OPQL.querycontext.ContextEvent]:
    context_event = context.lookupSymbol(event.tag)
    if context_event is not None:
        return [context_event]

        # no such event known in context, could be "anything"
    if event.type is not None:
        # look up events of said type
        candidate_event_ids = ocel.getEventIdsByType(event.type)
        return [OPQL.querycontext.ContextEvent(ocel_id, event.type) for ocel_id in candidate_event_ids]

    # could be any event
    candidate_event_ids = ocel.getEventIds()
    return [OPQL.querycontext.ContextEvent(ocel_id, ocel.getEventType(ocel_id)) for ocel_id in candidate_event_ids]


def resolve_object_single(ocel: OPQL.ocellog.OCELLog,
                          context: OPQL.querycontext.QueryContext,
                          g_object: OPQL.query.GraphObject) -> list[OPQL.querycontext.ContextObject]:
    context_object = context.lookupSymbol(g_object.tag)
    if context_object is not None:
        return [context_object]

    # no such object known in context, could be "anything"
    if g_object.type is not None:
        # look up events of said type
        candidate_object_ids = ocel.getObjectIdsByType(g_object.type)
        return [OPQL.querycontext.ContextObject(ocel_id, g_object.type) for ocel_id in candidate_object_ids]

    # could be any event
    candidate_object_ids = ocel.getObjectIds()
    return [OPQL.querycontext.ContextObject(ocel_id, ocel.getObjectType(ocel_id)) for ocel_id in candidate_object_ids]


def resolve_relation(ocel: OPQL.ocellog.OCELLog,
                     context: OPQL.querycontext.QueryContext,
                     lh_entity: OPQL.querycontext.ContextEvent | OPQL.querycontext.ContextObject,
                     relation: OPQL.query.GraphRelation,
                     endpoint: OPQL.query.GraphEvent | OPQL.query.GraphObject) -> list[(str, str)]:
    # TODO: handle tagged relations!
    # check if entry is pinned to any symbolic name already, will greatly reduce result list

    endpoint_id = None

    endpoint_cto = context.lookupSymbol(endpoint.tag)
    if endpoint_cto:
        endpoint_id = endpoint_cto.ocel_id

    if type(lh_entity) == OPQL.querycontext.ContextObject and type(endpoint) == OPQL.query.GraphObject:
        result = []
        if relation.direction == OPQL.query.GraphRelationDirection.LEFT \
                or relation.direction == OPQL.query.GraphRelationDirection.ANY:
            lh_result = ocel.getOORelations(source_id=endpoint_id, source_type=endpoint.type,
                                          target_id=lh_entity.ocel_id, target_type=lh_entity.ocel_type,
                                          qualifier=relation.type)
            # context object is of source_id and source_type since the relation is in reverse / left direction
            tf_res = [(OPQL.querycontext.ContextOORelation(resultrow[-1], OPQL.querycontext.ContextRelationDirection.LEFT),
                       OPQL.querycontext.ContextObject(resultrow[0], resultrow[1]))
                      for resultrow in lh_result]
            result += tf_res
        elif relation.direction == OPQL.query.GraphRelationDirection.RIGHT \
                or relation.direction == OPQL.query.GraphRelationDirection.ANY:
            rh_result = ocel.getOORelations(source_id=lh_entity.ocel_id, source_type=lh_entity.ocel_type,
                                            target_id=endpoint_id, target_type=endpoint.type,
                                            qualifier=relation.type)
            tf_res = [(OPQL.querycontext.ContextOORelation(resultrow[-1], OPQL.querycontext.ContextRelationDirection.RIGHT),
                       OPQL.querycontext.ContextObject(resultrow[2], resultrow[3]))
                      for resultrow in rh_result]
            result += tf_res

        return result

    elif type(lh_entity) == OPQL.querycontext.ContextEvent and type(endpoint) == OPQL.query.GraphObject:
        if relation.direction == OPQL.query.GraphRelationDirection.LEFT:
            # objects pointing at events are illegal by definition
            return []
        elif relation.direction == OPQL.query.GraphRelationDirection.RIGHT \
                or relation.direction == OPQL.query.GraphRelationDirection.ANY:
            result = ocel.getEORelations(event_id=lh_entity.ocel_id, event_type=lh_entity.ocel_type,
                                         object_id=endpoint_id, object_type=endpoint.type,
                                         qualifier=relation.type)

            tf_res = [(OPQL.querycontext.ContextEORelation(resultrow[-1], OPQL.querycontext.ContextRelationDirection.RIGHT),
                       OPQL.querycontext.ContextObject(resultrow[2], resultrow[3]))
                      for resultrow in result]
            return tf_res

    elif type(lh_entity) == OPQL.querycontext.ContextObject and type(endpoint) == OPQL.query.GraphEvent:
        if relation.direction == OPQL.query.GraphRelationDirection.RIGHT:
            # objects pointing at events are illegal by definition
            return []
        elif relation.direction == OPQL.query.GraphRelationDirection.LEFT or relation.direction == OPQL.query.GraphRelationDirection.ANY:
            result = ocel.getEORelations(event_id=endpoint_id, event_type=endpoint.type,
                                         object_id=lh_entity.ocel_id, object_type=lh_entity.ocel_type,
                                         qualifier=relation.type)
            tf_res = [(OPQL.querycontext.ContextEORelation(resultrow[-1], OPQL.querycontext.ContextRelationDirection.LEFT),
                       OPQL.querycontext.ContextEvent(resultrow[0], resultrow[1]))
                      for resultrow in result]
            return tf_res

    # print(f"Warning: did not run into any legal entity-relation case while resolving {str(lh_entity)}{str(relation)}{str(endpoint)}")
    return []


# returns the relative depth of the endpoint to root
# will return -1 on error (e.g. endpoint has no upstream connection to root)
def get_relative_depth(root: OPQL.querycontext.QueryContext, endpoint: OPQL.querycontext.QueryContext):
    rel_dep = 0

    root_found = False
    current_node = endpoint

    while not root_found:
        # break condition 1: root found, done counting
        if current_node == root:
            root_found = True
            break

        # break condition 2 (error): cannot go further up, but root is not found.
        if current_node.parent is None:
            print(f"Error in finding relative depth from {endpoint} to {root}")
            rel_dep = -1
            break

        # increase depth, go further upwards
        current_node = current_node.parent
        rel_dep += 1

    return rel_dep


# generates further candidates for given context(entity) and relationship entity pair
def generate_candidates(ocel, context: OPQL.querycontext.QueryContext, rel_entity_pair: tuple) -> list[OPQL.querycontext.QueryContext]:
    relation = rel_entity_pair[0]
    endpoint = rel_entity_pair[1]

    #   generate new candidates from all current candidates
    # keep track of candidates that did not produce any children and therefore need to be pruned
    # TODO can this be removed since unused?
    children_to_prune = []
    candidate = context

    lefthand_entity = candidate.contextEntity
    new_candidates = resolve_relation(ocel, candidate, lefthand_entity, relation, endpoint)

    # could not generate any matching patterns - this is a dead end
    if not new_candidates:
        return []

    candidate.childrenSymbol = relation.tag

    # first, extract relations from new candidates as new context entity
    rel_names = set([rel_ent[0] for rel_ent in new_candidates])

    relations_with_children = {}
    for r in rel_names:
        relations_with_children[r] = []

    for rel_ent in new_candidates:
        relations_with_children[rel_ent[0]].append(rel_ent[1])

    endpoint_candidates = []
    new_children = []
    # second, add entities that are connected via each relation to context tree
    for key in relations_with_children:
        # create relation context
        rel_context = OPQL.querycontext.QueryContext(parent=candidate,
                                                     context_entity=key,
                                                     children_symbol=endpoint.tag,
                                                     children=[])
        children_ctx_entities = relations_with_children[key]
        children_ctx = [OPQL.querycontext.QueryContext(parent=rel_context,
                                                       context_entity=ctx_entity,
                                                       children_symbol=None,
                                                       children=[])
                        for ctx_entity in children_ctx_entities]
        # add children to relation context and parent them to it
        rel_context.children = children_ctx

        # finally add subtree to parent
        new_children.append(rel_context)

        # and add leaves as new candidates
        endpoint_candidates += children_ctx

    # copying while setting this new list is of
    # IMMENSE importance since the previous approach lead to all contexts referencing the same list somehow
    candidate.children = new_children

    if not endpoint_candidates:
        print("Error: no endpoint candidates for new candidates:")
        print(f"{new_candidates}")

    return endpoint_candidates


def find_children(ocel, context: OPQL.querycontext.QueryContext, rel_entity_pairs) -> list[OPQL.querycontext.QueryContext]:
    assert rel_entity_pairs

    next_pair = rel_entity_pairs[0]

    new_candidates: list[OPQL.querycontext.QueryContext] = generate_candidates(ocel, context, next_pair)

    # if there are no other relations to resolve, return.
    # also return if there are no new candidates generated,
    # essentially meaning that this context binding is not solvable
    if not new_candidates or len(rel_entity_pairs) == 1:
        return new_candidates

    if len(rel_entity_pairs) > 1:
        further_rel_ent_pairs = rel_entity_pairs[1:]

        endpoints: list[OPQL.querycontext.QueryContext] = []
        for ctx_candidate in new_candidates:
            candidate_endpoints = find_children(ocel, ctx_candidate, further_rel_ent_pairs)

            if not candidate_endpoints:
                # this candidate is a dead end, remove.
                ctx_candidate.parent.children.remove(ctx_candidate)
                # also remove parent reference to
                ctx_candidate.parent = None

                # do next candidate without adding to legitimate endpoints
                continue

            endpoints += candidate_endpoints

        return endpoints
        # find children with all generated context ends
        # get those that didnt return None
        # return these. or return None if none had valid children

        # do tail recursion


def check_cand_ctx(ocel, candidate_ctxs: list, rel_entity_pairs, resulting_endpoints):
    for candidate_ctx in candidate_ctxs:
        endpoints = find_children(ocel, candidate_ctx, rel_entity_pairs)

        if not endpoints:
            if candidate_ctx.parent:
                candidate_ctx.parent.children.remove(candidate_ctx)
            candidate_ctx.parent = None
        else:
            resulting_endpoints += endpoints


# not only is this slower but also produces inconsistent results, i.e. threading model is wrong.
def find_pattern_candidates_multi(ocel, context, pattern):
    print("WARNING: using concurrent candidate finding")
    print("WARNING: not only is this slower but also produces inconsistent results, i.e. threading model is wrong.")
    if len(pattern) == 0:
        return [context]

    pattern_head = pattern[0]
    context.childrenSymbol = pattern_head.tag
    candidates = []
    if type(pattern_head) == OPQL.query.GraphEvent:
        candidates = resolve_event_single(ocel, context, pattern_head)
    elif type(pattern_head) == OPQL.query.GraphObject:
        candidates = resolve_object_single(ocel, context, pattern_head)
    else:
        print("Error: encountered unknown node type")

    if pattern_head.tag:
        context.tag = pattern_head.tag

    if not candidates:
        print("ERROR no candidates found for pattern head " + str(pattern_head))
        return

    context.children = [OPQL.querycontext.QueryContext(parent=context, contextEntity=candidate) for candidate in
                        candidates]

    rel_entity_pairs = []
    for i in range(1, (len(pattern) - 1), 2):
        rel_entity_pairs.append((pattern[i], pattern[i + 1]))

    current_candidates: list[OPQL.querycontext.QueryContext] = context.children

    resulting_endpoints = []

    # no of logical cpus
    no_cpus = multiprocessing.cpu_count()
    print(f"checking candidates with {no_cpus} threads")

    rest = len(current_candidates) % no_cpus
    packsize = int((len(current_candidates) - rest) / no_cpus)


    workpacks = [current_candidates[i*packsize:(i+1)*packsize] for i in range(0,no_cpus)]
    leftovers = current_candidates[-rest:]
    workpacks.append(leftovers)

    def wrap_cand(params):
        check_cand_ctx(*params)

    with multiprocessing.pool.ThreadPool(no_cpus) as pool:
        # ocel, candidate_ctx, rel_entity_pairs, resulting_endpoints
        paramstuff = zip(itertools.repeat(ocel),
                         workpacks,
                         itertools.repeat(rel_entity_pairs),
                         itertools.repeat(resulting_endpoints))

        pool.map(wrap_cand, paramstuff)
        print("yay")

    return resulting_endpoints


def find_pattern_candidates(ocel, context, pattern):
    if len(pattern) == 0:
        return [context]

    pattern_head = pattern[0]

    candidates = []
    if type(pattern_head) == OPQL.query.GraphEvent:
        candidates = resolve_event_single(ocel, context, pattern_head)
    elif type(pattern_head) == OPQL.query.GraphObject:
        candidates = resolve_object_single(ocel, context, pattern_head)
    else:
        print("Error: encountered unknown node type")

    if pattern_head.tag:
        context.childrenSymbol = pattern_head.tag

    if not candidates:
        print("ERROR no candidates found for pattern head " + str(pattern_head))
        return

    context.children = [OPQL.querycontext.QueryContext(parent=context, context_entity=candidate)
                        for candidate in candidates]

    rel_entity_pairs = []
    for i in range(1, (len(pattern) - 1), 2):
        rel_entity_pairs.append((pattern[i], pattern[i + 1]))

    if not rel_entity_pairs:
        return context.children

    current_candidates: list[OPQL.querycontext.QueryContext] = context.children

    resulting_endpoints = []

    for candidate_ctx in current_candidates:
        endpoints = find_children(ocel, candidate_ctx, rel_entity_pairs)

        if not endpoints:
            if candidate_ctx.parent:
                candidate_ctx.parent.children.remove(candidate_ctx)
            candidate_ctx.parent = None
            continue

        resulting_endpoints += endpoints

    return resulting_endpoints


# we keep this old one here cuz its twice as fast,
# lots of this stems from not removing dead-end candidates
def evaluate_pattern(ocel, context, pattern):
    if len(pattern) == 0:
        return [context]

    pattern_head = pattern[0]
    context.childrenSymbol = pattern_head.tag
    candidates = []
    if type(pattern_head) == OPQL.query.GraphEvent:
        candidates = resolve_event_single(ocel, context, pattern_head)
    elif type(pattern_head) == OPQL.query.GraphObject:
        candidates = resolve_object_single(ocel, context, pattern_head)

    if pattern_head.tag:
        context.tag = pattern_head.tag

    if not candidates:
        print("ERROR no candidates found for pattern head " + str(pattern_head))
        return

    context.children = [OPQL.querycontext.QueryContext(parent=context, contextEntity=candidate) for candidate in candidates]

    rel_entity_pairs = []
    for i in range(1, (len(pattern) - 1), 2):
        rel_entity_pairs.append((pattern[i], pattern[i+1]))

    current_candidates = context.children
    # for every relationship+entity pair:

    for rel_entity_pair in rel_entity_pairs:
        relation = rel_entity_pair[0]
        endpoint = rel_entity_pair[1]
        relen_candidates = []

        #   generate new candidates from all current candidates
        # keep track of candidates that did not produce any children and therefore need to be pruned
        children_to_prune = []
        for candidate in current_candidates:
            lefthand_entity = candidate.contextEntity
            new_candidates = resolve_relation(ocel, candidate, lefthand_entity, relation, endpoint)

            # could not generate any matching patterns - this is a dead end
            if not new_candidates:
                children_to_prune.append(candidate)
                continue

            candidate.childrenSymbol = relation.tag

            # first, extract relations from new candidates as new context entity
            rel_names = set([rel_ent[0] for rel_ent in new_candidates])

            relations_with_children = {}
            for r in rel_names:
                relations_with_children[r] = []

            for rel_ent in new_candidates:
                relations_with_children[rel_ent[0]].append(rel_ent[1])

            endpoint_candidates = []
            # second, add entities that are connected via each relation to context tree
            for key in relations_with_children:
                # create relation context
                rel_context = OPQL.querycontext.QueryContext(parent=candidate,
                                                             contextEntity=key,
                                                             childrenSymbol=endpoint.tag,
                                                             children=[])
                children_ctx_entities = relations_with_children[key]
                children_ctx = [OPQL.querycontext.QueryContext(parent=rel_context,
                                                               contextEntity=ctx_entity,
                                                               childrenSymbol=None, children=[])
                                for ctx_entity in children_ctx_entities]
                # add children to relation context and parent them to it
                rel_context.children = children_ctx

                # finally add subtree to parent
                candidate.children.append(rel_context)

                # and add leaves as new candidates
                endpoint_candidates += children_ctx

            relen_candidates += endpoint_candidates

        # prune away candidates that didnt generate any further contexts
        # TODO this needs rewriting to actually remove them from their parents
        # for to_be_pruned in children_to_prune:
        #     current_candidates.remove(to_be_pruned)

        # check if actually candidates were found, if not, remove everything generated this round and return
        if not relen_candidates:
            # TODO add some useful information on what point of graph failed here.
            print("No suitable candidates found, exiting.")
            break

        # update list of current candidates to those new candidates
        # so that the next relationship+entity pair is run on those
        current_candidates = relen_candidates

    print("Candidate generation done!")
    return current_candidates
