from commands.Command import Command


class Help(Command):
    def __init__(self, name, flags):
        super().__init__(name, flags)

    def run(self, options):
        print(f"running Help command with flags: {self.flags}")
        print(f"given flags (options) from terminal were: {options}")