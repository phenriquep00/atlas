import os
import sys
import click

from commands.hello import Hello
from commands.ping import Ping
from commands.youtube_downloader import YoutubeDownloader
from commands.wikipedia_summarizer import WikipediaSummarizer
from commands.chat import Chat
from commands.dictionary import Dictionary


# Definition of the cli commands group
@click.group()
@click.pass_context
def cli(ctx):
    pass


# Commands declaration
# ----------------------------------------------------------------------------------------
# hello command (hello)
hello = Hello(cli=cli)
hello.create()

# ping command (ping)
ping = Ping(cli=cli)
ping.create()

# youtube downloader (yt-dl)
yt_dl = YoutubeDownloader(cli=cli)
yt_dl.create()

# wikipedia summarizer
wiki = WikipediaSummarizer(cli=cli)
wiki.create()

# AI chat
ask = Chat(cli=cli)
ask.create()

# Dictionary
dictionary = Dictionary(cli=cli)
dictionary.create()

# -------------------------------------------------------------------------------------

if __name__ == '__main__':
    cli()
