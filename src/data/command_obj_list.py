from commands.Command import Test
from commands.Help import Help

# objs
test = Test(name="test", flags=Test.DOCS.keys())
help = Help(name="help", flags=Help.DOCS.keys())

command_obj_list = [
    test,
    help,
]

class CommandManager:
    def __init__(self, comands: list):
        self.commands = comands


commandManager = CommandManager(command_obj_list)