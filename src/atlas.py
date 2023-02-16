from optparse import OptionParser
from commands.greet import Greet
from commands.youtube_downloader import YoutubeDownloader

class Atlas:
    """
    A command-line utility for various tasks.

    This utility provides a few different commands to perform various tasks.
    """
    def __init__(self):
        """
        Initializes the Atlas command-line utility.

        This method sets up the OptionParser object and adds the available commands to it.
        """
        # Initialize the OptionParser object
        self.parser = OptionParser()
        
        # Define the available commands with their respective names and help messages
        self.commands = {
            "--hello": Greet(name='--hello', help="show a greeting message to the user"),
            "--download": YoutubeDownloader(name="--download", help="download videos from YouTube by passing a video URL as option for this command")
        }
        
        # Add the '--version' option to the OptionParser object
        self.parser.add_option("-v", "--version", dest="version",
                               action="store_true",
                               help="display the version of Atlas")
        
        # Add the '--hello' option to the OptionParser object
        self.parser.add_option("--hello", dest="hello",
                               action="store_true",
                               help="show a greeting message to the user")
        
        # Add the '--download' option to the OptionParser object
        self.parser.add_option("--download", dest="download",
                               help="download videos from YouTube by passing a video URL as option for this command")

    def run(self):
        """
        Runs the Atlas command-line utility.

        This method parses the command line arguments and runs the appropriate command based on the options specified.
        """
        # Parse the command line arguments
        (options, args) = self.parser.parse_args()

        # If the '--version' option is specified, display the version
        if options.version:
            print("Atlas version 1.0.0")
        
        # If the '--hello' option is specified, run the corresponding command
        if options.hello:
            self.commands["--hello"].run()
        
        # If the '--download' option is specified, run the corresponding command
        if options.download:
            self.commands["--download"].run()
        
        # If no options are specified, display an error message
        else:
            self.parser.error("Please specify a command. Use 'atlas --help' to see available commands.")

# If the script is run as the main program, create an instance of the Atlas class and call its 'run' method.
if __name__ == "__main__":
    atlas = Atlas()
    atlas.run()
