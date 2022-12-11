from classes.Messanger import Messanger
from commands.Command import Command
import secrets
import string
import pyperclip


class PasswordGenerator(Command):
    DOCS = {
        "-help": "display password generator usage",
        "-len": "number of characters to be included in the generated password default: 12",
        "-dontcopy": "copy the password to clipboard",
        "-hide": "down display the generated password",
    }

    def __init__(self, name, flags):
        super().__init__(name, flags)

    def run(self, options):
        self.validate(options=options)
        self.help(docs=PasswordGenerator.DOCS, options=options)
        
        # TODO:
        # for now, all passwords will contain letters, digits and special chars
        # but the user will have a chance to customize it in the future

        letters = string.ascii_letters
        digits = string.digits
        special_chars = string.punctuation

        valid_chars = letters + digits + special_chars

        def generate(length: int):
            pwd = ''

            for i in range(length):
                pwd += ''.join(secrets.choice(valid_chars))
            return pwd

        if '-len' in options:
            # check if the user typed the -digits flag, if so, ask a input for a custon value for the password to be generated
            while ...:
                try:
                    pwd_length = int(input('Number of digits for the newly generated password: '))

                    break
                except ValueError:
                    Messanger.message(tag="failure", text="invalid! use only integer numbers. try again or exit [ctrl + c]")
        else:
            Messanger.message(tag="hint", text='generating a 12 digit password')
            pwd_length = 12
        
        # generate a password:
        password = generate(pwd_length)

        if '-dontcopy' in options:
            pass
        else:
            pyperclip.copy(password)

        if "-hide" in options:
            pass
        else:
            print(password)

        Messanger.message(tag="success", text="Password succesfully generated")
