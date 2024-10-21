import ast
from io import StringIO
from pylint import lint


def lint_code(code_string):
    # First, check for syntax errors
    try:
        ast.parse(code_string)
    except SyntaxError as e:
        return f"Syntax Error: {str(e)}"
    # Run pylint with specific options
    (pylint_stdout, pylint_stderr) = lint.Run(
        ["-E", "--disable=all", "--enable=error,undefined-variable,used-before-assignment,dangerous-default-value"],
        exit=False,
        do_exit=False,
        stdout=StringIO(),
        stderr=StringIO(),
    )

    # Get the output as a string
    output = pylint_stdout.getvalue()

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
    print("Lint result: ",lint_result)
