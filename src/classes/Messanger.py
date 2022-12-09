import sys
from colorama import Fore


class Messanger:

    TAGS = ["sucess", "failure", "warning", "hint"]

    @staticmethod
    def message(text, tag):
        """display a message in the terminal with a custom formatting based on the tag given

        Args:
            text (_type_): text to be displayed
            tag (_type_): type of message to display:
                possible tags are: sucess | failure | warning
        """
        if tag not in [_ for _ in Messanger.TAGS]:
            # if the tag is not available
            print("MessagerTagError: invalid tag")
            sys.exit()

        if tag == "sucess":
            # checks if the tag represents a sucess message
            print(Fore.GREEN + f"SUCESS\n{text}")
        elif tag == "failure":
            # check if the tag represents a failure message
            print(Fore.RED + f"ERROR\n{text}")
        elif tag == "warning":
            # check if the tag represents a warning message
            print(Fore.YELLOW + f"WARNING\n{text}")
        elif tag == "hint":
            # check if the tag represents a hinting message
            print(Fore.CYAN + f"HINT\n{text}")
