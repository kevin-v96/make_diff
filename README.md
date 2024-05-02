### Requirements
Run `pip install -r requirements.txt` to install the required modules. 

### Testing
Simply run `pytest` after installing the requirements to run the tests I've written for both the functions.
If you want to add your own tests, you can add them by appending a tupple of `(snippet_a, snippet_b, expected_result)` in `test_data` in either of the test files. In case any tests fail and you want to see what is making them fail in detail, you can run `pytest -vv`.

### references
- https://docs.python.org/3/library/ast.html
- https://petr-muller.github.io/projects/2018/04/06/python-diff-started.html
- https://docs.python.org/dev/library/difflib.html#difflib.ndiff