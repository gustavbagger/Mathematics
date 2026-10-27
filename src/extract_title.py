import re

def extract_title(markdown):
    match = re.match(r"title:[ \t]*(.+)", markdown)
    if not match:
        raise ValueError("First line must be: title: TITLE")
    return match.group(1).strip()

