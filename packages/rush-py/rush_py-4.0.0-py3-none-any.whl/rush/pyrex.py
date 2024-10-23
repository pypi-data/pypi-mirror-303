#!/usr/bin/env python3

# pyrex is a python library for constructing rex expressions


from typing import Any, Literal
from dataclasses import dataclass

from rush.typedef import RushType


type ExprKinds = Literal["Fun", "Val", "Exprs", "Lambda"]


@dataclass
class JsonVal:
    Json: Any


@dataclass
class Val:
    Val: JsonVal


@dataclass
class Named:
    name: str


@dataclass
class Var:
    Var: Named


@dataclass
class Fun:
    Fun: Named


@dataclass
class Lambda:
    exprs: list[JsonVal | Fun | Val | Var | "Lambda" | "Exprs"]
    vars: list[str]


@dataclass
class Exprs:
    Exprs: list[JsonVal | Fun | Lambda | Val | Var | "Exprs"]


Expr = JsonVal | Fun | Lambda | Var | Exprs | Val


def isExpr(v: Any):
    return isinstance(v, (Exprs, Lambda, Fun, Var, JsonVal))


def wrapVal(v: Any) -> Expr:
    if isExpr(v):
        return v
    return Val(JsonVal(v))


def mk_fun(name: str, args: list[RushType[Any] | str] = []):
    def fun(*args: Any):
        return Exprs([Fun(Named(name))] + [wrapVal(arg) for arg in args])

    return fun


add = mk_fun("add", ["u8", "u8"])
sub = mk_fun("sub", ["u8", "u8"])

sub(add(1, 2), 2)
