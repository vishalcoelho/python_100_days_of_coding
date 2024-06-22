"""
Build out a library that finds news from wikipedia and returns the top 10 keywords from the article.
"""

import wikipedia
import yake

from typing import List, Any


def wiki_search(search_term: str) -> List[Any]:
    """
    Get the top 10 keywords from a wikipedia article.
    """
    list_of_terms = []
    try:
        list_of_terms = wikipedia.search(search_term, results=10)
    except wikipedia.exceptions.DisambiguationError as _exc:
        print(_exc)
    else:
        return list_of_terms


def wiki_content(search_term: str) -> Any:
    """Get the page content for a particular term."""
    try:
        return wikipedia.page(search_term).content
    except wikipedia.exceptions.DisambiguationError as _exc:
        print(_exc)


def wiki_keywords(search_term: str) -> List[Any]:
    """
    Function that returns the top 10 keyworks from a wikipedia article using yake.
    """
    content = wiki_content(search_term)
    kw_extractor = yake.KeywordExtractor()
    keywords = kw_extractor.extract_keywords(content)
    return keywords


if __name__ == "__main__":
    try:
        search_terms = wiki_search("Trains")
        print(wiki_keywords("Bankruptcy of FTX"))
    except NameError as exc:
        print(f"Error: {exc}")
