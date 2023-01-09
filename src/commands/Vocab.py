import string
from classes.Messanger import Messanger
from commands.Command import Command
import requests


class Vocab(Command):
    """Display data about a single word from the user input

    Args:
        Command (Commans): Command class
    Returns:
        _type_: none
    """

    # command documentation
    DOCS = {
        "-help": "Vocabulary command (english only for now)",
    }

    # initializing the command
    def __init__(self, name, flags):
        # inherit attributes
        super().__init__(name, flags)

    def run(self, options):
        """runs the vocab command
        validating the flags and the asking the user for the word do analyse
        the method then proceeds to find the word in the api. If the word exists
        in the api, returns information about it

        Args:
            options (_type_): command options
        """
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

        Messanger.message(tag="hint", text="loading...")
        response = requests.get(
            f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
        )

        try:
            if response.json()["title"]:
                Messanger.message(
                    tag="failure",
                    text="Sorry pal, we couldn't find definitions for the word you were looking for.",
                )
        except TypeError:
            data = response.json()[0]

            Vocab.formatted_data(data=data)

            Messanger.message(tag="success", text="Vocab ran succesfully")

    @staticmethod
    def check_word():
        """checks if the word contains only ascii letters characters

        Returns:
            _word: returns the word in case it is valid
        """
        word = str(input("What word would you like to get information from: \n"))
        for letter in word:
            if letter not in string.ascii_letters:
                raise (ValueError)

        return word

    @staticmethod
    def formatted_data(data):
        """display the formatted information from the api about the word

        Args:
            data (obj): the response from the api
        """
        Messanger.message(
            tag="success", text=f"Prompting data for the word {data['word'].upper()}"
        )

        print("Definitions: \n")
        for meaning in data["meanings"]:
            print(f"  ---> {meaning['definitions'][0]['definition']}")
        print("")

        print("Synonyms: \n")
        for meaning in data["meanings"]:
            print(f"  ---> {meaning['definitions'][0]['synonyms']}")
        print("")

# TODO:
# - return more information from the words
# - add language flags to access diferent dictionaries
# - add flags to display custom information about the word:
#       - return only definitions
#       - return only synonims
#       - return only examples