from classes.Messanger import Messanger
from commands.Command import Command


class SpeedTest(Command):
    DOCS = {}

    def __init__(self, name, flags):
        super().__init__(name, flags)

    def run(self, options):
        self.validate(options=options)
        self.help(docs=SpeedTest.DOCS, options=options)
