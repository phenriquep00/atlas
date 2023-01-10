from commands.Command import Test
from commands.Help import Help
from commands.PasswordGenerator import PasswordGenerator
from commands.WikipediaEntry import WikipediaEntry
from commands.Vocab import Vocab
from commands.Timer import Timer

# objs
test = Test(name="test", flags=Test.DOCS.keys())
help = Help(name="help", flags=Help.DOCS.keys())
pass_gen = PasswordGenerator(name="pass_gen", flags=PasswordGenerator.DOCS.keys())
vocab = Vocab(name="vocab", flags=Vocab.DOCS.keys())
timer = Timer(name="timer", flags=Timer.DOCS.keys())
wiki_entry = WikipediaEntry(name="wikientry", flags=WikipediaEntry.DOCS.keys())

command_obj_list = [
    test,
    help,
    pass_gen,
    vocab,
    timer,
    wiki_entry,
]


class CommandManager:
    def __init__(self, comands: list):
        self.commands = comands


commandManager = CommandManager(command_obj_list)
