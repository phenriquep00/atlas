import click
from commands.command import Command

from pytube import YouTube


class YoutubeDownloader(Command):
    def __init__(self, cli):
        super().__init__(cli)

    def create(self):
        @self.cli.command(help="download youtube videos")
        @click.argument("url", required=True)
        def yt_dl(url):
            youtubeObject = YouTube(url)
            youtubeObject = youtubeObject.streams.get_highest_resolution()
            try:
                youtubeObject.download()
            except:
                click.echo("An error has occurred")
            click.echo("Download is completed successfully")
