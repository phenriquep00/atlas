from classes.Messanger import Messanger
from commands.Command import Command
import data.command_obj_list as d


class Help(Command):

    DOCS = {
        "-help": "display the documentation for the help command",
    }

    def __init__(self, name, flags):
        super().__init__(name, flags)

    def run(self, options):
        self.validate(options=options)
        self.help(Help.DOCS, options=options)
        Messanger.message(tag="success", text="AVAILABLE COMMANDS\n")
        for command in d.commandManager.commands:
            Messanger.message(
                tag="success",
                text=f"{command.name}:\nflags:\n{list(command.flags)}\n",
            )
