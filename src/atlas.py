import os
import click

from commands.hello import Hello


@click.group()
@click.pass_context
def cli(ctx):
    pass


hello = Hello(cli=cli)
hello.create()


if __name__ == '__main__':
    cli()
