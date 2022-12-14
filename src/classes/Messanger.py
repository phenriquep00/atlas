import sys
from colorama import Fore


class Messanger:

    TAGS = ["success", "failure", "warning", "hint", "help"]

    @staticmethod
    def message(text:str, tag:str, command_documentation=dict()):
        """display a message in the terminal with a custom formatting based on the tag given

        Args:
            text (_type_): text to be displayed
            tag (_type_): type of message to display:
                possible tags are: success | failure | warning | hint | help
        """
        if tag not in [_ for _ in Messanger.TAGS]:
            # if the tag is not available
            print("MessagerTagError: invalid tag")
            sys.exit()

        if tag == "success":
            # checks if the tag represents a sucess message
            print(Fore.GREEN + text + Fore.RESET)
        elif tag == "failure":
            # check if the tag represents a failure message
            print(Fore.RED + f"ERROR\n{text}" + Fore.RESET)
        elif tag == "warning":
            # check if the tag represents a warning message
            print(Fore.YELLOW + text + Fore.RESET)
        elif tag == "hint":
            # check if the tag represents a hinting message
            print(Fore.CYAN + text + Fore.RESET)
        elif tag == "help":
            # check if the tag represents a help message
            #TODO: format the command_documentation
            print(Fore.BLUE + f"HELP\n{text}" + Fore.RESET)
            print(command_documentation)