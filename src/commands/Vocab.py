import string
from classes.Messanger import Messanger
from commands.Command import Command
import requests


class Vocab(Command):

    DOCS = {
        "-help": "Vocabulary command (english only for now)",
    }

    def __init__(self, name, flags):
        super().__init__(name, flags)

    def run(self, options):
        self.validate(options=options)
        self.help(docs=Vocab.DOCS, options=options)

        while ...:
            # ask the user for the word to analyse
            try:

                word = Vocab.check_word()
                break
            except ValueError:
                Messanger.message(
                    tag="failure",
                    text="invalid value, please type a alphabetical value",
                )

        response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")

        print(response.json())

        Messanger.message(tag="success", text="Vocab ran succesfully")

    @staticmethod
    def check_word():
        word = str(input("What word would you like to get information from: "))
        for letter in word:
            if letter not in string.ascii_letters:
                raise(ValueError)

        return word

