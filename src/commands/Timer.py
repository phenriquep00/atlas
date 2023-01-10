from classes.Messanger import Messanger
from commands.Command import Command
from time import sleep


class Timer(Command):
    """ Timer class to implement the timer command used by atlas
    this command has the responsability to implement time related functions

    Args:
        Command (Command): super class
    """
    DOCS = {
        "-help": "the timer command can be used for opperations with time, right now, the only usability available is the countdown function"
    }

    def __init__(self, name: str, flags: list):
        """class constructor

        Args:
            name (str): name of the command to be called with atlas 
            flags (list): list of possible options to be used with this command
        """
        super().__init__(name, flags)

    def run(self, options):
        """
        run the implementation of this command 

        Args:
            options (_type_): given options when the command was called with atlas
        """
        # validade the flags comparing them with the available options
        self.validate(options=options)
        # in case the -help option was called, runs this method and displays the ocmmand usability
        self.help(docs=Timer.DOCS, options=options)

        # command execution goes here

        # aks for the user the amount os time (in seconds) to countdown
        while ...:
            try:
                t = int(input("enter the time to countdown (in seconds): \n"))
                break
            except ValueError:
                Messanger.message(
                    tag="failure",
                    text="invalid! use only integer numbers. try again or exit [ctrl + c]",
                )

        # start the countdown loop
        while t:
            mins, secs = divmod(t, 60)
            timer = f"{mins:02d}:{secs:02d}"
            print(timer, end="\r")
            sleep(1)
            t -= 1

        # display that the command has been completed without errors
        Messanger.message(tag="success", text="the countdown has succesfully finished")
