from __future__ import print_function
import AST


def addToClass(cls):
    def decorator(func):
        setattr(cls, func.__name__, func)
        return func

    return decorator


class TreePrinter:

    @addToClass(AST.Node)
    def printTree(self, indent=0):
        raise Exception("printTree not defined in class " + self.__class__.__name__)

    @addToClass(AST.IntNum)
    def printTree(self, indent=0):
        print("|  " + self.value)
        pass
        # fill in the body

    @addToClass(AST.FloatNum)
    def printTree(self, indent=0):
        pass
        # fill in the body

    @addToClass(AST.Variable)
    def printTree(self, indent=0):
        pass
        # fill in the body

    @addToClass(AST.BinExpr)
    def printTree(self, indent=0):
        pass
        # fill in the body

    @addToClass(AST.RelExpr)
    def printTree(self, indent=0):
        pass

    @addToClass(AST.AssignExpr)
    def printTree(self, indent=0):
        print(self.operator)
        print("|  " + self.left)
        print("|  " + self.right)

    @addToClass(AST.IfExpr)
    def printTree(self, indent=0):
        pass

    @addToClass(AST.WhileLoop)
    def printTree(self, indent=0):
        pass

    @addToClass(AST.ForLoop)
    def printTree(self, indent=0):
        pass

    @addToClass(AST.String)
    def printTree(self, indent=0):
        pass

    @addToClass(AST.Error)
    def printTree(self, indent=0):
        pass
        # fill in the body

