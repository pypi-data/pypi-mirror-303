import re
from fuzzysearch import find_near_matches

def extract_citations(text: str) -> list[str]:
    # A pattern that captures text between various kinds of quotation marks
    pattern = r'[“«„‚‘"‹\'](.+?)[”»„‚’"›\']'

    citations = re.findall(pattern, text)
    return citations

def fuzzy_find_in_text(citation: str, text: str, max_distance: int) -> str:
    # Clean the text and citation by collapsing multiple spaces and normalizing newlines
    text = re.sub(r'\s+', ' ', text)
    citation = re.sub(r'\s+', ' ', citation)

    # First check if the citation is an exact match, ignoring case
    # (because this is common and faster)
    exact_match = re.search(re.escape(citation), text, re.IGNORECASE)
    if exact_match:
        return (exact_match.group(), 0)

    # Otherwise, use fuzzy search to find the closest
    matches = find_near_matches(citation, text, max_l_dist=min(len(citation)//4, max_distance))
    if not matches:
        return None
    else:
        # Find the match with the smallest distance
        best_match = min(matches, key=lambda match: match.dist)
        return (best_match.matched, best_match.dist)
