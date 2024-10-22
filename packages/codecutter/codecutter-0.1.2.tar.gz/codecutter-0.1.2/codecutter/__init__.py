import ast
import inspect
from importlib import invalidate_caches
from importlib.abc import SourceLoader
from importlib.util import module_from_spec
from importlib.machinery import ModuleSpec
from typing import Callable
from codecutter.modifiers import (
    remove_all_decorators,
    replace_variables,
    replace_shortcircuit_constants,
    replace_constant_ifs,
)


# ------------------------ MODULE LOADING FROM STRING ------------------------ #


class StringLoader(SourceLoader):
    def __init__(self, source):
        self.source = source

    def get_source(self, fullname):
        return self.source

    def get_filename(self, fullname):
        return f"<StringLoader>"

    def get_data(self, path):  # noqa
        return self.source


def import_from_string(data, variables={}):
    invalidate_caches()

    loader = StringLoader(data)
    spec = ModuleSpec("<StringLoader>", loader)
    module = module_from_spec(spec)

    # Update "variables" that are needed on module execution time, such as
    # decorator functions
    module.__dict__.update(variables)

    if spec.loader is None:
        raise Exception("Failed to load loader to the spec")

    spec.loader.exec_module(module)

    return module


# ------------------------- PREPROCESSING DECORATORS ------------------------- #


def preprocess_with_functions(
    preprocess_functions, variables={}, log_source=False
):
    def wrapped(function):
        # Load code and remove indentation
        source = inspect.getsource(function)
        source_lines = source.splitlines()
        source_first_line = source_lines[0]
        source_indentation = len(source_first_line) - len(
            source_first_line.lstrip()
        )
        source = "\n".join(
            [line[source_indentation:] for line in source_lines]
        )
        module_tree = ast.parse(source)
        function_tree: ast.FunctionDef = module_tree.body[0]  # type: ignore

        # Remove all decorators because otherwise they get applied twice
        remove_all_decorators(function_tree)

        # Manupulate code with preprocess functions until no changes were made
        # by any preprocess function
        changes = True
        while changes:
            changes = False
            for preprocess_function in preprocess_functions:
                changes = changes or preprocess_function(function_tree)

        # Load manipulated code
        new_source = ast.unparse(function_tree)
        if log_source == True:
            print("-------------------------------")
            print("SOURCE CODE AFTER PREPROCESSING")
            print("-------------------------------")
            print(new_source)
            print("-------------------------------")
        elif isinstance(log_source, Callable):
            log_source(new_source)

        tmp_module = import_from_string(new_source, variables=variables)
        new_function = getattr(tmp_module, function_tree.name)

        return new_function

    return wrapped


def preprocess(constants={}, variables={}, log_source=False, additional_preprocessors=[]):
    return preprocess_with_functions(
        [
            replace_variables(constants),
            replace_shortcircuit_constants,
            replace_constant_ifs,
            *additional_preprocessors,
        ],
        variables=variables,
        log_source=log_source,
    )
