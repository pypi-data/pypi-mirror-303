import ast
import tempfile
from io import StringIO
from pylint import lint
import contextlib
import os


def lint_code(code_string):
    """
    Lints the provided Python code string using pylint and returns the linting results.

    Args:
        code_string (str): The Python code to lint.

    Returns:
        str: The linting results or a message indicating no issues were found.
    """
    # First, check for syntax errors
    try:
        ast.parse(code_string)
    except SyntaxError as e:
        return f"Syntax Error: {str(e)}"

    # Write code_string to a temporary file
    with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as tmp_file:
        tmp_file.write(code_string)
        tmp_file_path = tmp_file.name

    # Prepare to capture stdout and stderr
    pylint_output = StringIO()
    with contextlib.redirect_stdout(pylint_output), contextlib.redirect_stderr(pylint_output):
        try:
            lint.Run(
                [
                    "--errors-only",
                    "--disable=all",
                    "--enable=error,undefined-variable,used-before-assignment,dangerous-default-value",
                    tmp_file_path
                ],
                exit=False,
            )
        except Exception as e:
            return f"Pylint run failed: {str(e)}"
        finally:
            os.unlink(tmp_file_path)  # Remove the temporary file

    # Get the output as a string
    output = pylint_output.getvalue()

    return output if output.strip() else "No issues found with code."


if __name__ == "__main__":
    buggy_code = '''
def calculate_sum(a, b):
    result = a + b
        return result  # This line is incorrectly indented

def main():
    x = 5
    y = 10
    total = calculate_sum(x, y)
print("The sum is:", total)  # This line should be indented to be inside the main function

if __name__ == "__main__":
    main()
    '''
        
    lint_result = lint_code(buggy_code)
    print("Lint result: ", lint_result)
