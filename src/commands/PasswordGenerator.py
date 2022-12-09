from classes.Messanger import Messanger
from commands.Command import Command


class PasswordGenerator(Command):
    DOCS = {
        "-help": "display password generator usage",
        "-digits": "number of characters to be included in the generated password default: 8",
        "-copy": "copy the password to clipboard",
        "-hide": "down display the generated password",
    }

    def __init__(self, name, flags):
        super().__init__(name, flags)

    def run(self, options):
        self.validate(options=options)
        self.help(docs=PasswordGenerator.DOCS, options=options)
        Messanger.message(tag="success", text="Running password generator")
