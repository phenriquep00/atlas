from classes.Messanger import Messanger
from commands.Command import Command
import wikipedia
import pyttsx3

# TODO: work on the reliability of thiw command
# TODO: catch common errors with pyttsx3 api
# TODO: add flags


class WikipediaEntry(Command):
    """
    class to execute the --wikientry-- command within atlas
    this command is responsable for searching entries on wikipedia
    based on the used input for Q


    Args:
        Command (_type_): super class
    """

    DOCS = {"-help": "in progress..."}

    def __init__(self, name: str, flags: list):
        """class constructior

        Args:
            name (str):name of the commmand
            flags (list):list of possible options
        """
        super().__init__(name, flags)

    def run(self, options):
        self.validate(options=options)
        self.help(docs=WikipediaEntry.DOCS, options=options)

        while ...:
            try:
                q = str(input("entry: \n"))
                break
            except ValueError:
                Messanger.message(
                    tag="failure",
                    text="oops! you typed a invalid value, please try again",
                )

        engine = pyttsx3.init()

        results = wikipedia.summary(q, sentences=1)
        print(results)
        engine.say(results)
        engine.runAndWait()
