# This file is placed in the Public Domain.
# pylint: disable=C,W0105


"list of commands"


from nixt.main   import Commands
from nixt.object import keys


def cmd(event):
    event.reply(",".join(sorted(keys(Commands.cmds))))
