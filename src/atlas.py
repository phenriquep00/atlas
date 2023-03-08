import os
import sys
import click

from commands.hello import Hello
from commands.ping import Ping


# Definition of the cli commands group
@click.group()
@click.pass_context
def cli(ctx):
    pass


# Commands declaration
# hello command
hello = Hello(cli=cli)
hello.create()

# ping command
ping = Ping(cli=cli)
ping.create()


if __name__ == '__main__':
    cli()
