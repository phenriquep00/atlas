from Command import Command
import click


class Hello(Command):
    def __init__(self, cli):
        super().__init__(cli)

    def create(self):
        @self.cli.command(help="a test command just in case")
        @click.option('--lang', default="en")
        def hello(lang):
            if str(lang) == 'pt':
                click.echo('Olá')
            else:
                click.echo('Hello there')
