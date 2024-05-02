import ast
import re

def parse_and_compare(code_a: str, code_b: str) -> bool:
    """Parses the two code snippets and compares them to see if they both accomplish the same thing"""
    try:
        tree_a = ast.parse(code_a)
        tree_b = ast.parse(code_b)
        return ast.dump(tree_a) == ast.dump(tree_b)
    except SyntaxError:
        return False

def is_valid_python(code: str):
   """Checks whether the line is valid python code"""
   try:
       ast.parse(code)
       return True
   except SyntaxError:
       return False

def first_non_whitespace(s: str):
    """Extracts the first non-whitespace character in the line"""
    match = re.search(r'\S', s)
    if match:
        return match.group(0)
    else:
        return None

def is_comment(code: str) -> bool:
    """Checks if the line of code is a comment"""
    first_non_whitespace(code)
    return first_non_whitespace(code) == "#"

def normalize_code(code: str) -> str:
    """Removes leading/trailing whitespace and normalizes indentation"""
    lines = code.strip().split('\n')
    normalized_lines = [line.strip() for line in lines]
    return '\n'.join(normalized_lines)

def is_diff(code: str) -> bool:
    return code.startswith('-') or code.startswith('+')

def categorize_diff(diff: str) -> str:
    """Categorizes the different kinds of diffs"""
    type = None
    if is_diff(diff) and is_comment(diff[1:]):
        type = 'comment'
    elif is_diff(diff):
        type = 'interpreter'
    else:
        type = 'formatting'

    return {"type": type, "diff": diff}