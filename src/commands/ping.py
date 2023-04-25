import subprocess
from Command import Command


class Ping(Command):
    def __init__(self, cli):
        super().__init__(cli)

    def create(self):
        @self.cli.command(help="internet connection test")
        def ping():
            # Snippet from https://medium.com/@networksuatomation/python-ping-an-ip-adress-663ed902e051
            host = "www.google.com"  # Hosts list

            ping_test = subprocess.call(
                'ping %s -n 2' % host)  # Ping host n times
            if ping_test == 0:  # If ping test is 0, it' reachable
                print("google.com domain is reachable")
            else:
                print("google.com domain is not reachable")
