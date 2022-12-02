from commands.Command import Command


class Help(Command):
    def __init__(self, name, flags):
        super().__init__(name, flags)

    def run(self, options):
        print(f"running --help-- command. This command has the following flags: {self.flags}")
        print(f"the given options (flags) from terminal were: {options}")