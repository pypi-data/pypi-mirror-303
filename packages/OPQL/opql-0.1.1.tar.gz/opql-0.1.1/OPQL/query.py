import enum


class Atomic:
    def __init__(self):
        self.value = None

    def __str__(self):
        return self.value.__str__()


class SignAddSub(enum.Enum):
    ADD = 0
    SUB = 1

    def __str__(self):
        res = ""
        if self.value == 0:
            res = "+"
        elif self.value == 1:
            res = "-"

        return res


class UnaryAddSub:
    def __init__(self):
        self.sign: SignAddSub | None = None
        self.atomic: Atomic | None = None

    def __str__(self):
        res = ""
        if self.sign:
            res += self.sign.__str__()

        res += self.atomic.__str__()

        return res


class Power:
    def __init__(self):
        # power is encompassed of only one operation so no need to carry tuples here
        self.unary_addsubs: list[UnaryAddSub] = []

    def __str__(self):
        if not self.unary_addsubs:
            return ""

        res = self.unary_addsubs[0].__str__()

        for i in range(1, len(self.unary_addsubs)):
            res += " ^ " + self.unary_addsubs[i].__str__()

        return res


class SignMulDivMod(enum.Enum):
    MUL = 0
    DIV = 1
    MOD = 2

    def __str__(self):
        res = ""
        if self.value == 0:
            res = "*"
        elif self.value == 1:
            res = "/"
        elif self.value == 2:
            res = "%"

        return res


class MulDiv:
    def __init__(self):
        self.power = None
        self.further_powers: list[tuple] = []

    def __str__(self):
        if not self.power:
            return ""

        res = self.power.__str__()

        for f_tpl in self.further_powers:
            res += " " + f_tpl[0].__str__() + " " + f_tpl[1].__str__()

        return res


class AddSub:
    def __init__(self):
        self.muldiv: MulDiv | None = None
        self.further_muldivs: list[tuple[SignAddSub, MulDiv]] = []

    def __str__(self):
        if not self.muldiv:
            return ""

        res = self.muldiv.__str__()

        for f_tpl in self.further_muldivs:
            res += " " + f_tpl[0].__str__() + " " + f_tpl[1].__str__()

        return res


class ComparisonSign(enum.Enum):
    EQUAL_TO = 0
    LE = 1
    GE = 2
    GT = 3
    LT = 4
    NOT_EQUAL = 5

    def __str__(self):
        res = ""
        if self.value == 0:
            res = "=="
        elif self.value == 1:
            res = "<="
        elif self.value == 2:
            res = ">="
        elif self.value == 3:
            res = ">"
        elif self.value == 4:
            res = "<"
        elif self.value == 5:
            res = "!="

        return res


class Comparison:
    def __init__(self):
        self.addsub = None

        # tuples are (comparison sign, addsub)
        self.further_addsubs: list[tuple[ComparisonSign, AddSub]] = []

    def __str__(self):
        if not self.addsub:
            return ""

        res = self.addsub.__str__()

        for f_tpl in self.further_addsubs:
            res += " " + f_tpl[0].__str__() + " " + f_tpl[1].__str__()

        return res


class GraphExNOT:
    def __init__(self):
        self.invert = False
        self.comparison: Comparison | None = None

    def __str__(self):
        res = ""

        if self.invert:
            res += "NOT "

        if not self.comparison:
            return "None"

        wubba = self.comparison.__str__()
        res += wubba

        return res


class GraphExAND:
    def __init__(self):
        self.NOTs: list[GraphExNOT] = []

    def __str__(self):
        if not self.NOTs:
            return ""

        res = self.NOTs[0].__str__()

        for i in range(1, len(self.NOTs)):
            res += " OR " + self.NOTs[i].__str__()

        return res


class GraphExXOR:
    def __init__(self):
        self.ANDs: list[GraphExAND] = []

    def __str__(self):
        if not self.ANDs:
            return ""

        res = self.ANDs[0].__str__()

        for i in range(1, len(self.ANDs)):
            res += " XOR " + self.ANDs[i].__str__()

        return res


class GraphExpression:
    def __init__(self):
        # OR these subterms
        self.XORs: list[GraphExXOR] = []

    def __str__(self):
        if not self.XORs:
            return ""

        res = self.XORs[0].__str__()

        for i in range(1, len(self.XORs)):
            res += " OR " + self.XORs[i].__str__()

        return res


class GraphObject:
    def __init__(self):
        self.tag = None
        self.type = None

    def __str__(self):
        return f"O({self.tag} : {self.type})"


class GraphEvent:
    def __init__(self):
        self.tag = None
        self.type = None

    def __str__(self):
        return f"E({self.tag} : {self.type})"


class GraphRelationDirection(enum.Enum):
    RIGHT = 1
    LEFT = 2
    ANY = 3


class GraphRelation:
    def __init__(self):
        self.tag = None
        self.type = None
        self.direction = None

    def __str__(self):
        return f"-[{self.tag} : {self.type} direction: {self.direction}]-"


class ValueReference:
    def __init__(self):
        self.name = None
        self.property = None
        self.timestamp = None

    def __str__(self):
        res_str = self.name
        if self.property:
            res_str += "." + self.property

        if self.timestamp:
            res_str += "@" + str(self.timestamp)

        return res_str


class FunctionArgument:
    def __init__(self):
        self.arg = None

    def __str__(self):
        res = self.arg.__str__()

        if res:
            return res

        return "FARG"


class Function:
    def __init__(self):
        self.name: str | None = None
        self.arguments = []

    def __str__(self):
        res = self.name + "("

        if self.arguments:
            res += self.arguments[0].__str__()

        for i in range(1, len(self.arguments)):
            res += "," + self.arguments[i].__str__()

        return res + ")"


class Graph:
    def __init__(self):
        self.tag = None
        self.patterns = []
        self.filter = None


class Filter:
    def __init__(self):
        self.entities_to_remove: list = []


class OrderDirection(enum.Enum):
    ASC = 0
    DESC = 1


class OrderItem:
    def __init__(self):
        self.expression = None
        self.direction = None


class BinningInfinity(enum.Enum):
    NEGATIVE_INFINITY = 0
    POSITIVE_INFINITY = 1


class BinningInterval:
    def __init__(self):
        self.begin = None
        self.end = None
        self.include_begin = False
        self.include_end = False

        self.target = None


class ProjectionItem:
    def __init__(self):
        self.tag = None
        self.evaluatable = None
        self.binning = None


class Projection:
    def __init__(self):
        # wildcard denotes whether to keep context up until here
        self.wildcard = False
        self.distinct = False
        self.ctx_expansions: list[tuple] = []

        # expressions evaluating to numbers for ordering
        self.order: list[OrderItem] = []

        # integer "row" limit
        self.limit = None


class Keep:
    def __init__(self):
        self.projection = None
        self.filter = None


class Return:
    def __init__(self):
        self.ocel: bool = False
        self.projection = None
        self.filter = None


class FullQuery:
    def __init__(self):
        self.graphsAndFilters = []
        self.return_rule = []
