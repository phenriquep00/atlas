import os
from commands.command import Command

import click
import openai


openai.api_key = os.getenv("OPENAI_API_KEY")

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
                temperature=0.6
            )
            click.echo(f'{response.choices[0].text} \n')
