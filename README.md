# make_diff
Function that outputs diffs between snippets of code.

### Requirements
Run `pip install -r requirements.txt` to install the required modules. 

### Testing
Simply run `pytest` after installing the requirements to run the tests I've written for both the functions.
If you want to add your own tests, you can add them by appending a tupple of `(snippet_a, snippet_b, expected_result)` in `test_data` in either of the test files. In case any tests fail and you want to see what is making them fail in detail, you can run `pytest -vv`.

### Results
The tests for `resolve_diff` should all pass, the tests for `resolve_categorised_diff` will fail because the function is still not correctly categorising the coupled diffs - I've tracked down the reason for this, which is that my current approach doesn't work when code is divided between lines. Completing `resolve_categorised_diff` is left as a to-do.

### TODO
- [x] Add uncategorised differ
- [ ] Add differ with categories
- [x] Add test cases for both functions

### references
- https://docs.python.org/3/library/ast.html
- https://petr-muller.github.io/projects/2018/04/06/python-diff-started.html
- https://docs.python.org/dev/library/difflib.html#difflib.ndiff
