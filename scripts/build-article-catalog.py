"""Build the dashboard's public article title index from canonical HTML pages."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
SECTIONS = {
    "claims": "보험금 청구", "silbi": "실비보험", "diagnosis-benefit": "진단비",
    "surgery-benefit": "수술비", "treatment-costs": "치료비", "standards": "약관·기준",
    "cases": "생활 사례", "underwriting": "가입 심사", "cancers": "암 정보",
    "caregiver": "간병", "checkups": "건강검진", "guides": "방문 가이드",
}


class ArticleParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_title = False
        self.title = []
        self.canonical = ""
        self.noindex = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "title":
            self.in_title = True
        if tag == "link" and attrs.get("rel") == "canonical":
            self.canonical = attrs.get("href", "")
        if tag == "meta" and attrs.get("name") == "robots":
            self.noindex = "noindex" in attrs.get("content", "")

    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False

    def handle_data(self, data):
        if self.in_title:
            self.title.append(data)


articles = {}
for section, category in SECTIONS.items():
    for file in sorted((ROOT / section).rglob("*.html")):
        if file.name == "index.html" or "page" in file.relative_to(ROOT / section).parts:
            continue
        parser = ArticleParser()
        parser.feed(file.read_text(encoding="utf-8"))
        canonical = urlparse(parser.canonical)
        if parser.noindex or canonical.hostname != "hospital.hbuby.com" or not parser.title:
            continue
        path = canonical.path.removesuffix(".html").rstrip("/") or "/"
        articles[path] = {"path": path, "title": "".join(parser.title).strip(), "category": category}

output = json.dumps(list(articles.values()), ensure_ascii=False, indent=2) + "\n"
target = ROOT / "assets" / "article-catalog.json"
if "--check" in sys.argv:
    if not target.exists() or target.read_text(encoding="utf-8") != output:
        raise SystemExit("Article catalog needs updating: python scripts/build-article-catalog.py")
else:
    target.write_text(output, encoding="utf-8")
print(f"Article catalog: {len(articles)} articles")
