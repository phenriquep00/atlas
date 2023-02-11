from commands.command import Command


class Greet(Command):
    """A child class to implement the 'hello' command"""
    def run(self):
        """Prints a greeting to the user"""
        print("Hello, thanks for using the atlas virtual assistant! if you get lost, just use 'atlas -h' or 'atlas --help' to get some help")