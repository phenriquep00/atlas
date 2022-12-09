# TODO: rewrite this
# Command and it's children classes are used to make the atlas object execute some instruction
#
# ---------------------------------------------------------------------------------------------
#
# Every command has a run() method that is the part will be executed from within atlas
#
# Command objects are constructed in ./data.command_obj_lsit.py and are stores inside the
# commandManager object.
#
# Command objects will have a name attribute, that HAS to be set with the same name as the object itself
# in order to make it reachable in atlas' own run() method.
#
# The flags given to a command are all the possible options that can be passed to it, a good practice is
# to start every flag command with a single "-".
#
# ----------------------------------------------------------------------------------------------
#
# CREATING A COMMAND:
# To create a command following the design utilized over the entire project, please follow this instructions:
# - Ultimatly, a command is a classs that inherits the Command class codded here.
# - after seting up the constructor, the new command class has to overwrite the run() method with the logic
# that it wants to be ran by atlas.
#
# - the validate method can be usto get further control of validating options, in case the command
# has multiple unique flags or subflags that work in a specific way;
# - create a dictionary with the command flags for keys, and flags descriptions for values, this will be automatically formatted
# by the Messanger message() method described in the parent Command class.
# NOTE: ALWAYS CALL THE HELP() METHOD, PASSING THE DICTIONARY AS A ARGUMENT IN ORDER TO GENERATE THE HELP OPTION AND HANDLE IT
# AUTOMATICALLY.
# to generate a custom help documentation, just overwrite the help() method.


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
        for option in options:
            if option not in self.flags:
                Messanger.message(tag="failure", text="invalid option given to this command, check all valid flags with -- <command> -help --")
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


##    add logic here


mockumentation = {"-help": "some usefull text "}


class Test(Command):
    """mock Command for testing"""

    DOCS = mockumentation

    def __init__(self, name, flags):
        super().__init__(name, flags)


    def run(self, options):
        self.validate(options)
        self.help(docs=Test.DOCS, options=options)
        Messanger.message(tag="success", text="the test commnad has been succesfuly ran")