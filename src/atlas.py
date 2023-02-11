from optparse import OptionParser

from commands.greet import Greet

greet = Greet(name='--hello')

class Atlas:
    """
    The Atlas class represents the virtual assistant, and provides
    the functionality for greeting the user and displaying the version
    and help information.
    """
    def __init__(self):
        """
        Initialize an instance of the Atlas class by creating an
        OptionParser object.
        """
        self.parser = OptionParser()
        self.greet = greet

    def run(self):
        """
        Run the virtual assistant and handle the command line arguments.
        """
        # Add the '--hello' option
        self.parser.add_option("--hello", dest="greet",
                               action="store_true",
                               help="display a greeting to the user")
        
        # Add the '--version' option
        self.parser.add_option("--version", dest="version",
                               action="store_true",
                               help="display the version of Atlas")
        
        # Parse the command line arguments
        (options, args) = self.parser.parse_args()

        
        # If the '--hello' option is specified, call the 'greet' method
        if options.greet:
            self.greet.run()
        
        # If the '--version' option is specified, display the version
        elif options.version:
            print("Atlas version 1.0.0")
        
        
        # If no options are specified, display an error message
        else:
            self.parser.error("Please specify a command. Use 'atlas --help' to see available commands.")

if __name__ == "__main__":
    """
    If the script is run as the main program, create an instance of the
    Atlas class and call its 'run' method.
    """
    atlas = Atlas()
    atlas.run()
