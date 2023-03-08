import os, sys
import click

from commands.hello import Hello
from commands.ping import Ping


@click.group()
@click.pass_context
def cli(ctx):
    pass


hello = Hello(cli=cli)
hello.create()

ping = Ping(cli=cli)
ping.create()


if __name__ == '__main__':
    cli()
