# coding: utf-8
import shutil
import os,sys
import PyInstaller.__main__
import glob
import site
import subprocess

filepath = "main.py"
version = "1.0"

basepath = site.getsitepackages()[1] + r"\ffmpeg"
if os.path.exists(basepath):
    for file in glob.glob("build_need/noconcole-files/*"):
        try:
            os.remove(basepath + "\\" + os.path.basename(file))
        except:
            pass
        try:
            shutil.copyfile(file, basepath + "\\" + os.path.basename(file))
        except:
            pass

try:
    shutil.rmtree("dist")
except:
    pass

PyInstaller.__main__.run([
    filepath,
    '--windowed',
    "--additional-hooks-dir=./build_need",
    "--icon=./build_need/aymgv-10e4t-001.ico"
])

outdir = f"dist\\{os.path.splitext(os.path.basename(filepath))[0]}"
try:
    shutil.copytree("build_need\\bin",os.path.join(outdir,"bin"))
except:
    pass

outdir = f"dist\\{os.path.splitext(os.path.basename(filepath))[0]}\\ライセンス文章"
copypath = "build_need\\ライセンス文章"
try:
    shutil.copytree(copypath,outdir)
except:
    pass

try:
    subprocess.Popen(["explorer.exe",os.path.abspath(f"dist\\{os.path.splitext(os.path.basename(filepath))[0]}")])
except:
    pass