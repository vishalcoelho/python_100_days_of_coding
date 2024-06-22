#!.env/Scripts/python.exe
"""Use click to build out a CLI for the wiki_news_keywords.py library"""

import click

import wiki_news_keywords as wnk

# build a click group
@click.group()
def cli():
    """Search for keywords in wikipedia articles.

    Example:

    $ cli_wiki_keywords search "python"

    $ cli_wiki_keywords content "ftx bankruptcy"
    """
    pass


# build a click command for the search function
@click.command("search")
@click.argument("search_term", type=str, default="FTX Bankruptcy")
def search(search_term):
    """Search for a wikipedia article.

    Example:
    $ cli_wiki_keywords search "python"
    """
    search_results = wnk.wiki_search(search_term)
    click.echo(search_results)


# build a click command for the keywords function
@click.command("keywords")
@click.argument("search_term", type=str, default="FTX Bankruptcy")
@click.option("--limit", type=int, default=3)
def keywords(search_term, limit):
    """Return the top 10 keywords from a wikipedia article.

    Example:
    $ cli_wiki_keywords keywords "python"
    """
    keywords_results = wnk.wiki_keywords(search_term)
    for keyword in keywords_results[:limit]:
        click.echo(click.style(keyword[0], fg="green"))


if __name__ == "__main__":
    cli.add_command(search)
    cli.add_command(keywords)
    cli()
