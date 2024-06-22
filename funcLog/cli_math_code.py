#!.env/Scripts/python.exe

"""
Build a click-base CLI that uses the logic in math_code.py
"""
import click
from math_code import add, sub, mul, div


@click.group()
def cli() -> None:
    """
    A CLI app that used the math_code functions.

    Example:

    $ cliMathCode.py add 1 2\n
    $ cliMathCode.py sub 3 2\n
    $ cliMathCode.py mul 6 7\n
    $ cliMathCode.py div 14 7\n
    """


@cli.command("add")
@click.argument("a", type=int)
@click.argument("b", type=int)
def cli_add(a: int, b: int) -> None:
    """Add two numbers"""
    click.echo(add(a, b))


@cli.command("sub")
@click.argument("a", type=int)
@click.argument("b", type=int)
def cli_sub(a: int, b: int) -> None:
    """Subtract two numbers"""
    click.echo(sub(a, b))


@cli.command("mul")
@click.argument("a", type=int)
@click.argument("b", type=int)
def cli_mul(a: int, b: int) -> None:
    """Multiply two numbers"""
    click.echo(mul(a, b))


@cli.command("div")
@click.argument("a", type=int)
@click.argument("b", type=int)
def cli_div(a: int, b: int) -> None:
    """Divide two numbers"""
    click.echo(div(a, b))


if __name__ == "__main__":
    cli()
