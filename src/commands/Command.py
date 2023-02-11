class Command:
    """A parent class for all commands in the atlas virtual assistant"""

    def __init__(self, name: str, help: str):
        self.name = name
        self.help = help


def run(self):
    """Method to be overridden by child classes to implement specific functionality for each command"""
    pass
