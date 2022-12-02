from data.command_obj_list import command_obj_list
import sys


def flatten(l):
    return [item for sublist in l for item in sublist]


class Atlas:
    def __init__(self, commands):
        self.commands = [_ for _ in commands[1:] if _[0] != "-"]
        self.flags = commands[2:]
        self.command = self.validate_arguments()
        

    def run(self):
        for c in command_obj_list:
            if c.name == self.command:
                c.run(self.flags)

    def validate_arguments(self):
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
                _ for _ in self.commands if _ not in [i.name for i in command_obj_list]
            ]
            if invalid_commands:
                print(f"invalid command -- {' | '.join(invalid_commands)} --")
                sys.exit()

            invalid_flags = [
                _ for _ in self.flags if _ not in flatten([_.flags for _ in command_obj_list])
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
