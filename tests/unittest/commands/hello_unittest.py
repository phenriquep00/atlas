import unittest
from click.testing import CliRunner

from atlas.src.commands.hello import Hello



class TestHello(unittest.TestCase):
    def setUp(self):
        self.runner = CliRunner()
        self.command = Hello(cli=None)
        self.command.create()

    def test_hello_default(self):
        result = self.runner.invoke(self.command.cli, ['hello'])
        self.assertEqual(result.exit_code, 0)
        self.assertEqual(result.output.strip(), 'Hello there')

    def test_hello_pt(self):
        result = self.runner.invoke(self.command.cli, ['hello', '--lang', 'pt'])
        self.assertEqual(result.exit_code, 0)
        self.assertEqual(result.output.strip(), 'Olá')


if __name__ == '__main__':
    unittest.main()
