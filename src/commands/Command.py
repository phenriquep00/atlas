class Command:
    """A parent class for all commands in the atlas virtual assistant"""
    def __init__(self, name):
        self.name = name

    def run(self):
        """Method to be overridden by child classes to implement specific functionality for each command"""
        pass