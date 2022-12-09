from data.command_obj_list import commandManager
import sys


def flatten(l):
    """transforms a list of lists in a single list 

    Args:
        l (list): a list object, populated with other lists

    Returns:
        list: returns a single list with separetted items
    """
    return [item for sublist in l for item in sublist]


class Atlas:
    """Atlas class to reference the atlas object that is used to run the commands 
    and pluggins
    """
    def __init__(self, commands):
        """construct a object

        Args:
            commands (string): a string with the name of the command to be executed by the atlas object
        """
        self.commands = [_ for _ in commands[1:] if _[0] != "-"]
        self.flags = commands[2:]
        self.command = self.validate_arguments()
        

    def run(self):
        """loops through all the commands from command_obj_list trying to find
        the matching command to the given interaction, in case the command is existent, runs it by
        calling the Command child object own self.run()
        """
        for c in commandManager.commands:
            if c.name == self.command:
                c.run(self.flags)

    def validate_arguments(self):
        """method to validate the arguments passed to the atlas object, 
        valid arguments are those containing a single command (and it's flags)
        this method tries to check if the command is valid by looping through the
        object list of command and all the valid flags inside all the objects

        Returns:
            command: in case the command and flags are valid returns a stripped 
            command to be used on the self.run() method
        """
        # TODO: change validation by using the command_obj_list
        # check if the atlas keyword was called properly with valid arguments
        if len(self.commands) == 0:
            # if it was called with no arguments, prompt how to check the arguments
            print("atlas <command> \ncheck commands using --atlas help--")
            sys.exit()
        elif len(self.commands) > 1:
            print("pass only one command at time")
            sys.exit()
        else:
            # if it was called with invalid arguments, prompt to the user the invalid ones
            invalid_commands = [
                _ for _ in self.commands if _ not in [i.name for i in commandManager.commands]
            ]
            if invalid_commands:
                print(f"invalid command -- {' | '.join(invalid_commands)} --")
                sys.exit()

            invalid_flags = [
                _ for _ in self.flags if _ not in flatten([_.flags for _ in commandManager.commands])
            ]


            if invalid_flags:
                print(
                    f"invalid flags for command {self.commands[0]} found at -- {' | '.join(invalid_flags)} --"
                )
                print(
                    f"check valid flags for {self.commands[0]} with -- atlas help -{self.commands[0]} --"
                )
                sys.exit()
        return self.commands[0]
