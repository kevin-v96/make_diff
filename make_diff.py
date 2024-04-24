import difflib as dl
from typing import List
from functools import reduce
from utils import normalize_code, is_valid_python, is_comment, parse_and_compare, categorize_diff

def get_coupled_diff_lines(diffs: List[str]) -> List[str]:
    """Returns lines from the diff coupled with each other"""
    changed_lines_a = []
    changed_lines_b = []

    for line in diffs:
        if line.startswith('-'):
            changed_lines_a.append(line)
        elif line.startswith('+'):
            changed_lines_b.append(line)

    coupled_diffs = [a + '\n' + b for a, b in zip(changed_lines_a, changed_lines_b)]
    return coupled_diffs

def resolve_diff(snippet_a: str, snippet_b: str) -> List[str]:
    """Return simple diff only if it has code change that will be noticed by python interpreter"""
    #check if there are no programmatic differences in the snippets
    if parse_and_compare(snippet_a, snippet_b):
        return []
    
    normalized_a = normalize_code(snippet_a)
    normalized_b = normalize_code(snippet_b)

    diff = dl.ndiff(normalized_a.split('\n'), normalized_b.split('\n'))

    filtered_diff = [
        line for line in diff
        if is_valid_python(line[2:])
        and not (line.startswith('?') or line.startswith(' ') or is_comment(line[2:]))
    ]

    diffs = get_coupled_diff_lines(filtered_diff)
    return diffs

def resolve_categorized_diff(snippet_a: str, snippet_b: str) -> List[str]:
    #check if there are no programmatic differences in the snippets
    if parse_and_compare(snippet_a, snippet_b):
        return []
    
    normalized_a = normalize_code(snippet_a)
    normalized_b = normalize_code(snippet_b)

    diff = dl.ndiff(normalized_a.split('\n'), normalized_b.split('\n'))

    diffs = get_coupled_diff_lines(diff)
    
    diffs_with_types = reduce(lambda acc, val: acc + [val],  map(categorize_diff, diffs), [])

    return diffs_with_types

