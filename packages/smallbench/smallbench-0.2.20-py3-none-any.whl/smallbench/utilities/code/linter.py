import ast
from io import StringIO
from pylint import epylint as lint


def lint_code(code_string):
    # First, check for syntax errors
    try:
        ast.parse(code_string)
    except SyntaxError as e:
        return f"Syntax Error: {str(e)}"

    # Create a temporary file-like object
    temp_file = StringIO(code_string)

    # Run pylint with specific options
    (pylint_stdout, pylint_stderr) = lint.py_run(
        temp_file.getvalue(),
        return_std=True,
        # Focus on errors and some critical warnings
        args=[
            "-E",
            "--disable=all",
            "--enable=error,undefined-variable,used-before-assignment,dangerous-default-value",
        ],
    )

    # Get the output as a string
    output = pylint_stdout.getvalue()

    return output if output.strip() else "No issues found with code."
