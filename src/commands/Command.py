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
# - the validate method can be overwritten to get further control of validating options, in case the command
# has multiple unique flags or subflags that work in a specific way;
#
# --------------------------------------------------------------------------------------------- 
#
# A good practice is to create a -help flag to every custom command using the Messanger class with the "help"
# tag to document how the command works and how it's flags should be used


class Command:
    def __init__(self, name, flags):
        self.name = name
        self.flags = flags

    def run(self):
        pass

    def validate(self):
        pass


class Test(Command):
    """mock Command for testing

    Args:
        Command (_type_): _description_
    """

    def __init__(self, name, flags):
        super().__init__(name, flags)

    def run(self, options):
        print(
            f"running --test-- command. This command has the following flags: {self.flags}"
        )
        print(f"the given options (flags) from terminal were: {options}")
