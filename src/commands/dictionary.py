import click
import requests
from commands.command import Command


class Dictionary(Command):
    def __init__(self, cli):
        super().__init__(cli)
        self.api_endpoint = 'https://api.dictionaryapi.dev/api/v2/entries/en/'

    def create(self):
        @self.cli.command(help="get definition of words in the english dictionary")
        @click.argument("word", required=True)
        def dict(word):
            response = requests.get(self.api_endpoint + word.strip())
            data = response.json()[0]
            formated_data = {
                'word': data['word'],
                'phonetic': data['phonetic'],
                'meanings': [[meaning['partOfSpeech'], meaning['definitions'][0]['definition']] for meaning in data['meanings']]
            }
            click.echo(
                f"Definition of the word \n---{formated_data['word'].upper()}---\n\nphonetic:{formated_data['phonetic']}\nmeanings:\n")
            for meaning in formated_data['meanings']:
                click.echo('--------------------------------------')
                click.echo(meaning[0].upper() +'\n')
                click.echo(meaning[1])
                click.echo('--------------------------------------\n')

