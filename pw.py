#! python3
# pw.py - a basic password locker program

PASSWORDS = {'facebook': 'fb123',
             'twitter': 'twitter123',
             'instagram': 'insta123'}
# Add the accounts and their corresponding passwords in the dictionary above.

import sys, pyperclip
if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)
        
