from commands.command import Command

from pytube import YouTube

class YoutubeDownloader(Command):
    def run(self):
        print('downloader')