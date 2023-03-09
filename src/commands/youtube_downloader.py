import click
from commands.command import Command


class YoutubeDownloader(Command):
    def __init__(self, cli):
        super().__init__(cli)

    def create(self):
        @self.cli.command(help="download youtube videos")
        @click.argument("url", required=True)
        def yt_dl(url):
            click.echo(url)