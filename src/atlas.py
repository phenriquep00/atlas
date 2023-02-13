from optparse import OptionParser

from commands.greet import Greet
from commands.youtube_downloader import YoutubeDownloader

# TODO: find a way to check if the command was parsed with a option

class Atlas:
    """
    The Atlas class represents the virtual assistant, and provides
    the functionality for greeting the user, displaying the version
    and help information, and executing other commands.
    """

    def __init__(self):
        """
        Initialize an instance of the Atlas class by creating an
        OptionParser object and an instance of the Greet class.
        """
        self.parser = OptionParser()
        self.commands = {
            "--hello": Greet(name='--hello', help="show a greeting message to the user"),
            "--download": YoutubeDownloader(name="--download", help="download videos from YouTube by passing a video URL as option for this command")
        }

    def run(self):
        """
        Run the virtual assistant and handle the command line arguments.
        """
        # Add the options based on the commands dictionary
        for name, cmd in self.commands.items():
            self.parser.add_option(
                name, dest=name, action="store_true", help=cmd.help)

        # Add the '--version' option
        self.parser.add_option("-v", "--version", dest="version",
                               action="store_true",
                               help="display the version of Atlas")

        # Parse the command line arguments
        (options, args) = self.parser.parse_args()

        # If the number of arguments is incorrect, display an error message
        if len(args) != 0:
            self.parser.error(
                "Too many arguments. Use 'atlas --help' for usage information.")

        # loop through the command dictionary and check if this command has been called by the atlas via optparse's options
        for name, cmd in self.commands.items():
            # FIXME: not working if i have more than 1 command in the command dictionary
            if getattr(options, name):
                cmd.run()

            # If the '--version' option is specified, display the version
            elif options.version:
                print("Atlas version 1.0.0")

            # If no options are specified, display an error message
            else:
                self.parser.error(
                    "Please specify a command. Use 'atlas --help' to see available commands.")


if __name__ == "__main__":
    """
    If the script is run as the main program, create an instance of the
    Atlas class and call its 'run' method.
    """
    atlas = Atlas()
    atlas.run()
