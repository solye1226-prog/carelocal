"""Check canonical URLs and sitemap entries against Pages' clean URL routes."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse
import sys
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
HOST = "https://hospital.hbuby.com"


class CanonicalParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.canonicals = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "link" and attrs.get("rel") == "canonical":
            self.canonicals.append(attrs.get("href", ""))


def check():
    namespaces = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    entries = [node.text for node in ET.parse(ROOT / "sitemap.xml").findall(".//s:loc", namespaces)]
    errors = []
    if len(entries) != len(set(entries)):
        errors.append("Duplicate sitemap URLs")
    for url in entries:
        if not url or urlparse(url).netloc != urlparse(HOST).netloc:
            errors.append(f"Unexpected sitemap hostname: {url}")
            continue
        parsed = urlparse(url)
        if parsed.query or parsed.fragment or parsed.path.endswith(".html"):
            errors.append(f"Noncanonical sitemap URL: {url}")
            continue
        route = parsed.path
        path = ROOT / (route.lstrip("/") + "index.html" if route.endswith("/") else route.lstrip("/") + ".html")
        if not path.is_file():
            errors.append(f"Missing canonical target: {url}")
            continue
        parser = CanonicalParser()
        parser.feed(path.read_text(encoding="utf-8"))
        if parser.canonicals != [url]:
            errors.append(f"Canonical mismatch: {path.relative_to(ROOT)} -> {parser.canonicals}, expected {url}")
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"Checked {len(entries)} sitemap URLs: clean URLs, unique entries and matching self-canonicals.")
    return 0


if __name__ == "__main__":
    sys.exit(check())
