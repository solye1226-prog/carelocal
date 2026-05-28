from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse
import sys

ROOT = Path(__file__).resolve().parents[1]


class LinkParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attrs):
        for name, value in attrs:
            if name == "href" and value:
                self.links.append(value)


def target_exists(source, href):
    parsed = urlparse(href)
    if parsed.scheme in {"http", "https", "mailto", "tel"} or href.startswith("#"):
        return True

    clean = parsed.path
    if not clean:
        return True

    base = ROOT if clean.startswith("/") else source.parent
    target = (base / clean.lstrip("/")).resolve()

    if clean.endswith("/"):
        target = target / "index.html"
    elif not target.suffix:
        target = target.with_suffix(".html")

    return target.exists()


failures = []
html_files = [path for path in ROOT.rglob("*.html") if ".git" not in path.parts]

for file_path in html_files:
    parser = LinkParser()
    parser.feed(file_path.read_text(encoding="utf-8"))
    for link in parser.links:
        if not target_exists(file_path, link):
            failures.append(f"{file_path.relative_to(ROOT)} -> {link}")

if failures:
    print("\n".join(failures), file=sys.stderr)
    sys.exit(1)

print(f"Checked {len(html_files)} HTML files. All local links resolve.")
