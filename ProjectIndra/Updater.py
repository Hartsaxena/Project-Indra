# This is an Updater program that executes when you decide to Update the game
# Only execute and/or edit this program sparingly, or else you could seriously break Something
# This took me so long to debug...


import git
import time
import shutil
import os
from os import getcwd
import os.path
import requests
from pathlib import Path
yesno = input("Are you sure? doing this will update the game to the current\nversion (In the github page). This will also reset the game.\nIn order to save progress, make a copy of the 'saves' file\nthat can be found in the Saves folder in the ProjectIndra folder.\n[y/n]\n")
if yesno.lower() == 'yes' or yesno.lower() == 'y' or yesno.lower() == 'yep':
    print("Ok!")
    time.sleep(1)
    print("Warning! Don't terminate this program while this is being run.\nDoing so can and most likely will\ncause serious problems.")
    print("Checking if a Download folder currently exists...")
    if os.path.exists(Path.home()/"Documents/ProjectIndra"):
        print ("Deleting Download Folder...")
        shutil.rmtree(Path.home()/"Documents/ProjectIndra")
    print("Removing old files...")
    if os.path.exists(Path.home()/"Documents/Indra.py")==True:
        try:
            os.remove(Path.home()/"Documents/Indra.py")
        except PermissionError:
            shutil.rmtree(Path.home()/"Documents/Indra.py")
    print("Downloading most recent version of Project Indra...")
    git.Git(Path.home()/"Documents").clone("https://github.com/Hartsaxena/ProjectIndra.git")
    url = 'https://raw.githubusercontent.com/Hartsaxena/Project-Indra/master/Indra.py'
    r = requests.get(url, allow_redirects=True)
    open(Path.home()/"Documents/Indra.py", 'wb').write(r.content)
    # git.Git(Path.home()/"Documents").clone("https://github.com/Hartsaxena/Indra.py.git")
    print("Removing Useless files...")
    if os.path.exists(Path.home()/"Documents/LICENSE") == True:
        os.remove(Path.home()/"Documents/LICENSE")
    if os.path.exists(Path.home()/"Documents/README.md") == True:
        os.remove(Path.home()/"Documents/README.md")

    print ("Done!")
