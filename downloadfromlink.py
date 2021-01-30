import requests, pyperclip, sys, os

os.chdir('C:\\Users\\frank\\Downloads')
resp = requests.get(pyperclip.paste())
name = input('what to name the file: ')
extention = input("what's the extension you want *not required : ")

if resp.status_code != 200:
    sys.exit()

else:
    if not extention:
        ex = int(input('how much is the extention e.g 3 (like png) or 4 like (html): '))
        playFile = open(f'{name}.{pyperclip.paste()[-ex:]}', 'wb')
    else:
        playFile = open(f'{name}.{extention}', 'wb')


    for chunk in resp.iter_content(100000):
        playFile.write(chunk)
    
    playFile.close()