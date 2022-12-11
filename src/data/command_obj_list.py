from commands.Command import Test
from commands.Help import Help
from commands.PasswordGenerator import PasswordGenerator

# objs
test = Test(name="test", flags=Test.DOCS.keys())
help = Help(name="help", flags=Help.DOCS.keys())
pass_gen = PasswordGenerator(
    name="pass_gen", flags=PasswordGenerator.DOCS.keys()
)

command_obj_list = [
    test,
    help,
    pass_gen,
]


class CommandManager:
    def __init__(self, comands: list):
        self.commands = comands


commandManager = CommandManager(command_obj_list)
