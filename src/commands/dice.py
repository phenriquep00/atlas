import click
from commands.command import Command

from random import choice

class Dice(Command):
    def __init__(self, cli):
        super().__init__(cli)

    def create(self):
        @self.cli.command(help="roll a dice and returns a random number")
        @click.argument("size", required=True)
        def dice(size):
            result = choice(list(range(1, int(size)+1)))
            click.echo(f"The result for the dice is: {result}")
        