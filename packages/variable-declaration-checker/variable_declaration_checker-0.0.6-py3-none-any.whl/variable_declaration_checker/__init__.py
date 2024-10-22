import astroid as _astroid
from pylint.checkers import BaseChecker as _BaseChecker
from pylint.lint import PyLinter as _PyLinter


class VariableDeclarationChecker(_BaseChecker):
    name = "variable-declaration-checker"
    msgs = {
        "W5901": ("Declare the variable with type annotation.",
                  "un-declared-variable",
                  "It's the first time the variable appears, so here should be a type annotation."),
        "W5902": ("Remove the type annotation, or rename the variable.",
                  "re-declared-variable",
                  "The variable has been used before, so here shouldn't be a type annotation."),
    }

    def _check(self, node: _astroid.nodes.LocalsDictNodeNG):
        # locals 中会包含 nonlocal 的变量：
        # https://github.com/pylint-dev/astroid/issues/2616
        non_locals = {
            name
            for node in node.nodes_of_class(_astroid.nodes.Nonlocal,
                                            _astroid.nodes.FunctionDef)
            for name in node.names
        }
        for name, occurrences in node.locals.items():
            if name == "_":
                continue

            occurrence_iterator = iter(occurrences)
            if name not in non_locals:
                occurrence = next(occurrence_iterator)
                if (
                        isinstance(occurrence, _astroid.nodes.AssignName) and
                        (not isinstance(occurrence.parent, _astroid.nodes.AnnAssign)) and
                        (not isinstance(occurrence.parent, _astroid.nodes.Arguments)) and
                        (not isinstance(occurrence.parent, _astroid.nodes.TypeAlias))
                ):
                    self.add_message("un-declared-variable", node=occurrence)

            for occurrence in occurrence_iterator:
                if (
                        isinstance(occurrence.parent, _astroid.AnnAssign)
                ):
                    self.add_message("re-declared-variable", node=occurrence)

    def visit_functiondef(self, node: _astroid.FunctionDef):
        self._check(node)

    def visit_module(self, node: _astroid.Module):
        self._check(node)

    def visit_classdef(self, node: _astroid.ClassDef):
        self._check(node)


def register(linter: _PyLinter) -> None:
    linter.register_checker(VariableDeclarationChecker(linter))
