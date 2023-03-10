class Command:
    """Command interface 
    """
    def __init__(self, cli):
        """instance initializer

        Args:
            cli (clicker command group): the clicker command group function
        """
        self.cli = cli

    def create(self):
        """create the command object to be executed at atlas.py
        the definition of arguments and options go in here before the function to be executed
        """
        pass
