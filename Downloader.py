# This is the temporary downloader for Project Indra
# Only execute and/or edit this program sparingly, or else you could seriously break Something
# This took me so long to debug...
# Once I turn the program into an app, this program will be discarded and replaced with a .zip or a .dmg file.
# I created this because I can't get py2app to work for some reason.


import git
import time
import shutil
import os
from os import getcwd
import os.path
import requests
from pathlib import Path

print ("Downloading Project Indra...")
try:
    time.sleep(1)
    print("Warning! Don't terminate this program while this is being run.\nDoing so can and most likely will cause serious problems.")
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
except:
    print ("Sorry, something went wrong and the downloader wasn't able to fully download the Project.")
