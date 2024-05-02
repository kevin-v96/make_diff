from make_diff import resolve_categorized_diff
import pytest

test_data = [
    (
        ("# Router definition" "\napi_router = APIRouter()"),
        (
            "# Make sure endpoint are immune to missing trailing slashes"
            "\napi_router = APIRouter("
            "\n\tredirect_slashes=True"
            "\n)"
        ),
        [
            {
                "type": "interpreter",
                "diff": "- api_router = APIRouter()\n+ api_router = APIRouter(redirect_slashes=True)",
            },
            {
                "type": "formatting",
                "diff": "- api_router = APIRouter()\n+ api_router = APIRouter(\n\tredirect_slashes=True\n)",
            },
            {
                "type": "comment",
                "diff": "- # Router definition\n+ # Make sure endpoint are immune to missing trailing slashes",
            },
        ],
    ),
    # Only the change is included
    ("x = 5  # Old comment", "# New comment\n  x = 5 + 2", [
     {"type": "comment", "diff": "- # Old comment\n+ # New comment"},
     {"type": "interpreter", "diff": "+ 2"}
 ]),
    # Only formatting change
    (
        "if x > 0:\n  print('Positive')",
        "if x > 0:    print('Positive')",
        [{"type": "formatting", "diff": "+    "}],
    ),
]


@pytest.mark.parametrize("snippet_a, snippet_b, expected_result", test_data)
def test_correct_diff(snippet_a, snippet_b, expected_result):
    assert resolve_categorized_diff(snippet_a, snippet_b) == expected_result
