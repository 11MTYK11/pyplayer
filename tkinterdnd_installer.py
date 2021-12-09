import os
import sys
import shutil
import subprocess

def resourcePath(filename):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, filename)
    return os.path.join(filename)

try:
    shutil.copytree(resourcePath("tkinter_dnd_files\\tkdnd2.8"),sys.exec_prefix + "\\tcl\\tkdnd2.8")
except:
    import traceback
    traceback.print_exc()

os.chdir(resourcePath("tkinter_dnd_files\\tkinterdnd2-master"))
try:
    subprocess.run(["python","setup.py","install"],shell=True)
except:
    import traceback
    traceback.print_exc()
