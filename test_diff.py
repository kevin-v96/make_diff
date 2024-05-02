from make_diff import resolve_diff
import pytest

test_data = [
    (
        ("  # Router definition" "\napi_router = APIRouter()"),
        (
            "  # Make sure endpoint are immune to missing trailing slashes"
            "\napi_router = APIRouter(redirect_slashes=True)"
        ),
        ["- api_router = APIRouter()\n+ api_router = APIRouter(redirect_slashes=True)"],
    ),
    (
        (
            "  # Make sure endpoint are immune to missing trailing slashes"
            "\napi_router = APIRouter(redirect_slashes=True)"
        ),
        (
            "# Router definition"
            "\napi_router = APIRouter("
            "\n\tredirect_slashes=True"
            "\n)"
        ),
        [],
    ),
    #(no semantic difference)
    ("x = 5", "  x = 5", []),
    #(comment addition is ignored)
    ("x = 5", "# This assigns 5 to x\n x = 5", []),
    #(change affects program behavior)
    ("x = 5", "y = 5", ["- x = 5\n+ y = 5"]),
    #(change affects program behavior)
    ("print('Hello')", "print(f'Hello, world!')", ["- print('Hello')\n+ print(f'Hello, world!')"])
]


@pytest.mark.parametrize("snippet_a, snippet_b, expected_result", test_data)
def test_correct_diff(snippet_a, snippet_b, expected_result):
    assert resolve_diff(snippet_a, snippet_b) == expected_result
