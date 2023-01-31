from data.command_obj_list import commandManager
from classes.Messanger import Messanger
import sys


class Atlas:
    """Atlas class to reference the atlas object that is used to run the commands and pluggins"""

    def __init__(self, commands):
        """construct a intance of Atlas class

        Args:
            commands (string): a string with the name of the command to be executed by the atlas object
        """
        self.commands = [_ for _ in commands[1:] if _[0] != "-"]
        self.options = commands[2:]
        self.command = self.validate_arguments()

    def run(self):
        """loops through all the commands from command_obj_list trying to find the matching command to the given interaction,
        in case the command is existent, runs it by calling the Command child object own self.run()"""
        print('running')
        for c in commandManager.commands:
            if c.name == self.command:
                c.run(self.options)

    def validate_arguments(self):
        """method to validate the arguments passed to the atlas object,
        valid arguments are those containing a single command (and it's options) this method tries to check if the
         command is valid by looping through the object list of command and all the valid flags inside all the objects

        Returns:
            command: in case the command and options are valid returns a stripped
            command to be used on the self.run() method
        """
        # check if the atlas keyword was called properly with valid arguments
        if len(self.commands) == 0:
            # if it was called with no arguments, prompt how to check the arguments
            Messanger.message(
                tag="warning",
                text="atlas <command> check usage by typing --atlas help--",
            )

            sys.exit()
        elif len(self.commands) > 1:
            Messanger.message(tag="failure", text="Pass only 1 command at time")
            sys.exit()
        else:
            # if it was called with invalid arguments, prompt to the user the invalid ones
            invalid_commands = [
                _
                for _ in self.commands
                if _ not in [i.name for i in commandManager.commands]
            ]
            if invalid_commands:
                Messanger.message(
                    tag="failure",
                    text=f"invalid command -- {' | '.join(invalid_commands)} --",
                )
                sys.exit()

        return self.commands[0]
