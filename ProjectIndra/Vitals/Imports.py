import os
import os.path
import shutil
import time
import random
import sys
import numpy
import PIL
from pathlib import Path
from time import ctime
if sys.version_info < (3, 0):
    import Tkinter as tk
else:
    import tkinter as tk
    from tkinter import *
    from PIL import ImageTk,Image
