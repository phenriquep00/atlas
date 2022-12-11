# Command and it's children classes are used to make the atlas object execute some instruction
#
# ---------------------------------------------------------------------------------------------
#
# HOW TO CREATE A COMMAND:
# - create a new class inheting the Command class defined in this file
# - this new class (command) should have 2 parameters: a name and a list of flags
# NOTE: a command name MUST match ist object instanced in data.command_obj_list.py in order for it to be
# correctly executed inside atlas
# NOTE: the list of flags MUST include at least 1 flag: "-help"
# a command must also have a Documentation constant in the shape of a dictionary
# this constant will be used in the help() method that documentates it's usage
# the disctionary keys will resamble the  command flags (ALWAYS STARTING WITH "-")
# and it's values will be the usage description for the flag
#
# The run() method is where the logic to be executed by atlas will be implemented
# the first two lines will be self.validate() and self.help()
# self.validate() comes from the Command class, and check if the options takem from atlas arguments are
# valid, if not, end the process.
# self.help() checks if the -help flag was given as a option in the atlas arguments, if so, displays to the
# user the list of flags for this command, and hows him the documentation.
#
# EXEMPLE OF IMPLEMENTATION
# class Exemple(Command):
#
#   DOCS = {
#      "-help": "display exemple command usage",
#     "-blablabla": "some description",
#    "-and_so_on": "and so forth",
# }
#
#   def __init__(self, name:str, flags:list):
#      super().__init__(name, flags)
#
#   def run(self, options):
#      self.validate(options=options)
#      self.help(docs=self.DOCS, options=options)
#
#      =-~=-~THE COMMAND LOGIC GOES HERE ~-=~-=
#
# NOTE: the self.validate() but it's not recommended, since it is the only bit of code that actually checks
# if the flags are valid. If you do want more control of the validation method, I recommend the implementation of
# a new method that runs the self.validate() within it,or just adding your custom validation inside the self.run()
#
# NOTE: the self.help() method can also be overwritten, and it is also not recommended, the self.help() method
# generates automatically a nicely formatted usage documentation based on the DOCS constant, overwriting it will make
# your custom command lose the design that all the others have.


import sys
from classes.Messanger import Messanger


class Command:
    def __init__(self, name: str, flags: list):
        """Command constructor method

        Args:
            name (string): name of the command NOTE: FOR THE COMMAND TO BE EXECUTED, THIS ATTRIBUTING THE CLASS (A TEST COMMAND HAS TO HAVE IT'S NAME ATTRIBUTE SET TO TEST, FOR EXEMPLE)
            flags (list): flags are all the possible options that can be passed to execute the command via atlas run()
        """
        self.name = name
        self.flags = flags

    def validate(self, options: list):
        """method to check if the options where correctly used in order to make the command function properly

        Args:
            options (list): options passed as sys.args within the atlas command
        """
        #TODO: change this method to check if the given option STARTSWITH a flag
        # this change is necessary in order to add arguments to flags that need custom inputs
        for option in options:
            if option not in self.flags:
                Messanger.message(
                    tag="failure",
                    text="invalid option given to this command, check all valid flags with -- <command> -help --",
                )
                sys.exit()
        pass

    def help(self, docs: dict, options: list):
        """method that displays the usage documentation for a given method

        Args:
            docs (dict): description of every flag that the command has, using flag names for eys and describion it in the values
            options (list): options passed as sys.args within the atlas command
        """
        if "-help" in options:
            # check if the -help option was invoked
            Messanger.message(
                tag="help",
                text=f"usage for {self.name} command\n",
                command_documentation=docs,
            )
            sys.exit()

    def run(self, options):
        """implements the logic to be run by atlas"""
        self.help(dict(), options)


###### add logic here


mockumentation = {"-help": "some usefull text ", "-test": "aaaaaaaaaaaaaaaaaa"}


class Test(Command):
    """mock Command for testing"""

    DOCS = mockumentation

    def __init__(self, name, flags):
        super().__init__(name, flags)

    def run(self, options):
        self.validate(options)
        self.help(docs=Test.DOCS, options=options)
        Messanger.message(
            tag="success", text="the test commnad has been succesfuly ran"
        )
