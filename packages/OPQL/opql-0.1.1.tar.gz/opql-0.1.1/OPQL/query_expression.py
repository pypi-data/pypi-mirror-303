import datetime

import OPQL.query
import OPQL.querycontext
import OPQL.ocellog


import OPQL.SQLITEResolver

import pandas


# looks up to what value a symbolic name is bound in a context
def get_value(ocel: OPQL.ocellog.OCELLog, context, var_ref: OPQL.query.ValueReference):
    if var_ref is None:
        print("Warning: tried to look up 'None'")
        return None
    if var_ref.name is None:
        return None

    context_binding = context.lookupSymbol(var_ref.name)

    if context_binding is None:
        print(f"Error: Symbol {var_ref.name} could not be resolved.")
        return None

    if type(context_binding) == OPQL.querycontext.ContextEvent:
        if var_ref.timestamp:
            print("Warning: Event properties dont support evaluation times, ignoring")

        if var_ref.property == "ocel_id":
            return context_binding.ocel_id

        event_binding: OPQL.querycontext.ContextEvent = context_binding
        event = ocel.getEvent(event_binding.ocel_id)

        if not var_ref.property:
            return event_binding

        if var_ref.property == "ocel_type":
            return event.getType()

        val = event.getPropertyValue(var_ref.property)

        return val

    if type(context_binding) == OPQL.querycontext.ContextObject:
        object_binding: OPQL.querycontext.ContextObject = context_binding

        if not var_ref.property:
            return object_binding

        if var_ref.property == "ocel_id":
            return context_binding.ocel_id

        if var_ref.property == "ocel_type":
            return context_binding.ocel_type

        if not var_ref.timestamp:
            print("Error: Object properties (except ocel_id and ocel_type) need a point in time to evaluate!")
            return None

        ocelobject = ocel.getObject(object_binding.ocel_id)

        # if timestamp is actual timestamp, go on, if its event, lookup event time and use that
        # if type(timestamp)
        version_ts = None
        if type(var_ref.timestamp) == datetime.datetime:
            version_ts = var_ref.timestamp
        elif type(var_ref.timestamp) == str:
            # if string, must be reference to event
            ctx_entity = context.lookupSymbol(var_ref.timestamp)
            if type(ctx_entity) != OPQL.querycontext.ContextEvent:
                print(f"Error: version symbol {var_ref.timestamp} is not an event, cannot infer datetime")
                return None

            ctx_event: OPQL.querycontext.ContextEvent = ctx_entity
            event = ocel.getEvent(ctx_event.ocel_id)
            version_ts = event.getPropertyValue("ocel_time")
        else:
            print(f"Error: failed to use version timestamp {var_ref.timestamp}"
                  f" of property {var_ref.name}{var_ref.property} ")
            return None

        value = ocelobject.getPropertyValue(var_ref.property, version_ts)

        return value

    if type(context_binding) == OPQL.querycontext.ContextOORelation:
        ctxb: OPQL.querycontext.ContextOORelation = context_binding
        if var_ref.property == "qualifier":
            return ctxb.ocel_qualifier

        print("Error: failed to evaluate OOR context for {str(var_ref)}")
        return None

    if type(context_binding) == OPQL.querycontext.ContextEORelation:
        ctxb: OPQL.querycontext.ContextEORelation = context_binding
        if var_ref.property == "qualifier":
            return ctxb.ocel_qualifier

        print("Error: failed to evaluate EOR context for {str(var_ref)}")
        return None

    if type(context_binding) == OPQL.querycontext.ContextGraphBegin:
        ctxb: OPQL.querycontext.ContextGraphBegin = context_binding
        return ctxb.fullrep

    # simply return whatever value is behind said context
    if not var_ref.property and not var_ref.timestamp:
        return context_binding

    print(f"Error: unknown context object for {str(var_ref)}")
    return None


def get_all_objects_u_addsub(ocel, context, uas: OPQL.query.UnaryAddSub):
    objects = []

    # print("Atomic value type: " + str(type(uas.atomic.value)))

    if type(uas.atomic.value) == OPQL.query.ValueReference:
        valref: OPQL.query.ValueReference = uas.atomic.value
        if valref.property is not None and valref.timestamp is None:
            context_binding = context.lookupSymbol(valref.name)
            if type(context_binding) == OPQL.querycontext.ContextObject:
                objects.append(valref)

    return objects


def get_all_objects_power(ocel, context, power: OPQL.query.Power):
    objects = []

    for uas in power.unary_addsubs:
        objects += get_all_objects_u_addsub(ocel, context, uas)

    return objects


def get_all_objects_muldiv(ocel, context, muldiv: OPQL.query.MulDiv):
    objects = get_all_objects_power(ocel, context, muldiv.power)

    for _, fpower in muldiv.further_powers:
        objects += get_all_objects_power(ocel, context, fpower)

    return objects


def get_all_objects_addsub(ocel, context, addsub: OPQL.query.AddSub):
    objects = get_all_objects_muldiv(ocel, context, addsub.muldiv)

    for sign, further_md, in addsub.further_muldivs:
        objects += get_all_objects_muldiv(ocel, context, further_md)

    return objects


def get_all_objects(ocel, context, expression: OPQL.query.GraphExpression):
    objects = []
    for ex_xor in expression.XORs:
        ex_xor: OPQL.query.GraphExXOR

        for ex_and in ex_xor.ANDs:
            ex_and: OPQL.query.GraphExAND

            for ex_not in ex_and.NOTs:
                ex_not: OPQL.query.GraphExNOT

                comp: OPQL.query.Comparison = ex_not.comparison
                objects += get_all_objects_addsub(ocel, context, comp.addsub)

                for sign, further_as in comp.further_addsubs:
                    objects += get_all_objects_addsub(ocel, context, further_as)

    return objects


def find_undetermined_object_properties(ocel, context, expression):
    unbound_props = [obj for obj in get_all_objects(ocel, context, expression) if obj.timestamp is None]
    return unbound_props


def evaluate_function(ocel, context, function_call: OPQL.query.Function):
    f_name = function_call.name

    # when is a bit of a special case since it receives the unevaluated expression as function argument
    # and then tries to find all points in time where that expression becomes true
    if f_name == "when":
        # TODO rigorous type checking
        # assert len(function_call.arguments == 1)
        expression = function_call.arguments[0].arg

        unbound_props = find_undetermined_object_properties(ocel, context, expression)

        obs_to_lookup = [val_ref.name for val_ref in unbound_props]
        pts_in_time_to_eval = []
        for ocel_object in obs_to_lookup:
            ctx_bound_obj = context.lookupSymbol(ocel_object)

            # TODO currently this is full history, although property dependent history would technically suffice
            full_history = ocel.getObject(ctx_bound_obj.ocel_id).getFullHistory()
            pts_in_time_to_eval += full_history

        # TODO probably cheaper to just allow for some more-than-once evaluations and remove duplicates
        # only in the end, since evaluations here should be cheap (remember, no functions allowed)
        pts_in_time_to_eval = list(set(pts_in_time_to_eval))

        def eval_ex_at(ocel, context, expression, timestamp, objects_to_bind):
            for object_ref in objects_to_bind:
                object_ref.timestamp = timestamp

            result = evaluate_graphexpression(ocel, context, expression)

            for object_ref in objects_to_bind:
                object_ref.timestamp = None

            return result

        valid_points_in_time = [timestamp for timestamp in pts_in_time_to_eval
                                if eval_ex_at(ocel, context, expression, timestamp, unbound_props)]

        return valid_points_in_time

    args = []
    for f_arg in function_call.arguments:
        if type(f_arg.arg) == OPQL.query.GraphExpression:
            args.append(evaluate_graphexpression(ocel, context, f_arg.arg))
        elif type(f_arg.arg) == OPQL.query.FullQuery:
            subquery: OPQL.query.FullQuery = f_arg.arg

            if len(subquery.return_rule.projection.ctx_expansions) != 1:
                print("Error: only subqueries with single return column supported")
                return None

            subquery_dataframe = OPQL.SQLITEResolver.resolve_query(ocel, subquery, root_context=context)

            args.append(subquery_dataframe)

        else:
            print(f"Error: unknown argument type {type(f_arg.arg)}")

    if f_name == "count":
        if not len(args) == 1:
            print(f"Error: invalid number of arguments for function {f_name} {len(args)}")

        if type(args[0]) != pandas.DataFrame:
            print(f"Error: invalid type of argument for function {f_name} {type(args[0])}")

        rowcount = args[0].shape[0]

        return rowcount
    elif f_name == "avg":
        if not len(args) == 1:
            print(f"Error: invalid number of arguments for function {f_name} {len(args)}")

        if type(args[0]) != pandas.DataFrame:
            print(f"Error: invalid type of argument for function {f_name} {type(args[0])}")

        avg = args[0].mean()[0]
        return avg
    elif f_name == "median":
        if not len(args) == 1:
            print(f"Error: invalid number of arguments for function {f_name} {len(args)}")

        if type(args[0]) != pandas.DataFrame:
            print(f"Error: invalid type of argument for function {f_name} {type(args[0])}")

        median = args[0].median()[0]
        return median
    elif f_name == "sum":
        if not len(args) == 1:
            print(f"Error: invalid number of arguments for function {f_name} {len(args)}")

        if type(args[0]) != pandas.DataFrame:
            print(f"Error: invalid type of argument for function {f_name} {type(args[0])}")

        sum = args[0].sum()[0]
        return sum
    elif f_name == "stddev":
        if not len(args) == 1:
            print(f"Error: invalid number of arguments for function {f_name} {len(args)}")

        if type(args[0]) != pandas.DataFrame:
            print(f"Error: invalid type of argument for function {f_name} {type(args[0])}")

        std = args[0].std()[0]
        return std
    elif f_name == "max":
        if not len(args) == 1:
            print(f"Error: invalid number of arguments for function {f_name} {len(args)}")

        if type(args[0]) != pandas.DataFrame:
            print(f"Error: invalid type of argument for function {f_name} {type(args[0])}")

        max = args[0].max()[0]
        return max
    elif f_name == "min":
        if not len(args) == 1:
            print(f"Error: invalid number of arguments for function {f_name} {len(args)}")

        if type(args[0]) != pandas.DataFrame:
            print(f"Error: invalid type of argument for function {f_name} {type(args[0])}")

        min = args[0].min()[0]
        return min
    elif f_name == "olead" or f_name == "olag":
        if len(args) < 2:
            print(f"Error: Not enough arguments provided to {f_name}, at least 2 required")
            return None

        # TODO do rigorous type checking here

        event = args[0]
        object = args[1]

        offset = 0
        etype = None

        if len(args) == 3:
            if type(args[2]) == str:
                etype = args[2]
            elif type(args[2]) == int:
                offset = args[2]

        lag = True if f_name == "olag" else False
        result = ocel.olaglead(event.ocel_id,
                               object.ocel_id,
                               lag,
                               offset,
                               etype)

        if result:
            return OPQL.querycontext.ContextEvent(ocel_id=result, ocel_type=ocel.getEventType(result))

        return None
    else:
        print(f"Error: unknown function called: {f_name}")


def evaluate_atomic(ocel, context, atom: OPQL.query.Atomic):
    if type(atom.value) == str:
        return atom.value

    if type(atom.value) == int:
        return atom.value

    if type(atom.value) == float:
        return atom.value

    if type(atom.value) == datetime.datetime:
        return atom.value

    if type(atom.value) == OPQL.query.ValueReference:
        return get_value(ocel, context, atom.value)

    if type(atom.value) == OPQL.query.Function:
        return evaluate_function(ocel, context, atom.value)

    print(f"Error: failed to determine value of {atom.value}")
    return None


def evaluate_unary_addsub(ocel, context, uas: OPQL.query.UnaryAddSub):
    atom_val = evaluate_atomic(ocel, context, uas.atomic)

    if type(atom_val) == str:
        return atom_val

    if uas.sign:
        if uas.sign == OPQL.query.SignAddSub.ADD:
            return atom_val
        elif uas.sign == OPQL.query.SignAddSub.SUB:
            return -1*atom_val

    return atom_val


def evaluate_power(ocel, context, power: OPQL.query.Power):
    rval = evaluate_unary_addsub(ocel, context, power.unary_addsubs[0])

    if len(power.unary_addsubs) == 1:
        return rval

    for uas in power.unary_addsubs[1:-1]:
        rhs_val = evaluate_unary_addsub(ocel, context, uas)
        rval = rval ** rhs_val

    return rval


def evaluate_muldiv(ocel, context, muldiv: OPQL.query.MulDiv):
    rval = evaluate_power(ocel, context, muldiv.power)

    if not muldiv.further_powers:
        return rval

    for next_op in muldiv.further_powers:
        rhs_val = evaluate_power(ocel, context, next_op[1])

        if next_op[0] == OPQL.query.SignMulDivMod.MUL:
            rval = rval * rhs_val
        elif next_op[0] == OPQL.query.SignMulDivMod.DIV:
            rval = rval / rhs_val
        elif next_op[0] == OPQL.query.SignMulDivMod.MOD:
            rval = rval % rhs_val
        else:
            print(f"Error: unknown operation in muldiv (neither mul / div / mod): {next_op[0]}")

    return rval


def evaluate_addsub(ocel, context, addsub: OPQL.query.AddSub):
    rval = evaluate_muldiv(ocel, context, addsub.muldiv)

    if not addsub.further_muldivs:
        return rval

    for next_op in addsub.further_muldivs:
        rhs_val = evaluate_muldiv(ocel, context, next_op[1])
        if next_op[0] == OPQL.query.SignAddSub.ADD:
            rval = rval + rhs_val
        elif next_op[0] == OPQL.query.SignAddSub.SUB:
            rval = rval - rhs_val
        else:
            print("Error: unknown operation in addsub (neither add nor sub)")

    return rval


def run_comparison(lhs, rhs, sign: OPQL.query.ComparisonSign) -> bool:
    if not type(lhs) == type(rhs):
        print(f"Error: comparison of {type(lhs)} and {type(rhs)} not implemented")

    assert type(lhs) == type(rhs)

    match sign:
        case OPQL.query.ComparisonSign.EQUAL_TO:
            return lhs == rhs
        case OPQL.query.ComparisonSign.LE:
            return lhs <= rhs
        case OPQL.query.ComparisonSign.GE:
            return lhs >= rhs
        case OPQL.query.ComparisonSign.LT:
            return lhs < rhs
        case OPQL.query.ComparisonSign.GT:
            return lhs > rhs
        case OPQL.query.ComparisonSign.NOT_EQUAL:
            return lhs != rhs
        case _:
            print(f"Error: unknown comparison sign {sign.__repr__()}")
            print("Evaluating to False!")

    return False


def evaluate_comp(ocel, context, comparison: OPQL.query.Comparison) -> bool | None:
    val_mlh = evaluate_addsub(ocel, context, comparison.addsub)

    # simply hand through if no further operation specified
    if not comparison.further_addsubs:
        return val_mlh

    truth_val = None
    rhs = comparison.further_addsubs[0][1]
    rhs_val = evaluate_addsub(ocel, context, rhs)
    sign = comparison.further_addsubs[0][0]

    try:
        # dereferencing safe since we already checked that further_addsubs has at least 1 element
        truth_val = run_comparison(val_mlh, rhs_val, sign)
        # print(f"{val_mlh}{sign}{rhs_val} is {truth_val}")
    except:
        print(f"Error: Failed to compare {val_mlh}{sign}{rhs} of types {type(val_mlh)}{type(rhs_val)}")
        return None

    prev_val = rhs_val
    for sign, rhs in comparison.further_addsubs[1:]:
        rhs_val = evaluate_addsub(ocel, context, rhs)
        try:
            truth_val = truth_val and run_comparison(prev_val, rhs_val, sign)
            # print(f"{prev_val}{sign}{rhs_val} is {truth_val}")
        except:
            print(f"Error: Failed to compare {prev_val}{sign}{rhs_val} of types {type(prev_val)}{type(rhs_val)}")
            return None
        prev_val = rhs_val

        # no need to continue if already false
        if not truth_val:
            break

    return truth_val


def evaluate_not(ocel, context, g_not: OPQL.query.GraphExNOT) -> bool:
    val = evaluate_comp(ocel, context, g_not.comparison)

    if not g_not.invert:
        return val

    return not val


def evaluate_and(ocel, context, g_and: OPQL.query.GraphExAND) -> bool:
    if len(g_and.NOTs) == 1:
        return evaluate_not(ocel, context, g_and.NOTs[0])

    for g_not in g_and.NOTs:
        # if at least one is false, the whole expression becomes false
        if not evaluate_not(ocel, context, g_not):
            return False

    return True


def evaluate_xor(ocel, context, xor: OPQL.query.GraphExXOR) -> bool:
    vals = [evaluate_and(ocel, context, g_and) for g_and in xor.ANDs]

    rval = vals[0]

    if len(vals) > 1:
        for val in vals[1:-1]:
            # != is for all intends and purposes XOR
            rval = rval != val

    return rval


def evaluate_graphexpression(ocel, context, expression: OPQL.query.GraphExpression) -> bool:
    # if there is only one, simply hand value through
    if len(expression.XORs) == 1:
        return evaluate_xor(ocel, context, expression.XORs[0])

    # all elements of an expression are ORed together, so if the first one is true, just return true.
    for xor in expression.XORs:
        rval = evaluate_xor(ocel, context, xor)

        if rval:
            return True

    # if none evaluated true, return False
    return False
