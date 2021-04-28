# -*- coding: utf-8 -*-

from albert import *
import os
from time import sleep
from getpass import getuser


__title__ = "Memo"
__version__ = "0.0.3"
__triggers__ = "mm "
__authors__ = "TheRealLorenz"

iconPath = iconLookup("albert")

def handleQuery(query):
    if not query.isTriggered:
        return

    if query.string.startswith("+"):
        return Item(id=__title__,
                    icon=os.path.dirname(__file__)+"/plus.png",
                    text="<b>%s</b>" % query.string.split('+')[1].strip(),
                    subtext="<i>Add item to memo</i>",
                    actions=[ProcAction(text='Add entry',
                                        commandline=[os.path.dirname(__file__)+'/add-item', '%s' % query.string.split('+')[1].strip()],
                                        cwd=os.path.dirname(__file__)
                                        )])

    results = []
    with open(os.path.dirname(__file__)+'/memo.txt', 'a+') as memfile:
        memfile.seek(0)
        text = '||'
        for line in memfile:
            text = line.split('|')[1].strip()
            date = line.split('|')[0].strip()
            item = Item(id=__title__,
                icon=os.path.dirname(__file__)+"/note.png", 
                text=text, 
                subtext="<i>%s</i>" % date
                )
            item.actions = [ProcAction(text='Remove entry',
                                        commandline=[os.path.dirname(__file__)+'/rm-item', text],
                                        cwd=os.path.dirname(__file__)
                                        )]
            results.append(item)

        if text == '||':
            item = Item(
                    id=__title__,
                    icon=os.path.dirname(__file__)+"/note.png",
                    text='<b>Empty tasklist</b>',
                    subtext="<i>Type </i><b>'+'</b><i> and the task you want to add</i>"
                    )
            results.append(item)

    # Api v 0.2
    info(configLocation())
    info(cacheLocation())
    info(dataLocation())

    return results
