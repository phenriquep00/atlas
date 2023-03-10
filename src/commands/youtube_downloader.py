import os
import click
from pytube import YouTube

from commands.command import Command


class YoutubeDownloader(Command):
    def __init__(self, cli):
        super().__init__(cli)

    def create(self):
        @self.cli.command(help="download youtube videos")
        @click.option("--filename", required=False, )
        @click.option("--path", default=f"{os.environ['UserProfile']}/Videos")
        @click.argument("url", required=True)
        def yt_dl(url, filename, path):
            youtubeObject = YouTube(url)
            youtubeObject = youtubeObject.streams.filter(
                file_extension="mp4").get_highest_resolution()
            try:
                if filename:
                    youtubeObject.download(
                        output_path=path, filename=f'{filename}.mp4')
                else:
                    youtubeObject.download(path)
            except:
                click.echo("An error has occurred")
            click.echo("Download is completed successfully")
