class Node(object):
    pass


class Instructions(Node):
    def __init__(self, instructions):
        self.instructions = instructions

    def append(self, instruction):
        self.instructions.append(instruction)


class IntNum(Node):
    def __init__(self, value):
        self.value = value


class FloatNum(Node):
    def __init__(self, value):
        self.value = value


class Variable(Node):
    def __init__(self, name):
        self.name = name


class BinExpr(Node):
    def __init__(self, operator, left, right):
        self.operator = operator
        self.left = left
        self.right = right


class RelExpr(Node):
    def __init__(self, operator, left, right):
        self.operator = operator
        self.left = left
        self.right = right


class AssignExpr(Node):
    def __init__(self, operator, left, right):
        self.operator = operator
        self.left = left
        self.right = right


class IfExpr(Node):
    def __init__(self, condition, expression):
        self.condition = condition
        self.expression = expression


class IfElseExpr(Node):
    def __init__(self, condition, expression1, expression2):
        self.condition = condition
        self.expression1 = expression1
        self.expression2 = expression2


class WhileLoop(Node):
    def __init__(self, condition, expression):
        self.condition = condition
        self.expression = expression


class ForLoop(Node):
    def __init__(self, range, step, expression):
        self.range = range
        self.step = step
        self.expression = expression


class Range(Node):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class String(Node):
    def __init__(self, name):
        self.name = name


class UNegation(Node):
    def __init__(self, value):
        self.value = value


class Transposition(Node):
    def __init__(self, value):
        self.value = value


class Break(Node):
    def __init__(self):
        pass


class Continue(Node):
    def __init__(self):
        pass


class Return(Node):
    def __init__(self):
        pass


class ReturnValue(Node):
    def __init__(self, value):
        self.value = value


class Print(Node):
    def __init__(self, name):
        self.name = name


class Arguments(Node):
    def __init__(self, value):
        self.value = value


class Array(Node):
    def __init__(self, size=None):
        self.size = size


class Error(Node):
    def __init__(self):
        pass


class OperationNode(object):
    pass


class AssignInArrayExpr(object):
    def __init__(self, operator, ID, array_range, value):
        self.operator = operator
        self.ID = ID
        self.array_range = array_range
        self.value = value


class MatrixInitialization(Node):
    def __init__(self, mode, value):
        self.mode = mode
        self.value = value


class Dimensions(object):
    def __init__(self, value): #, dimensions=None):
        self.value = value
        # self.dimensions = dimensions
