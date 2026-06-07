from duckduckgo_search import DDGS


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


