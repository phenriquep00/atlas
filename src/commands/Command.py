class Command:
    """An interface for creating CLI commands.
    """

    def __init__(self, cli):
        """Initialize a new Command instance.

        Args:
            cli (click.Group): The click command group function that will serve as the entry point for the command.
        """
        self.cli = cli

    def create(self):
        """Create the command object to be executed by the CLI application.

        The `create()` method should be implemented in each subclass to define the command object and its arguments and options.
        """
        pass
