# -*- coding: utf-8 -*-

from albert import *
import os
from time import sleep
from getpass import getuser


__title__ = "Memo"
__version__ = "0.0.1"
__triggers__ = "mm "
__authors__ = "TheRealLorenz"

iconPath = iconLookup("albert")

def handleQuery(query):
    if not query.isTriggered:
        return

    if query.string.startswith("+"):
        return Item(id=__title__,
                    icon=os.path.dirname(__file__)+"/plus.png",
                    text="%s" % query.string.split('+')[1].strip(),
                    subtext="Add item to memo",
                    actions=[ProcAction(text='Add entry',
                                        commandline=['/home/%s/.local/share/albert/org.albert.extension.python/modules/memo/add-item' % getuser(), '%s' % query.string.split('+')[1].strip()],
                                        cwd='/home/%s/.local/share/albert/org.albert.extension.python/modules/memo/' % getuser()
                                        )])

    results = []
    with open('/home/lollo/.local/share/albert/org.albert.extension.python/modules/memo/memo.txt', 'a+') as memfile:
        memfile.seek(0)
        for line in memfile:
            text = line.split('|')[1].strip()
            date = line.split('|')[0].strip()
            item = Item(id=__title__,
                icon=os.path.dirname(__file__)+"/note.png", 
                text=text, 
                subtext=date
                )
            item.actions = [ProcAction(text='Remove entry',
                                        commandline=['/home/%s/.local/share/albert/org.albert.extension.python/modules/memo/rm-item' % getuser(), text],
                                        cwd='/home/%s/.local/share/albert/org.albert.extension.python/modules/memo/' % getuser()
                                        )]
            results.append(item)

    # Api v 0.2
    info(configLocation())
    info(cacheLocation())
    info(dataLocation())

    return results
