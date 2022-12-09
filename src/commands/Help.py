from classes.Messanger import Messanger
from commands.Command import Command


class Help(Command):

    DOCS = {
        "-help": "display the documentation for the help command",
    }

    def __init__(self, name, flags):
        super().__init__(name, flags)

    def run(self, options):
        self.validate(options=options)
        self.help(Help.DOCS, options=options)
        Messanger.message(tag="success", text="running test command\nTODO: display all commands and it's usage")