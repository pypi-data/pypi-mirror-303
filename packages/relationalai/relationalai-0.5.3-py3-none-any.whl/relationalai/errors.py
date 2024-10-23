from __future__ import annotations
import sys
from types import TracebackType
import ast
import io
import re
import textwrap
from typing import Any, List, Tuple
import warnings
from .metamodel import Action, Task
from rich.console import Console
from rich.text import Text
from rich.table import Table
from rich import box
from enum import Enum
from . import debugging

#--------------------------------------------------
# Print helpers
#--------------------------------------------------

def rich_str(item:Any, style:str|None = None) -> str:
    output = io.StringIO()
    console = Console(file=output, force_terminal=True)
    console.print(item, style=style)
    return output.getvalue()

def body_text(console, body:str):
    body = textwrap.dedent(body)
    for line in body.splitlines():
        if not line.startswith("  "):
            console.print(line)
        else:
            console.print(line, soft_wrap=True)

def mark_source(source: debugging.SourceInfo|None, start_line:int|None=None, end_line:int|None=None, indent=8, highlight="yellow", highlight_lines = []):
    if source is None:
        return ""

    final_lines = []
    all_lines = source.source.splitlines()
    source_start = source.source_start_line or source.line or start_line or 0
    start_line = start_line if start_line is not None else source.line
    max_line = source.line + len(all_lines)
    end_line = end_line if end_line is not None else max_line
    line_number_len = len(str(max_line))
    for ix, line in enumerate(source.source.splitlines()):
        cur = line
        cur_indent = indent if ix > 0 else 0
        line_number = source_start + ix
        color = "dim white"
        if (line_number >= start_line and line_number <= end_line) or line_number in highlight_lines:
            color = highlight + " bold"
        cur = f"{' '*cur_indent}[{color}]  {line_number :>{line_number_len}} |  {cur}[/{color}]"
        final_lines.append(cur)
    return "\n".join(final_lines)

def print_source_error(source, name:str, content:str, color="red"):
    fixed_content_length = len(name) + len(source.file) + len(str(source.line)) + 2  # 2 for the spaces around the dash
    num_dashes = 74 - fixed_content_length
    dashes = '-' * num_dashes
    console = Console(width=80, force_jupyter=False, stderr=True)
    console.print("\n")
    console.print(f"[{color}]--- {name} {dashes} {source.file}: {source.line}")
    console.print()
    body_text(console, content)
    console.print()
    console.print(f'[{color}]{"-" * 80}')
    console.print()

def print_error(name:str, content:str, color="red"):
    fixed_content_length = len(name) + 2  # 2 for the spaces around the dash
    num_dashes = 76 - fixed_content_length
    dashes = '-' * num_dashes
    console = Console(width=80, force_jupyter=False, stderr=True)
    console.print("\n")
    console.print(f"[{color}]--- {name} {dashes}")
    console.print()
    body_text(console, content)
    console.print()
    console.print(f'[{color}]{"-" * 80}')
    console.print()

def print_error_name(name:str, color="red"):
    console = Console(width=80, force_jupyter=False, stderr=True)
    console.print("\n")
    console.print(f'[{color}]{"-" * 80}')
    console.print()
    body_text(console, name)
    console.print()
    console.print(f'[{color}]{"-" * 80}')
    console.print()

#--------------------------------------------------
# Transformers
#--------------------------------------------------

class IfToWithTransformer(ast.NodeTransformer):
    def visit_If(self, node):
        with_node = ast.With(
            items=[ast.withitem(context_expr=node.test, optional_vars=None)],
            body=node.body,
            lineno=node.lineno,
            type_comment=None)
        return with_node

class WithDynamic(ast.NodeTransformer):
    def visit_With(self, node):
        content = ast.unparse(node.items[0].context_expr).replace(")", "dynamic=True)")
        with_node = ast.With(
            items=[ast.withitem(context_expr=ast.Name(id=content), optional_vars=node.items[0].optional_vars)],
            body=[],
            lineno=node.lineno,
            type_comment=None)
        return with_node

class SetToMethod(ast.NodeTransformer):
    def visit_Assign(self, node):
        if isinstance(node.targets[0], ast.Attribute):
            keyword = ast.keyword(arg=node.targets[0].attr, value=node.value)
            return ast.Expr(value=ast.Call(
                func=ast.Attribute(value=node.targets[0].value, attr="set", ctx=ast.Load()),
                args=[],
                keywords=[keyword],
                lineno=node.lineno
            ))
        return node

class AssignToCompare(ast.NodeTransformer):
    def visit_Assign(self, node):
        if isinstance(node.targets[0], ast.Attribute) and len(node.targets) == 1:
            compare_node = ast.Compare(
                left=node.targets[0],
                ops=[ast.Eq()],
                comparators=[node.value]
            )
            expr_node = ast.Expr(value=compare_node)
            ast.copy_location(expr_node, node)

            return expr_node
        return node

class PropertyNameReplacer(ast.NodeTransformer):
    def __init__(self, old_name, new_name):
        self.old_name = old_name
        self.new_name = new_name

    def visit_Attribute(self, node):
        # Check if the attribute name matches the old name
        if isinstance(node.attr, str) and node.attr == self.old_name:
            # Replace the attribute name with the new name
            node.attr = self.new_name
        return node

    def visit_Name(self, node):
        # Check if the variable name matches the old name
        if isinstance(node.id, str) and node.id == self.old_name:
            # Replace the variable name with the new name
            node.id = self.new_name
        return node

#--------------------------------------------------
# Finders
#--------------------------------------------------

class PropertyFinder(ast.NodeVisitor):
    def __init__(self, start_line, properties):
        self.errors = []
        self.start_line = start_line
        self.properties = properties
        self.found_properties_lines = []  # To store lines where properties are found
        self.dynamic_properties = []  # To store dynamic properties

    def to_line_numbers(self, node):
        return (node.lineno, node.end_lineno)

    def visit_Attribute(self, node):
        if node.attr in self.properties:
            line_numbers = self.to_line_numbers(node)
            if line_numbers[0] >= self.start_line:
                self.found_properties_lines.append(node.lineno)
        self.generic_visit(node)

    def visit_Call(self, node):
        # Check if this is a call to 'getattr'
        if (isinstance(node.func, ast.Name) and node.func.id == 'getattr' and
                len(node.args) >= 2):
            if isinstance(node.args[1], ast.Str):
                property_name = node.args[1].s
                if property_name in self.properties:
                    line_numbers = self.to_line_numbers(node)
                    if line_numbers[0] >= self.start_line:
                        self.found_properties_lines.append(node.lineno)
            else:
                line_numbers = self.to_line_numbers(node)
                if line_numbers[0] >= self.start_line:
                    self.dynamic_properties.append(node.lineno)
        self.generic_visit(node)

#--------------------------------------------------
# Metaclass
#--------------------------------------------------

class RAIPostInitMeta(type):
    def __call__(cls, *args, **kwargs):
        instance = super().__call__(*args, **kwargs)
        instance.__post_init__()
        return instance

# --------------------------------------------------
# RAIException
# --------------------------------------------------

class RAIException(Exception, metaclass=RAIPostInitMeta):
    def __init__(self, message, name=None, content=None, source=None, **kwargs):
        super().__init__(message)
        self.name = name
        self.message = message
        self.content = content
        self.source = source

        # Store any additional keyword arguments as attributes
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        return self.message

    def __post_init__(self):
        self.raw_content = self.strip_rich_tags()

    def pprint(self):
        if self.source and self.content:
            print_source_error(self.source, self.name or self.message, self.content.strip())
        elif self.content:
            print_error(self.name or self.message, self.content.strip())
        else:
            print_error_name(self.name or self.message)

    def __eq__(self, other):
        if isinstance(other, RAIException):
            return self.message == other.message and self.__dict__ == other.__dict__
        return False

    def strip_rich_tags(self):
        if self.content:
            # Use Text.from_markup to remove rich tags
            plain_text = Text.from_markup(self.content).plain
            # Split the content into lines
            lines = plain_text.split('\n')
            # Remove leading empty lines or lines with only whitespace
            while lines and not lines[0].strip():
                lines.pop(0)
            # Strip leading whitespace from the first non-empty line
            if lines:
                lines[0] = lines[0].lstrip()
            # Join the lines back together
            cleaned_content = '\n'.join(lines)
            return cleaned_content
        else:
            return self.message

    def clone(self):
        try:
            raise AssertionError
        except AssertionError:
            traceback = sys.exc_info()[2]
            back_frame = traceback.tb_frame.f_back if traceback else None

            if back_frame is None:
                return self.with_traceback(traceback)

        back_tb = TracebackType(tb_next=None,
                                    tb_frame=back_frame,
                                    tb_lasti=back_frame.f_lasti,
                                    tb_lineno=back_frame.f_lineno)
        return self.with_traceback(back_tb)

class ModelError(RAIException):
    error_locations = {}

    def __init__(self, problems):
        super().__init__("Error object added")
        problem = problems[0]
        self.problems = problems
        self.source = ModelError.error_locations.get(problem["props"]["pyrel_id"], debugging.SourceInfo())
        self.message = problem["message"]
        self.name = "Model error"
        self.content = self.format_message()

    def get_formatted_props_string(self):
        # Create a table
        table = Table(show_header=True, box=box.ROUNDED, padding=(0, 1))
        ks = list([k for k in self.problems[0]["props"].keys() if not k.startswith("pyrel_")])
        for k in ks:
            table.add_column(k)

        for problem in self.problems:
            row = []
            for k in ks:
                row.append(str(problem["props"].get(k, "")))
            table.add_row(*row)

        with io.StringIO() as string_io:
            console = Console(file=string_io)
            console.print(table)
            table_string = string_io.getvalue()

        return table_string

    def format_message(self):
        row_str = self.get_formatted_props_string()

        marked = mark_source(self.source, self.source.line, self.source.line, indent=2) if self.source else ""
        return "\n\n".join([self.message, "  " + marked, row_str])


class RelQueryError(RAIException):
    def __init__(self, problem, source: debugging.SourceInfo|None = None):
        super().__init__("Rel query error")
        self.problem = problem
        self.source = source
        self.message = "Query error"
        self.name = "Query error"
        self.content = self.format_message()

    def format_message(self):
        problem = self.problem
        marked = mark_source(self.source, -1, -1) if self.source else ""
        return textwrap.dedent(f"""
        {problem["report"]}
        {problem["message"]}

        {marked}
        """)

class RAIExceptionSet(RAIException):
    def __init__(self, exceptions: List[RAIException]):
        super().__init__("Multiple Errors, see above")
        self.exceptions = exceptions

    def pprint(self):
        for exception in self.exceptions:
            exception.pprint()

    def clone(self):
        return RAIExceptionSet([exception.clone() for exception in self.exceptions])

# --------------------------------------------------
# Warning
# --------------------------------------------------

class RAIWarning(Warning, metaclass=RAIPostInitMeta):
    name = ""
    message: str|None = None
    content = None
    source = None

    def __init__(self, message="", name=None, content=None, source=None):
        self.name = name
        self.message = message
        self.content = content
        self.source = source

    def pprint(self):
        msg = self.name or self.message or ""
        if self.source and self.content:
            print_source_error(self.source, msg, self.content.strip(), color="yellow")
        elif self.content:
            print_error(msg, self.content.strip(), color="yellow")
        else:
            print_error_name(msg, color="yellow")

    def __post_init__(self):
        self.raw_content = self.strip_rich_tags()
        debugging.warn(self)
        warnings.warn(self)

    def strip_rich_tags(self):
        if self.content:
            # Use Text.from_markup to remove rich tags
            plain_text = Text.from_markup(self.content).plain
            # Split the content into lines
            lines = plain_text.split('\n')
            # Remove leading empty lines or lines with only whitespace
            while lines and not lines[0].strip():
                lines.pop(0)
            # Strip leading whitespace from the first non-empty line
            if lines:
                lines[0] = lines[0].lstrip()
            # Join the lines back together
            cleaned_content = '\n'.join(lines)

            return cleaned_content
        else:
            return self.name

    def __str__(self):
        return f"{self.name}: {self.raw_content}"

class RelQueryWarning(RAIWarning):
    def __init__(self, problem, source):
        super().__init__("Query warning")
        self.name = "Query warning"
        self.problem = problem
        self.source = source
        self.message = "Query warning"
        self.content = self.format_message()

    def format_message(self):
        problem = self.problem
        marked = mark_source(self.source, -1, -1)
        return textwrap.dedent(f"""
        {problem["report"]}
        {problem["message"]}

        {marked}
        """)

class IntegrityConstraintViolation(RAIException):
    def __init__(self, violation, source=None):
        self.violation = violation
        self.source = source

        body = violation["message"]
        self.name = "Integrity constraint violation"
        self.message = "Integrity constraint violation"
        self.content = self.format_message(body)
        super().__init__(self.message, self.name, self.content, self.source)

    def format_message(self, body):
        marked = mark_source(self.source, -1, -1)

        f"Integrity constraint violation\n{body}"

        return textwrap.dedent(f"""
        {body}

        {marked}
        """)

    def clone(self):
        return IntegrityConstraintViolation(self.violation, self.source)

class ModelWarning(RAIWarning):
    error_locations = {}

    def __init__(self, problems):
        super().__init__("Error object added")
        problem = problems[0]
        self.problems = problems
        self.source = ModelError.error_locations.get(problem["props"]["pyrel_id"], debugging.SourceInfo())
        self.message = problem["message"]
        self.name = "Model warning"
        self.content = self.format_message()

    def get_formatted_props_string(self):
        # Create a table
        table = Table(show_header=True, box=box.ROUNDED, padding=(0, 1))
        ks = list([k for k in self.problems[0]["props"].keys() if not k.startswith("pyrel_")])
        for k in ks:
            table.add_column(k)

        for problem in self.problems:
            row = []
            for k in ks:
                row.append(problem["props"].get(k, ""))
            table.add_row(*row)

        with io.StringIO() as string_io:
            console = Console(file=string_io)
            console.print(table)
            table_string = string_io.getvalue()

        return table_string

    def format_message(self):
        row_str = self.get_formatted_props_string()

        marked = mark_source(self.source, self.source.line, self.source.line, indent=2) if self.source else ""
        return "\n\n".join([self.message or "", "  " + marked, row_str])


# --------------------------------------------------
# Rel Exceptions/warnings
# --------------------------------------------------

class NumericOverflow(RAIException):
    def __init__(self, problem, source):
        super().__init__("Numeric Overflow")
        self.problem = problem
        self.source = source
        self.message = "Numeric Overflow"
        self.name = "Numeric Overflow"
        self.content = self.format_message()

    def format_message(self):
        problem = self.problem
        marked = mark_source(self.source, -1, -1)
        info = problem["report"].split("\n--------------")[0].strip()
        return textwrap.dedent(f"""
        {info}

        {marked}
        """)

class ArityMismatch(RAIWarning):
    def __init__(self, problem, source):
        self.name = "Arity mismatch"
        self.message = problem["message"]
        self.source = source
        self.content = self.format_message()

    def format_message(self):
        source = self.source
        match = re.search(r"`(.+?)` expects (.*)", self.message or "")
        if match is None:
            return self.message
        fq_name = match.group(1)
        rel_name = fq_name.split("::")[-1]
        arity_sentence = match.group(2)
        found = PropertyFinder(source.line, [rel_name])
        if source.block:
            found.visit(source.block)
        found_lines = found.found_properties_lines or found.dynamic_properties
        marked = mark_source(self.source, -1, -1, highlight_lines=found_lines)
        return textwrap.dedent(f"""
        The relation [yellow]{rel_name}[/yellow] expects {arity_sentence}

        {marked}
        """)

class UninitializedPropertyException(RAIException):
    def __init__(self, undefineds: List[Tuple[str, Any]]):
        self.content = ""
        self.raw_content = ""
        self.source = None
        self.name = "Uninitialized property"
        self.message = "Uninitialized property"

        # group by source
        source_map: dict[str, tuple[debugging.SourceInfo, list[str]]] = {}
        for name, source in undefineds:
            if source.source not in source_map:
                source_map[source.source] = (source, [name])
            else:
                source_map[source.source][1].append(name)

        chunks: list[str] = []
        for (source, names) in source_map.values():
            self.source = source

            unique_names = list(set(names))
            props = ", ".join([f"[yellow]{name}[/yellow]" for name in unique_names])
            prop_line = (
                f"property {props} has"
                if len(unique_names) == 1
                else f"properties {props} have"
            )
            found = PropertyFinder(source.line, unique_names)
            if source.block:
                found.visit(source.block)
            found_lines = found.found_properties_lines or found.dynamic_properties
            marked = mark_source(source, -1, -1, indent=12, highlight_lines=found_lines)
            chunks.append(textwrap.dedent(f"""
            The {prop_line} never been set or added to and so will always cause the rule or query to fail.

            {marked}
            """))

            self.content = "\n\n".join(chunks)

        super().__init__(self.name, self.message, self.content, self.source)


class RAITypeError(RAIException, TypeError):
    def __init__(self, param: str, message: str):
        self.param = param
        self.message = message
        self.name = "Invalid type error"
        self.source = Errors.call_source(4)

        # Mark the source if available
        if self.source:
            self.marked = mark_source(self.source, self.source.line, self.source.line)
        else:
            self.marked = ""

        # Format the content and raw_content
        self.content = self.format_message()
        self.raw_content = self.strip_rich_tags()

        super().__init__(self.message, self.name, self.content, self.source)

    def format_message(self):
        if self.source:
            return textwrap.dedent(f"""
            The parameter [yellow]{self.param}[/yellow] is of the wrong type.

            {self.marked}
            """)
        else:
            return textwrap.dedent(f"""
            The parameter [yellow]{self.param}[/yellow] is of the wrong type.
            """)

class RAIValueError(RAIException, ValueError):
    def __init__(self, message: str):
        self.message = message
        self.name = "Invalid value error"
        self.source = Errors.call_source(4)

        # Mark the source if available
        if self.source:
            self.marked = mark_source(self.source, self.source.line, self.source.line)
        else:
            self.marked = ""

        # Format the content and raw_content
        self.content = self.format_message()
        self.raw_content = self.strip_rich_tags()

        super().__init__(self.message, self.name, self.content, self.source)

    def format_message(self):
        if self.source:
            return textwrap.dedent(f"""
            {self.message}

            {self.marked}
            """)
        else:
            return textwrap.dedent(f"""
            {self.message}
            """)


# --------------------------------------------------
# DSL scope errors
# --------------------------------------------------
class OutOfContextException(RAIException):
    def __init__(self, source=None):
        self.name = "Outside of context"
        self.message = (
            "Looks like this object is being used outside of a rule or query."
        )
        self.source = source or Errors.call_source() or debugging.SourceInfo()
        self.content = self.format_message()

        super().__init__(self.message, self.name, self.content, source=source)

    def format_message(self):
        marked = mark_source(self.source, self.source.line, self.source.line)
        return textwrap.dedent(f"""
        Looks like this [yellow]object[/yellow] is being used outside of a rule or query.

        {marked}
        """)


class VariableOutOfContextException(RAIException):
    def __init__(self, source, name: str|None, is_property=False):
        self.name = "Variable out of context"
        if name is None:
            self.message = "Looks like a variable is being used outside of the rule or query it was defined in."
        else:
            self.message = f"Looks like a variable representing '{name}' is being used outside of the rule or query it was defined in."
        self.source = source
        self.is_property = is_property
        self.content = self.format_message(name)

        super().__init__(self.message, self.name, self.content, source=source)

    def format_message(self, name):
        marked = mark_source(self.source, self.source.line, self.source.line)
        return textwrap.dedent(f"""
        Looks like a variable representing [yellow bold]{name}[/yellow bold] is being used outside of the rule or query it was defined in.

        {marked}
        """)

class SelectOutOfContext(RAIException):
    def __init__(self):
        self.name = "Outside of context"
        self.message = (
            "Looks like this select is being used outside of the query it was originally from."
        )
        self.source = Errors.call_source() or debugging.SourceInfo()
        self.content = self.format_message()

        super().__init__(self.message, self.name, self.content, source=self.source)

    def format_message(self):
        marked = mark_source(self.source, self.source.line, self.source.line)
        return textwrap.dedent(f"""
        Looks like this [yellow]select[/yellow] is being used outside of the query it is from.

        {marked}
        """)

#--------------------------------------------------
# DSL Type errors
#--------------------------------------------------

class FilterAsValue(RAIException):
    def __init__(self, source=None):
        self.name = "Filter used as a value"
        self.message = "Boolean expressions are filters and can't be used as values directly, use std.as_bool to cast them into True/False."
        self.source = source or Errors.call_source()
        self.content = self.format_message()

        super().__init__(self.message, self.name, self.content, source=self.source)

    def format_message(self):
        marked = mark_source(self.source, self.source.line, self.source.line) if self.source else ""
        return textwrap.dedent(f"""
        Boolean expressions are filters and can't be used as values directly. You can use relationalai.std.as_bool(..) to cast them into True/False.

        {marked}
        """)

class AsBoolForNonFilter(RAIException):
    def __init__(self, source=None):
        self.name = "as_bool used on non-filter"
        self.message = "as_bool can only be used on boolean expressions."
        self.source = source or Errors.call_source()
        self.content = self.format_message()

        super().__init__(self.message, self.name, self.content, source=self.source)

    def format_message(self):
        marked = mark_source(self.source, self.source.line, self.source.line) if self.source else ""
        return textwrap.dedent(f"""
        as_bool can only be used on boolean expressions.

        {marked}
        """)

class PropertyCaseMismatch(RAIWarning):
    def __init__(self, name, found_name):
        self.name = "Similar property name"
        self.message = ".{name} doesn't exist, but .{found_name} does"
        self.source = Errors.call_source()
        self.content = self.format_message(name, found_name)

    def format_message(self, name, found_name):
        source = self.source or debugging.SourceInfo()
        found = PropertyFinder(source.line, [name])
        if source.block:
            found.visit(source.block)
        found_lines = found.found_properties_lines or found.dynamic_properties
        marked = mark_source(source, -1, -1, indent=8, highlight_lines=found_lines)

        updated = mark_source(
            source.modify(PropertyNameReplacer(name, found_name)),
            -1, -1, indent=8, highlight_lines=found_lines, highlight="green",
        )

        return textwrap.dedent(f"""
        The property [yellow]{name}[/yellow] doesn't exist, but the very similar [green]{found_name}[/green] does.

        {marked}

        Did you mean [green]{found_name}[/green] instead?

        {updated}
        """)


class NonVarObject(RAIException, TypeError):
    def __init__(self, obj: Any, message: str):
        self.obj = obj
        self.message = message
        self.name = "non-var object used as variable"
        self.source = Errors.call_source(4)

        # Mark the source if available
        if self.source:
            self.marked = mark_source(self.source, self.source.line, self.source.line)
        else:
            self.marked = ""

        # Format the content and raw_content
        self.content = self.format_message()
        self.raw_content = self.strip_rich_tags()

        super().__init__(self.message, self.name, self.content, self.source)

    def format_message(self):
        if self.source:
            return textwrap.dedent(f"""
            [yellow]{self.obj.__class__.__name__}[/yellow] objects can't be used as variables, such as in a .add(), .set(), or select().

            {self.marked}
            """)
        else:
            return textwrap.dedent(f"""
            [yellow]{self.obj.__class__.__name__}[/yellow] objects can't be used as variables, such as in a .add(), .set(), or select().
            """)

class KeyedCantBeExtended(RAIException):
    def __init__(self):
        self.name = "Keyed types can't be extended"
        self.message = "Keyed types can't be extended."
        self.source = Errors.call_source() or debugging.SourceInfo()
        self.content = self.format_message()

        super().__init__(self.message, self.name, self.content, source=self.source)

    def format_message(self):
        marked = mark_source(self.source, self.source.line, self.source.line)
        return textwrap.dedent(f"""
        Keyed types can't be extended, use .add() in a rule instead.

        {marked}
        """)

class KeyedWrongArity(RAIException):
    def __init__(self, name:str, keys:List[str], given:int):
        self.name = "Incorrect number of keys"
        verb = "was" if given == 1 else "were"
        self.message = f"{name} expects {len(keys)} keys ({', '.join(keys)}), but only {given} {verb} given."
        self.source = Errors.call_source() or debugging.SourceInfo()
        self.content = self.format_message()

        super().__init__(self.message, self.name, self.content, source=self.source)

    def format_message(self):
        marked = mark_source(self.source, self.source.line, self.source.line)
        return textwrap.dedent(f"""
        {self.message}

        {marked}
        """)

class RowLiteralTooLargeWarning(RAIWarning):
    def __init__(self, size, max_size=1000):
        self.name = "Large row literal"
        self.message = f"Rows with more than {max_size} items can be slow to compile."
        self.size = size
        self.max_size = max_size
        self.source = Errors.call_source() or debugging.SourceInfo()
        self.content = self.format_message()

    def format_message(self):
        marked = mark_source(self.source, self.source.line, self.source.line)
        return textwrap.dedent(f"""
        Rows with more than {self.max_size} items can be slow to compile. This one has {self.size} items:

        {marked}
        """)

class RowLiteralTooLarge(RAIException):
    def __init__(self, size, max_size=10000):
        self.name = "Row literal too large"
        self.message = f"Rows can't have more than {max_size} items."
        self.size = size
        self.max_size = max_size
        self.source = Errors.call_source() or debugging.SourceInfo()
        self.content = self.format_message()

    def format_message(self):
        marked = mark_source(self.source, self.source.line, self.source.line)
        return textwrap.dedent(f"""
        Rows can't have more than {self.max_size} items. This one has {self.size} items:

        {marked}
        """)

class RowLiteralMismatch(RAIException):
    def __init__(self, mismatched_thing:str):
        self.name = "Row literal mismatch"
        self.message = f"All rows in a row literal must have the same {mismatched_thing}"
        self.mismatched_thing = mismatched_thing
        self.source = Errors.call_source() or debugging.SourceInfo()
        self.content = self.format_message()

    def format_message(self):
        marked = mark_source(self.source, self.source.line, self.source.line)
        return textwrap.dedent(f"""
        All rows in a row literal must have the same {self.mismatched_thing}

        {marked}
        """)


# --------------------------------------------------
# DSL property exceptions
# --------------------------------------------------


class ReservedPropertyException(RAIException):
    def __init__(self, source, property_name: str):
        self.name = "Reserved property name"
        self.message = f"The property '{property_name}' is a reserved property name on RelationalAI types."
        self.source = source
        self.content = self.format_message(property_name)

        super().__init__(self.message, self.name, self.content, source=self.source)

    def format_message(self, property_name):
        marked = mark_source(self.source, self.source.line, self.source.line)
        return textwrap.dedent(f"""
        The property '{property_name}' is a reserved property name on RelationalAI types.

        {marked}
        """)


class NonCallablePropertyException(RAIException):
    def __init__(self, source, property_name: str):
        self.name = "Non-callable property"
        self.message = f"The property '{property_name}' is not callable."
        self.source = source
        self.content = self.format_message(property_name)

        super().__init__(self.message, self.name, self.content, source=source)

    def format_message(self, property_name):
        marked = mark_source(self.source, self.source.line, self.source.line)
        return textwrap.dedent(f"""
        The property '{property_name}' is not callable on RelationalAI types.

        {marked}
        """)

class InvalidPropertySetException(RAIException):
    def __init__(self, source):
        self.name = "Invalid property set"
        self.message = "You can't set properties directly on a RAI object."
        self.source = source
        self.start_line = source.line
        self.end_line = source.line
        self.content = self.format_message()
        self.raw_content = self.strip_rich_tags()
        super().__init__(
            message=self.message, name=self.name, source=source, content=self.content
        )

    def format_message(self):
        marked = self.mark_source()
        dynamic = mark_source(
            self.source.modify(SetToMethod()),
            self.start_line,
            self.end_line,
            highlight="green",
        )
        compare = mark_source(
            self.source.modify(AssignToCompare()),
            self.start_line,
            self.end_line,
            highlight="green",
        )

        return textwrap.dedent(f"""
        You can't set properties directly on a RAI object.

        {marked}

        If you are trying to set the value of a property use [green]set()[/green]:

        {dynamic}

        Or maybe you meant [green]==[/green] instead?

        {compare}
        """)

    def mark_source(self):
        return mark_source(self.source, self.start_line, self.end_line)

class MultipleIdentities(RAIException):
    def __init__(self):
        source = Errors.call_source()
        self.name = "Multiple identities"
        self.message = "You can't pass multiple identity variables for a single object."
        self.source = source
        self.content = self.format_message()

        super().__init__(self.message, self.name, self.content, source=self.source)

    def format_message(self):
        marked = mark_source(self.source, self.source.line, self.source.line) if self.source else ""
        return textwrap.dedent(f"""
        You can't pass multiple identity variables for a single object.

        {marked}
        """)

# --------------------------------------------------
# Graph library exceptions
# --------------------------------------------------

class DirectedGraphNotApplicable(RAIValueError):
    def __init__(self, name: str):
        super().__init__(name)
        self.name = f"algorithm `{name}` is not applicable to directed graphs"

class DirectedGraphNotSupported(RAIValueError):
    def __init__(self, name: str):
        super().__init__(name)
        self.name = f"algorithm `{name}` does not currently support directed graphs"


class ParameterTypeMismatch(RAIValueError):
    def __init__(self, name: str, type_, value):
        super().__init__(name)
        self.name = (
            f"parameter `{name}` must be of type {type_.__name__.lower()}, "
            f"but its value {value!r} is of type {type(value)}"
        )

class ParameterBoundBelowInclusive(RAIValueError):
    def __init__(self, name: str, value, minimum):
        super().__init__(name)
        self.name = f"parameter `{name}` must be greater than or equal to {minimum}, but is {value!r}"

class ParameterBoundAboveInclusive(RAIValueError):
    def __init__(self, name: str, value, maximum):
        super().__init__(name)
        self.name = f"parameter `{name}` must be less than or equal to {maximum}, but is {value!r}"

class ParameterBoundBelowExclusive(RAIValueError):
    def __init__(self, name: str, value, minimum):
        super().__init__(name)
        self.name = f"parameter `{name}` must be strictly greater than {minimum}, but is {value!r}"

class ParameterBoundAboveExclusive(RAIValueError):
    def __init__(self, name: str, value, maximum):
        super().__init__(name)
        self.name = f"parameter `{name}` must be strictly less than {maximum}, but is {value!r}"


# --------------------------------------------------
# Engine exceptions
# --------------------------------------------------


class EngineNotFoundException(RAIException):
    def __init__(self, engine_name: str, message: str):
        self.engine_name = engine_name
        self.message = message
        self.name = "Engine unavailable"

        # Format the content and raw_content
        self.content = self.format_message()
        self.raw_content = self.strip_rich_tags()

        super().__init__(self.message, self.name, self.content)

    def format_message(self):
        return textwrap.dedent(f"""
        We were unable to detect an existing engine or provision a new engine for you. You can manually create an engine with the following command:

        [green]rai engines:create --name {self.engine_name}[/green]
        """)

class EngineAutoCreateFailed(RAIException):
    def __init__(self, engine_name: str):
        self.engine_name = engine_name
        self.message = "Engine auto-creation failed"
        self.name = "Engine auto-creation failed"

        # Format the content and raw_content
        self.content = self.format_message()
        self.raw_content = self.strip_rich_tags()

        super().__init__(self.message, self.name, self.content)

    def format_message(self):
        return textwrap.dedent(f"""
        Your [yellow]raiconfig.toml[/yellow] file is missing the [yellow]engine[/yellow] key.
        However, we tried to auto-create the engine [yellow]{self.engine_name}[/yellow] but it failed.

        You can manually start the engine with the following command:

        [green]rai engines:create --name {self.engine_name}[/green]
        """)

class EnginePending(RAIException):
    def __init__(self, engine_name: str):
        self.engine_name = engine_name
        self.message = "Engine is in a pending state"
        self.name = "Engine not ready"

        # Format the content and raw_content
        self.content = self.format_message()
        self.raw_content = self.strip_rich_tags()

        super().__init__(self.message, self.name, self.content)

    def format_message(self):
        return textwrap.dedent(f"""
        The engine [yellow]{self.engine_name}[/yellow] is in a pending state. You can see the status of engines with the following command:

        [green]rai engines:list[/green]
        """)

# --------------------------------------------------
# Hex exceptions
# --------------------------------------------------

class HexSessionException(RAIException):
    def __init__(self):
        self.name = "Hex session error"
        self.message = "Missing Snowflake session object in Hex"
        self.content = self.format_message()
        self.raw_content = self.strip_rich_tags()

        super().__init__(self.message, self.name, self.content)

    def format_message(self):
        return textwrap.dedent("""
        To use RelationalAI in Hex, get your Snowflake session and supply it as a connection parameter to `rai.Model` or `rai.Provider`:

        [green]
        import hextoolkit
        hex_snowflake_conn = hextoolkit.get_data_connection('<Your Connection Name>')
        hex_snowpark_session = hex_snowflake_conn.get_snowpark_session()
        [/green]
        """)


# --------------------------------------------------
# Snowflake errors
# --------------------------------------------------

access_integration_warning = textwrap.dedent("""
Make sure that S3_RAI_INTERNAL_BUCKET_EGRESS_INTEGRATION is enabled. You can access the toggle from the vertical ellipsis button in the top-right corner of the Snowflake notebook window: ⋮ > Notebook settings > External access.

If you don't see S3_RAI_INTERNAL_BUCKET_EGRESS_INTEGRATION listed, get an account administrator to run Step 4 in the installation notebook here:

https://relational.ai/notebooks/relationalai-installation.ipynb
""")

class SnowflakeIntegrationMissingException(RAIException):
    def __init__(self):
        self.message = access_integration_warning
        self.name = "Integration not enabled"
        self.content = self.format_message()

        super().__init__(self.message, self.name, self.content)

    def format_message(self):
        return access_integration_warning

class SnowflakeAppMissingException(RAIException):
    def __init__(self, app_name: str):
        self.app_name = app_name
        self.message = f"Either the app '{app_name}' isn't installed in this Snowflake account or you don't have permission to access it."
        self.name = "Couldn't find RelationalAI Snowflake application"
        self.content = self.format_message()

        super().__init__(self.message, self.name, self.content)

    def format_message(self):
        return textwrap.dedent(f"""
        Either the app '{self.app_name}' isn't installed in this Snowflake account or you don't have permission to access it.

        If it's installed under a different name, run 'rai init' on the command line and you can set the app name.

        If the app is installed but your current role doesn't have permission to access the app, switch to a role that does.
        """)


class SnowflakeImportMissingException(RAIException):
    def __init__(self, source: debugging.SourceInfo|None, import_name: str, model_name: str):
        self.source = source
        self.import_name = import_name
        self.model_name = model_name
        self.message = (
            f"The Snowflake object '{import_name}' hasn't been imported into RAI."
        )
        self.name = "Couldn't find import"
        self.content = self.format_message()

        super().__init__(self.message, self.name, self.content)

    def format_message(self):
        return textwrap.dedent(f"""
        The Snowflake object '{self.import_name}' hasn't been imported into RAI.

        You can create an import for it using the rai cli:

          [green]rai imports:stream --source {self.import_name} --model {self.model_name}[/green]
        """)


class SnowflakeChangeTrackingNotEnabledException(RAIException):
    def __init__(self, obj: str | list[str]):
        self.obj = obj
        if isinstance(obj, str):
            self.sql = f"[green]ALTER TABLE {obj} SET CHANGE_TRACKING = TRUE;[/green]"
            self.message = f"Change tracking isn't enabled for '{obj}'."
        elif isinstance(obj, list):
            self.sql = "\n".join([f"[green]ALTER TABLE {o} SET CHANGE_TRACKING = TRUE;[/green]" for o in obj])
            self.message = f"Change tracking isn't enabled for the following tables: {', '.join(obj)}"

        self.name = "Change tracking not enabled"
        self.content = self.format_message()

        super().__init__(self.message, self.name, self.content)

    def format_message(self):
        if isinstance(self.obj, str):
            obj_str = self.obj
        else:
            obj_str = ', '.join(self.obj)

        return (
            f"Change tracking isn't enabled for [yellow]{obj_str}[/yellow].\n\n"
            f"To enable change tracking, you'll need to run the following SQL:\n\n"
            f"{self.sql}"
        ).strip()

class SnowflakeTableObject:
    def __init__(self, message: str, source: str):
        self.message = message
        self.source = source

class SnowflakeTableObjectsException(RAIException):
    def __init__(self, table_objects: List[SnowflakeTableObject]):
        self.table_objects = table_objects
        table_count = len(table_objects)
        table_word = "table" if table_count == 1 else "tables"

        self.message = f"Getting the following {table_word} failed with the error in Snowflake."
        self.name = f"Snowflake {table_word.capitalize()} Streaming Error"

        self.content = self.format_message()

        super().__init__(self.message, self.name, self.content)

    def format_message(self):
        formatted_objects = [
            f"Source: [yellow bold]{obj.source}[/yellow bold]\n\n"
            f"Message: {obj.message.strip()}"
            for obj in self.table_objects
        ]
        return "\n\n".join(formatted_objects)

class SnowflakeInvalidSource(RAIException):
    def __init__(self, source, type_source: str):
        self.source = source
        self.type_source = type_source
        self.message = "Invalid source"
        self.name = "Invalid source"
        self.content = self.format_message()

        super().__init__(self.message, self.name, self.content, self.source)

    def format_message(self):
        marked = mark_source(self.source, self.source.line, self.source.line)
        return textwrap.dedent(f"""
        The source provided isn't a fully qualified Snowflake table or view name:

        {marked}
        """)


class SnowflakeRaiAppNotStarted(RAIException):
    def __init__(self, app_name: str):
        self.app_name = app_name
        self.message = f"The RelationalAI app '{app_name}' isn't started."
        self.name = "The RelationalAI application not started"
        self.content = self.format_message()

        super().__init__(self.message, self.name, self.content)

    def format_message(self):
        return textwrap.dedent(f"""
        Your app '{self.app_name}' has not been activated.
        You can activate it by running the following SQL:

        [green]call app.activate();[/green]
        """)


# --------------------------------------------------
# RAI Warnings
# --------------------------------------------------

class InvalidIfWarning(RAIWarning):
    def __init__(self, task: Task | Action, start_line: int, end_line: int):
        self.name = "Invalid if"
        self.source = debugging.get_source(task)
        self.start_line = start_line
        self.end_line = end_line
        self.content = self.format_message()

    def format_message(self):
        marked = self.mark_source()
        updated = mark_source(
            self.source.modify(IfToWithTransformer()),
            self.start_line,
            self.end_line,
            highlight="green",
        ) if self.source else ""
        dynamic = mark_source(
            self.source.modify(WithDynamic()),
            self.source.line,
            self.end_line,
            highlight="green",
        ) if self.source else ""

        return textwrap.dedent(f"""
        In a RelationalAI query, using an if statement dynamically modifies the structure of the query itself, rather than adding a conditional.

        {marked}

        If you're trying to do an action based on a condition, use a [green]with[/green] statement instead.

        {updated}

        If you are trying to create a dynamic query where parts are conditional, add the [green]dynamic=True[/green] flag to the query like so:

        {dynamic}
        """)

    def mark_source(self):
        return mark_source(self.source, self.start_line, self.end_line)


class InvalidLoopWarning(RAIWarning):
    def __init__(self, task: Task | Action, start_line: int, end_line: int):
        self.name = "Invalid loop"
        self.source = debugging.get_source(task)
        self.start_line = start_line
        self.end_line = end_line
        self.content = self.format_message()

    def format_message(self):
        marked = self.mark_source() if self.source else ""
        dynamic = mark_source(
            self.source.modify(WithDynamic()),
            self.source.line,
            self.end_line,
            highlight="green",
        ) if self.source else ""

        return textwrap.dedent(f"""
        In a RelationalAI query, using a loop statement would dynamically modify the query itself, like a macro.

        {marked}

        If that's the goal, you can add the [green]dynamic=True[/green] flag to the query:

        {dynamic}
        """)

    def mark_source(self):
        return mark_source(self.source, self.start_line, self.end_line)


class InvalidTryWarning(RAIWarning):
    def __init__(self, task: Task | Action, start_line: int, end_line: int):
        self.name = "Invalid try"
        self.source = debugging.get_source(task)
        self.start_line = start_line
        self.end_line = end_line
        self.content = self.format_message()

    def format_message(self):
        marked = self.mark_source()
        dynamic = mark_source(
            self.source.modify(WithDynamic()),
            self.source.line,
            self.end_line,
            highlight="green",
        ) if self.source else ""

        return textwrap.dedent(f"""
        In a RelationalAI query, using a try statement will have no effect unless a macro-like function is being called and can fail.

        {marked}

        If macro-like behavior is the goal, you can add the [green]dynamic=True[/green] flag to the query:

        {dynamic}
        """)

    def mark_source(self):
        return mark_source(self.source, self.start_line, self.end_line)


class InvalidBoolWarning(RAIWarning):
    def __init__(self, source):
        self.name = "Invalid boolean expression with Producer"
        self.source = source
        self.start_line = source.line
        self.end_line = source.line
        self.content = self.format_message()
        self.raw_content = self.strip_rich_tags()

    def format_message(self):
        marked = self.mark_source()
        return textwrap.dedent(f"""
        In a RelationalAI query, the truth values of Producer objects are unknown
        until the query has been evaluated. You may not use Producers in boolean
        expressions, such as those involving [green]if[/green], [green]while[/green], [green]and[/green], [green]or[/green], and [green]not[/green]:

        {marked}

        Producer objects include:

        - [green]Instance[/green] objects, such as [green]person[/green].
        - [green]InstanceProperty[/green] objects, such as [green]person.age[/green].
        - [green]Expression[/green] objects, such as [green]person.age >= 18[/green].
        """)

    def mark_source(self):
        return mark_source(self.source, self.start_line, self.end_line)

# whether the python library or the Rel schema is out of date (or both!)
class InvalidVersionKind(Enum):
    LibraryOutOfDate = 'LibraryOutOfDate'
    SchemaOutOfDate = 'SchemaOutOfDate'
    Incompatible = 'Incompatible'

class RAIInvalidVersionWarning(RAIWarning):
    def __init__(
        self,
        kind: InvalidVersionKind,
        expected: List[Tuple[str, str, str]],
        lock: dict,
        platform: str,
        model_name: str,
        app_name: str,
        engine_name: str,
        errors: List[Tuple[InvalidVersionKind, str, str]] = []
    ):
        super().__init__()
        self.libraries = self.get_current_libs(errors)
        self.expected_lib_version = self.get_expected_lib_version(expected)
        self.current_lib_version = self.get_current_lib_version(lock)
        self.model_name = model_name
        self.app_name = app_name
        self.engine_name = engine_name

        self.name = "Invalid version"

        if kind == InvalidVersionKind.LibraryOutOfDate:
            msg = textwrap.dedent("""
                The RelationalAI python library is out of date with respect to the schema. You can update the library using the following command:

                [green]pip install relationalai --upgrade[/green]
            """).strip()
        elif kind == InvalidVersionKind.SchemaOutOfDate:
            schema_fix = textwrap.dedent(f"""
                You can update the schema using the following stored procedure:

                {self.generate_command_line()}
                """).strip()

            if platform == "azure":
                schema_fix = "Unfortunately, the schema must be recreated in Azure."
            schema_msg = textwrap.dedent("""
                The schema is out of date with respect to the RelationalAI library.
                """).strip()
            msg = f"{schema_msg} {schema_fix}"
        else:
            lib_msg = textwrap.dedent("""
                The RelationalAI python library is incompatible with the current schema.
                You can update the library using the following command:

                [green]pip install relationalai --upgrade[/green]
            """).strip()
            if platform == "azure":
                schema_fix = "In addition, the schema must be recreated in Azure."
            else:
                schema_fix = textwrap.dedent(f"""
                In addition, you can update the schema using the following stored procedure:

                {self.generate_command_line()}
                """).strip()
            msg = f"{lib_msg}\n\n{schema_fix}"

        if len(self.libraries) > 0:
            library_info = self.generate_library_info()
            full_msg = f"{msg}\n\n{library_info}"
        else:
            full_msg = msg

        self.content = full_msg

    def extract_version(self, version_obj):
        match = re.search(r"\('([^']+)'\)", repr(version_obj))
        if match:
            return match.group(1)
        else:
            return ""

    def get_expected_lib_version(self, expected):
        libraries = {}
        for name, _, version_range in expected:
            from_version = self.extract_version(version_range[0])
            to_version = self.extract_version(version_range[1])
            libraries[name] = {"from": from_version, "to": to_version}
        return libraries

    def get_current_lib_version(self, lock):
        libraries = {}
        for k, v in lock.items():
            libraries[k[0]] = v
        return libraries

    def get_current_libs(self, errors=[]):
        if len(errors) == 0:
            return []

        libraries = []
        for _, library, _ in errors:
            libraries.append(library)
        return libraries

    def generate_library_info(self):
        if len(self.libraries) == 1:
            lib = self.libraries[0]
            current_version = self.current_lib_version.get(lib, "unknown")
            expected_version = self.expected_lib_version.get(lib, {})
            from_version = expected_version.get("from", "unknown")
            to_version = expected_version.get("to", "unknown")
            return (
                f"Your current library '{lib}' has version {current_version}. "
                f"However, it is expected to have a version range between {from_version} and {to_version}."
            )
        else:
            info = "Your current libraries have the following issues:\n"
            for lib in self.libraries:
                current_version = self.current_lib_version.get(lib, "unknown")
                expected_version = self.expected_lib_version.get(lib, {})
                from_version = expected_version.get("from", "unknown")
                to_version = expected_version.get("to", "unknown")
                info += (
                    f"- Library '{lib}' has version {current_version}. "
                    f"Expected version range: {from_version} to {to_version}.\n"
                )
            return info.strip()

    def generate_command_line(self):
        return f"[green]CALL {self.app_name or '<relationalai_app_name>'}.api.update_libraries('{self.model_name or '<model_name>'}', '{self.engine_name or '<engine_name>'}')[/green]"


#TODO: Take out call_source from Errors class and put it in the main module
class Errors:
    @staticmethod
    def call_source(steps=None):
        if steps is None:
            return debugging.capture_code_info()
        return debugging.capture_code_info(steps + 1)
