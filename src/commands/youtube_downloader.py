import os
import click
from commands.command import Command

from pytube import YouTube


class YoutubeDownloader(Command):
    def __init__(self, cli):
        super().__init__(cli)

    def create(self):
        @self.cli.command(help="download youtube videos")
        @click.option("--filename", required=False, )
        @click.argument("url", required=True)
        def yt_dl(url, filename):
            youtubeObject = YouTube(url)
            youtubeObject = youtubeObject.streams.filter(
                file_extension="mp4").get_highest_resolution()
            try:
                if filename:
                    youtubeObject.download(
                        output_path=f"{os.environ['UserProfile']}/Videos", filename=f'{filename}.mp4')
                else:
                    youtubeObject.download(
                        f"{os.environ['UserProfile']}/Videos")
            except:
                click.echo("An error has occurred")
            click.echo("Download is completed successfully")
