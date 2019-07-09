# password-puller
A simple script written in Python which lets the user copy a password associated with an account to the clipboard. Can be launched via 'Run' in Windows.

# Setting up
1. Download both pw.py and pw.bat and save them in the same location
2. Right click on pw.bat, select 'Edit'. In the first line, make sure the file path leads to pw.py in your computer
3. Edit pw.py. Add your accounts and their corresponding passwords in the dictionary. Do not forget to save.

# Usage
- To use this from desktop, hit 'Windows key + r' to open the run menu. Type in 'pw + (account)' and hit enter.
- You should see a command window open up which says "Password for (account) copied to clipboard."
- Now your password is the last text copied on your clipboard. You can hit 'ctrl + v' to paste it wherever.
- If you run 'pw + (account)' again it will replace the latest password you have saved in the clipboard.

#Limitations
1. You can only have one password per in the clipboard at any time.
2. Your passwords are saved in a .py file which can be edited in a text editor- meaning anyone who finds the file and opens it in edit mode will be able to see them.
