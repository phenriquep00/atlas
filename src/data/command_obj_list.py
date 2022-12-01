from commands.Command import Test
from commands.Help import Help

# objs
test = Test(name="test", flags=["-help, -test"])
help = Help(name="help", flags=["-help, -test"])

command_obj_list = [
    test,
    help,
]
