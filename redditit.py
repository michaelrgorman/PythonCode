import webbrowser, sys, pyperclip
if len(sys.argv) > 1:
    # Get address from command line.
    search = ' '.join(sys.argv[1:])
else:
    # Get address from clipboard.
    search = pyperclip.paste()

webbrowser.open('https://www.reddit.com/search/?q=' + search)
