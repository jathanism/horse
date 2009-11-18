
import os, sys
import re
from string import strip

__version__ = '0.0.1'
welcome = 'Welcome to Amazing Horse version %s, what would you like to do?' % __version__
prompt  = '> '
quitters = ('q', 'quit')


COMMANDS = {
    # command: response
    'winky': 'What would you like do to with winky?',
    'tug on winky': "OOH THAT'S DIRTY!",
}

def p():
    print prompt,

def interact():
    cmd = str()
    while not cmd.lower() in quitters:
        if cmd in quitters:
            print 'SHUT UP WOMAN, GET ON MY HORSE!'
            sys.exit(1)

        cmd = raw_input(prompt)
        cmd = strip(cmd)
        ok = validate(cmd)
        if not ok: 
            print "I don't know how to %s" % cmd
            continue
    
    
def validate(cmd):
    if not re.match(r'[a-zA-Z0-9\s]+', cmd): 
        return False

    return True
        
if __name__ == '__main__':
    print welcome
    interact()
