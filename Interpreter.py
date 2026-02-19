"""

definition: Interpreter - Represent a small language / grammer as objects
and interpret (evaluate) it against a context

good for - 

tiny DSLs (filters, rules, math expressions)
config rules / query conditions
Bad for: big languages (you'll reinvent a compiler)

"""


from __future__ import annotations
from dataclasses import dataclass
from typing import Dict


class Expr:
    def interpret(self, ctx: Dict[str, bool]) -> bool:
        raise NotImplementedError


@dataclass(frozen=True)
class Var(Expr):
    name: str
    def interpret(self, ctx: Dict[str, bool]) -> bool:
        return ctx[self.name]


@dataclass(frozen=True)
class And(Expr):
    a: Expr; b: Expr
    def interpret(self, ctx: Dict[str, bool]) -> bool:
        return self.a.interpret(ctx) and self.b.interpret(ctx)


@dataclass(frozen=True)
class Or(Expr):
    a: Expr; b: Expr
    def interpret(self, ctx: Dict[str, bool]) -> bool:
        return self.a.interpret(ctx) or self.b.interpret(ctx)


@dataclass(frozen=True)
class Not(Expr):
    x: Expr
    def interpret(self, ctx: Dict[str, bool]) -> bool:
        return not self.x.interpret(ctx)


if __name__ == "__main__":
    # rule: (is_admin OR is_owner) AND NOT is_banned
    rule = And(Or(Var("is_admin"), Var("is_owner")), Not(Var("is_banned")))

    print(rule.interpret({"is_admin": False, "is_owner": True, "is_banned": False}))  # True
    print(rule.interpret({"is_admin": False, "is_owner": True, "is_banned": True}))   # False







# arithematic DSL with variables


# from __future__ import annotations
# from dataclasses import dataclass
# from typing import Dict, List, Optional


# class Expr:
#     def interpret(self, ctx: Dict[str, float]) -> float:
#         raise NotImplementedError




# @dataclass(frozen=True)
# class Number(Expr):
#     value: float

#     def interpret(self, ctx: Dict[str, float]) -> float:
#         return self.value

    

# @dataclass(frozen=True)
# class Variable(Expr):
#     name: str

#     def interpret(self, ctx: Dict[str, float]) -> float:
#         if self.name not in ctx:
#             raise KeyError(f"Undefined variable: {self.name}")
#         return float(ctx[self.name])


# @dataclass(frozen=True)
# class Add(Expr):
#     left: Expr
#     right: Expr

#     def interpret(self, ctx: Dict[str, float]) -> float:
#         return self.left.interpret(ctx) + self.right.interpret(ctx)


# @dataclass(frozen=True)
# class Sub(Expr):
#     left: Expr
#     right: Expr

#     def interpret(self, ctx: Dict[str, float]) -> float:
#         return self.left.interpret(ctx) - self.right.interpret(ctx)


# @dataclass(frozen=True)
# class Mul(Expr):
#     left: Expr
#     right: Expr

#     def interpret(self, ctx: Dict[str, float]) -> float:
#         return self.left.interpret(ctx) * self.right.interpret(ctx)


# @dataclass(frozen=True)
# class Div(Expr):
#     left: Expr
#     right: Expr

#     def interpret(self, ctx: Dict[str, float]) -> float:
#         denom = self.right.interpret(ctx)
#         if denom == 0:
#             raise ZeroDivisionError("division by zero")
#         return self.left.interpret(ctx) / denom



# # --------- Tiny parser (recursive descent) ---------
# def tokenize(s: str) -> List[str]:
#     tokens: List[str] = []
#     i = 0
#     while i < len(s):
#         c = s[i]
#         if c.isspace():
#             i += 1
#         elif c in "+-*/()":
#             tokens.append(c)
#             i += 1
#         elif c.isdigit() or c == ".":
#             j = i
#             while j < len(s) and (s[j].isdigit() or s[j] == "."):
#                 j += 1
#             tokens.append(s[i:j])
#             i = j
#         elif c.isalpha() or c == "_":
#             j = i
#             while j < len(s) and (s[j].isalnum() or s[j] == "_"):
#                 j += 1
#             tokens.append(s[i:j])
#             i = j
#         else:
#             raise ValueError(f"Bad character: {c!r}")
#     return tokens



# class Parser:
#     def __init__(self, tokens: List[str]) -> None:
#         self.toks = tokens
#         self.pos = 0

#     def peek(self) -> Optional[str]:
#         return self.toks[self.pos] if self.pos < len(self.toks) else None

#     def eat(self, expected: str) -> None:
#         if self.peek() != expected:
#             raise ValueError(f"Expected {expected}, got {self.peek()}")
#         self.pos += 1

#     # expr := term (('+'|'-') term)*
#     def parse_expr(self) -> Expr:
#         node = self.parse_term()
#         while self.peek() in ("+", "-"):
#             op = self.peek()
#             self.pos += 1
#             rhs = self.parse_term()
#             node = Add(node, rhs) if op == "+" else Sub(node, rhs)
#         return node

#     # term := factor (('*'|'/') factor)*
#     def parse_term(self) -> Expr:
#         node = self.parse_factor()
#         while self.peek() in ("*", "/"):
#             op = self.peek()
#             self.pos += 1
#             rhs = self.parse_factor()
#             node = Mul(node, rhs) if op == "*" else Div(node, rhs)
#         return node

#     # factor := NUMBER | IDENT | '(' expr ')' | '-' factor
#     def parse_factor(self) -> Expr:
#         tok = self.peek()
#         if tok is None:
#             raise ValueError("Unexpected end")

#         if tok == "(":
#             self.eat("(")
#             node = self.parse_expr()
#             self.eat(")")
#             return node

#         if tok == "-":  # unary minus
#             self.eat("-")
#             return Sub(Number(0), self.parse_factor())

#         self.pos += 1
#         if tok.replace(".", "", 1).isdigit():
#             return Number(float(tok))
#         return Variable(tok)


# def parse(s: str) -> Expr:
#     p = Parser(tokenize(s))
#     ast = p.parse_expr()
#     if p.peek() is not None:
#         raise ValueError(f"Unexpected token: {p.peek()}")
#     return ast


# if __name__ == "__main__":
#     expr = parse("(x + 3) * (y - 2)")
#     print(expr.interpret({"x": 5, "y": 10}))  # -> 64.0