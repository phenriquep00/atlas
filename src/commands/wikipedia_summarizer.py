import click
from commands.command import Command

import wikipedia


class WikipediaSummarizer(Command):
    def __init__(self, cli):
        super().__init__(cli)

    def create(self):
        @self.cli.command(help="get information from a given topic based on it's wikipedia article")
        @click.option("--article", required=True, help="the name of the article to be summarized")
        @click.option("--len", default=2, type=int, help="lenght of the summary to be printed (number of sentences)", show_default=True)
        def wiki(article, len):
            summary = wikipedia.summary(article, sentences=len)
            click.echo(summary)
