class Command:
    def __init__(self, name, flags):
        self.name = name
        self.flags = flags

    def run(self):
        pass


class Test(Command):
    def __init__(self, name, flags):
        super().__init__(name, flags)

    def run(self, options):
        print(f"running Test command with flags: {self.flags}")
        print(f"given flags (options) from terminal were: {options}")
