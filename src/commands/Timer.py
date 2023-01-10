from classes.Messanger import Messanger
from commands.Command import Command
from time import sleep


class Timer(Command):
    DOCS = {}

    def __init__(self, name: str, flags):
        super().__init__(name, flags)

    def run(self, options):
        self.validate(options=options)
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

        while t:
            mins, secs = divmod(t, 60)
            timer = f"{mins:02d}:{secs:02d}"
            print(timer, end="\r")
            sleep(1)
            t -= 1

        Messanger.message(tag="success", text="the countdown has succesfully finished")
