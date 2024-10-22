# Copyright 2019-2023 Ingmar Dasseville, Pierre Carbonnelle
#
# This file is part of IDP-Z3.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from idp_engine.Expression import *
# from idp_engine.Expression import (ASTNode, Expression, AQuantification,
#                                    AConjunction, Brackets, AImplication,
#                                    AEquivalence, AppliedSymbol, AUnary,
#                                    AAggregate)


### class ASTNode


def SCA_Check(self, detections):
    return


ASTNode.SCA_Check = SCA_Check


## class Expression


def SCA_Check(self, detections):
    for sub in self.sub_exprs:
        sub.SCA_Check(detections)


Expression.SCA_Check = SCA_Check


## class AQuantification


def SCA_Check(self, detections):
    vars = set()
    # First, get all variables in quantification. (E.g. 'x' for !x in Type)
    for q in self.quantees:
        for q2 in q.vars:
            vars.add(q2[0].str)
    if self.f.variables != vars and self.f.variables is not None:
        # Detect unused variables.
        set3 = vars - set(self.f.variables)
        while len(set3) > 0:
            # Search all unused variables.
            a = set3.pop()
            for q in self.quantees:
                for q2 in q.vars:
                    if q2[0].str == a:
                        detections.append(
                            (q2[0], f"Unused variable {q2[0].str}.", "Warning")
                        )
                        break

    if self.q == "∀":
        # Check for a common mistake.
        if (
            isinstance(self.f, AConjunction)
            or isinstance(self.f, Brackets)
            and isinstance(self.f.f, AConjunction)
        ):
            detections.append(
                (
                    self.f,
                    "Common mistake, you likely want to use an implication (⇒)"
                    " after universal quantor (∀) instead of conjunction (∧)."
                    "Warning",
                )
            )
    if self.q == "∃":
        # Check for a common mistake.
        if (
            isinstance(self.f, AImplication)
            or isinstance(self.f, Brackets)
            and isinstance(self.f.f, AImplication)
        ):
            detections.append(
                (
                    self.f,
                    "Common mistake, you likely want to use use a conjuction"
                    " (∧) after existential quantor (∃) instead of an"
                    " implication (⇒).",
                    "Warning",
                )
            )
    if isinstance(self.f, AEquivalence):
        # Check for variables only occurring on one side of an equivalence.
        links = self.f.sub_exprs[0]
        rechts = self.f.sub_exprs[1]
        if len(links.variables) < len(
            vars
        ):  # check if all vars in left part van AEquivalence
            set3 = vars - links.variables
            detections.append(
                (
                    self.f,
                    f"Common mistake, variable {set3.pop()} only occurs on one"
                    " side of equivalence.",
                    "Warning",
                )
            )
        elif len(rechts.variables) < len(
            vars
        ):  # check if all vars in right part van AEquivalence
            set3 = vars - links.variables
            detections.append(
                (
                    self.f,
                    f"Common mistake, variable {set3.pop()} only occurs on one"
                    " side of equivalence.",
                    "Warning",
                )
            )

    Expression.SCA_Check(self, detections)


AQuantification.SCA_Check = SCA_Check


# class AUnary(Expression):


def SCA_Check(self, detections):
    # style rule: use brackets when negating an in-statement
    if isinstance(self.f, AppliedSymbol) and self.f.is_enumeration == "in":
        if hasattr(self, "parent"):
            detections.append(
                (
                    self,
                    "Style: place brackets around negated in-statement.",
                    "Warning",
                )
            )

    Expression.SCA_Check(self, detections)


AUnary.SCA_Check = SCA_Check


## class AAggregate(Expression):


def SCA_Check(self, detections):
    assert self.aggtype in [
        "sum",
        "#",
    ], "Internal error"  # min aggregates are changed by Annotate !
    if self.lambda_ == "lambda":
        detections.append(
            (self, f"Please use the new syntax for aggregates", "Warning")
        )
    Expression.SCA_Check(self, detections)


AAggregate.SCA_Check = SCA_Check

## class Brackets(Expression):


def SCA_Check(self, detections):
    # style rule: prevent unneeded brackets
    if isinstance(self.f, Brackets):
        detections.append((self, "Style: redundant brackets", "Warning"))
    return Expression.SCA_Check(self, detections)


Brackets.SCA_Check = SCA_Check
