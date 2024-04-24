from make_diff import resolve_diff, resolve_categorized_diff

if __name__ == "__main__":
    snippet_a = (
	"  # Router definition"
    "\napi_router = APIRouter()"
)
    snippet_b = (
	"  # Make sure endpoint are immune to missing trailing slashes"
    "\napi_router = APIRouter(redirect_slashes=True)"
)
    
    snippet_c = (
	"# Router definition"
    "\napi_router = APIRouter("
    "\n\tredirect_slashes=True"
    "\n)"
)

    print(resolve_categorized_diff(snippet_a, snippet_b))
    print(resolve_categorized_diff(snippet_b, snippet_c))