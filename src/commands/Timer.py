from classes.Messanger import Messanger
from commands.Command import Command


class Timer(Command):
    DOCS = {}
    def __init__(self, name:str, flags):
        super().__init__(name, flags)

    def run(self, options):
        self.validate(options=options)
        self.help(docs=Timer.DOCS, options=options)

        # command execution goes here