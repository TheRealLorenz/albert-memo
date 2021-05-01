# -*- coding: utf-8 -*-

from albert import *
import os
from time import sleep
from getpass import getuser


__title__ = "Notes"
__version__ = "0.0.4"
__triggers__ = "nt "
__authors__ = "TheRealLorenz"

iconPath = iconLookup("albert")

def handleQuery(query):
    if not query.isTriggered:
        return

    if query.string.startswith("+"):
        if ' x ' in query.string:
            substr = ' > %s' % query.string.split(' x ')[-1].strip()
            action = [ProcAction(text='Add entry',
                                        commandline=[os.path.dirname(__file__)+'/add-item', 
                                                    '%s' % query.string.split('+')[1].split(' x ')[0].strip(),
                                                    '%s' % query.string.split(' x ')[-1].strip()],
                                        cwd=os.path.dirname(__file__)
                                        )]
        else:
            substr = ' > ∞'
            action = [ProcAction(text='Add entry',
                                        commandline=[os.path.dirname(__file__)+'/add-item', 
                                                    '%s' % query.string.split('+')[1].strip(),
                                                    ''],
                                        cwd=os.path.dirname(__file__)
                                        )]
        return Item(id=__title__,
                    icon=os.path.dirname(__file__)+"/plus.png",
                    text="<b>%s</b>" % query.string.split('+')[1].strip(),
                    subtext="<i>Add note</i>" + substr,
                    actions=action)

    results = []
    with open(os.path.dirname(__file__)+'/notes.txt', 'a+') as memfile:
        memfile.seek(0)
        text = '||'
        for line in memfile:
            text = line.split('|')[1].strip()
            date = line.split('|')[0].strip()
            subdate = ' > ' + line.split('|')[-1].strip()
            item = Item(id=__title__,
                icon=os.path.dirname(__file__)+"/note.png", 
                text=text, 
                subtext="<i>%s</i><b>%s</b>" % (date, subdate)
                )
            item.actions = [ProcAction(text='Remove note',
                                        commandline=[os.path.dirname(__file__)+'/rm-item', text],
                                        cwd=os.path.dirname(__file__)
                                        )]
            results.append(item)

        if text == '||':
            item = Item(
                    id=__title__,
                    icon=os.path.dirname(__file__)+"/note.png",
                    text='<b>Empty notes</b>',
                    subtext="<i>Type </i><b>'+'</b><i> and the note you want to add</i>"
                    )
            results.append(item)

    # Api v 0.2
    info(configLocation())
    info(cacheLocation())
    info(dataLocation())

    return results
