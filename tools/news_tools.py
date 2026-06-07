from duckduckgo_search import DDGS
import requests
from bs4 import BeautifulSoup

def search_news(query, max_results=5):
    results = []

    with DDGS() as ddgs:
        for r in ddgs.text(query, max_results=max_results):
            results.append({
                "title": r.get("title", ""),
                "body": r.get("body", ""),
                "url": r.get("href", "")
            })

    return results


def read_article(url):
    try:
        headers = {
        "User-Agent": "Mozilla/5.0"
        }
        r = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(r.text, "html.parser")
        for tag in soup([
        "script",
        "style",
        "nav",
        "footer"
        ]):
            tag.extract()
        text = soup.get_text(separator="\n")
        return text[:5000]
    except Exception as e:
        return f"Error: {e}"
