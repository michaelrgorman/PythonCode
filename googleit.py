import webbrowser, sys, pyperclip
if len(sys.argv) > 1:
    # Get search from command line.
    search = ' '.join(sys.argv[1:])
else:
    # Get search from clipboard.
    search = pyperclip.paste()

webbrowser.open('https://www.google.com/search?q=' + search)


