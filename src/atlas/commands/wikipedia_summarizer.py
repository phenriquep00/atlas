from atlas.Command import Command

import os
import click
import wikipedia
import playsound

from gtts import gTTS


class WikipediaSummarizer(Command):
    def __init__(self, cli):
        super().__init__(cli)

    def create(self):
        @self.cli.command(help="get information from a given topic based on it's wikipedia article")
        @click.option("--article", required=True, help="the name of the article to be summarized")
        @click.option("--len", default=2, type=int, help="lenght of the summary to be printed (number of sentences)", show_default=True)
        @click.option("--read", default=False, is_flag=True, help="read the summary")
        @click.option("--hide", default=False, is_flag=True, help="hide the textual summary")
        def wiki(article, len, read, hide):
            summary = wikipedia.summary(article, sentences=len)
            if not hide:
                click.echo(summary)
            if read:
                WikipediaSummarizer.speak(summary)

    @staticmethod
    def speak(text):
        tts = gTTS(text=text, lang='en')

        filename = "abc.mp3"
        tts.save(filename)
        playsound.playsound(filename)
        os.remove(filename)
