import os


import click
import openai

from Command import Command


# TODO: use api key from .env insteadof the one set on the computer env vars manually

class Chat(Command):
    def __init__(self, cli):
        super().__init__(cli)

    def create(self):
        @self.cli.command(help="ai that generates a response based on a prompt")
        @click.argument("prompt", required=True)
        def ask(prompt):
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=prompt,
                temperature=0,
                max_tokens=256
            )
            click.echo(response)
            click.echo(f'{response.choices[0].text} \n')
