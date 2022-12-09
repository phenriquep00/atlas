from commands.Command import Test
from commands.Help import Help

# objs
#TODO: automate flags creation by getting the flags from the Class.DOCS constant
test = Test(name="test", flags=["-help", "-test"])
help = Help(name="help", flags=["-help"])

command_obj_list = [
    test,
    help,
]

class CommandManager:
    def __init__(self, comands: list):
        self.commands = comands


commandManager = CommandManager(command_obj_list)