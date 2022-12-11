from classes.Messanger import Messanger
from commands.Command import Command


class PasswordGenerator(Command):
    DOCS = {
        "-help": "display password generator usage",
        "-digits": "number of characters to be included in the generated password default: 8",
        "-dontcopy": "copy the password to clipboard",
        "-hide": "down display the generated password",
    }

    def __init__(self, name, flags):
        super().__init__(name, flags)

    def run(self, options):
        self.validate(options=options)
        self.help(docs=PasswordGenerator.DOCS, options=options)
        # validation:
        # if the command was called without flags: just generate a random 8 digit password
        # (number only), copy it to clipboard and display on screen, then finish the execution
        # if it was called with the '-digits' flag with a positive numeric argument: 
        # generate a password with that number of digits, copy it to clipboard, display on screen,
        # then finish 

        if '-digits' in options:
            while ...:
                try:
                    digits = int(input('Number of digits for the newly generated password: '))
                    break
                except ValueError:
                    Messanger.message(tag="failure", text="invalid! use only integer numbers. try again or exit [ctrl + c]")
        Messanger.message(tag="success", text=f"Running password generator with the options: {options}")
