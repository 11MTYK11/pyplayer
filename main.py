import tkinter as tk
import tkinterdnd2
import base64

root = tkinterdnd2.Tk()
#root.resizable(0,0)
root.title("音楽プレイヤー")
root.attributes("-topmost",True)
root.withdraw()

dlwin = tk.Toplevel(root)
dlwin.attributes("-topmost",True)
dlwin.overrideredirect(1)
dlwin.title("ロード中...")
wsize = 350
hsize = 300
xplace = int(root.winfo_screenwidth()/2)-int(wsize/2)
yplace = int(root.winfo_screenheight()/2)-int(hsize/2)
dlwin.geometry(f"{wsize}x{hsize}+{xplace}+{yplace}")
imglbl = tk.Label(dlwin)
imglbl.pack(fill=tk.BOTH,expand=True)
readimg = tk.PhotoImage(data=base64.b64decode("""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"""))
imglbl.config(image=readimg)
imglbl.img = readimg

dlwin.update()

from genericpath import exists
import random
import subprocess
import sys
from tkinter.font import families
import mouse
from tkinter import ttk
import time
import pygame.mixer
import threading
from tkinter import filedialog
import glob
import os
import datetime
from tkinter import messagebox
import base64
import shutil
import keyboard
from tkinter import simpledialog
import configparser
from tinytag import TinyTag
import webbrowser
import datetime
from tkinter import scrolledtext
import cv2
from PIL import ImageTk, Image
import tkinter
import pygame
import ffmpeg
import youtube_dl
import numpy as np
import json,uuid
import zlib,queue
import urllib.request

youtube_dlurl = "https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp.exe"
save_path = os.path.join(os.path.dirname(sys.argv[0]),"bin\\yt-dlp.exe")
if os.path.exists(save_path):
    pass
else:
    data = urllib.request.urlopen(youtube_dlurl).read()
    with open(save_path, mode="wb") as file:
        file.write(data)

#audio のクラス
class Audio():
    def __init__(self):
        pass
    def openfile(self, filepath):
        count = 0
        for flist in glob.glob("tempfile/audio/*.mp3"):
            try:
                os.remove(flist)
            except:
                pass
        try:
            os.makedirs("tempfile/audio")
        except:
            pass
        while True:
            self.title = "tempfile/audio/tempfile-" + str(count) + ".mp3"
            if os.path.exists(self.title):
                pass
            else:
                break
            count = count + 1
        try:
            videopath = filepath
            audiopath = self.title
            stream = ffmpeg.input(videopath)
            stream = ffmpeg.output(stream, audiopath,format="mp3")
            ffmpeg.run(stream,cmd=os.path.join(os.path.dirname(sys.argv[0]),"bin\\ffmpeg.exe"))
        except:
            pass
        try:
            pygame.mixer.init()
        except:
            pass
        pygame.mixer.music.load(self.title)
    def playth(self):
        pygame.mixer.music.play(1,0)
    def audioplay(self, place=0):
        self.playthread = threading.Thread(target=self.playth)
        self.playthread.setDaemon(True)
        self.playthread.start()
    def stop(self):
        try:
            pygame.mixer.music.stop()
            pygame.mixer.music.unload()
        except:
            pass
        try:
            os.remove(self.title)
        except:
            pass
        try:
            self.playthread.stop()
        except:
            pass
    def seek(self,time):
        try:
            pygame.mixer.music.stop()
        except:
            pass
        try:
            pygame.mixer.music.play(1,int(time))
        except:
            pass
    def pause(self):
        pygame.mixer.music.pause()
    def unpause(self):
        pygame.mixer.music.unpause()
    def setvolume(self,volume):
        try:
            pygame.mixer.music.set_volume(volume)
        except:
            pass
    def getpos(self):
        try:
            return pygame.mixer.music.get_pos()
        except:
            pass
#video のクラス
class Video():
    def __init__(self):
        self.widthsize = 500
        self.heightsize = 300
        self.readset = True
        self.endset = False
        self.threadrunset = True
    def openfile(self, file_path,frame):
        self.frame = frame
        self.readset = False
        self.endset = True
        try:
            self.videoreader = cv2.VideoCapture(file_path)
        except:
            pass
    def play(self):
        self.readset = True
        self.endset = False
        self.threadrunset = True
        self.video_thread = threading.Thread(target=self._stream)
        self.video_thread.setDaemon(True)
        self.video_thread.start()
    def _stream(self):
        start_time=time.time()
        try:
            sleeptime = 1/self.videoreader.get(cv2.CAP_PROP_FPS)
        except:
            return False
        self.FPS = self.videoreader.get(cv2.CAP_PROP_FPS)
        self.frame_now = 0
        while True:
            try:
                if self.endset:
                    break
                ftime = time.time()
                self.frame_now = self.frame_now + 1
                if self.readset:
                    if self.endset:
                        break
                    else:
                        ret,image = self.videoreader.read()
                if self.frame_now*sleeptime >= time.time()-start_time:
                    try:
                        image = cv2.resize(image,(moviewindow.winfo_width(),moviewindow.winfo_height()))
                        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                    except:
                        self.videoreader.set(cv2.CAP_PROP_FRAME_COUNT,0)
                        self.videoreader.set(cv2.CAP_PROP_POS_MSEC,0)
                        break
                    if self.readset:
                        if self.endset:
                            break
                        else:
                            frame_image = ImageTk.PhotoImage(Image.fromarray(image))
                            self.frame.config(image=frame_image)
                            self.frame.image = frame_image
                    time.sleep(max(0,sleeptime-(time.time()-ftime)))
                else:
                    pass
            except:
                break
        self.threadrunset = False
    def sizechange(self,wsize,hsize):
        self.widthsize = wsize
        self.heightsize = hsize
    def seek(self,time):
        self.readset = False
        self.videoreader.set(cv2.CAP_PROP_POS_MSEC,time*1000)
        self.readset = True
    def now(self):
        return int(self.videoreader.get(cv2.CAP_PROP_POS_MSEC)/1000)
    def pause(self):
        self.readset = False
    def unpause(self):
        self.readset = True
    def stop(self):
        self.pause()
        self.readset = False
        self.endset = True
        while self.threadrunset:
            self.frame.update()

class DlLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        pass

class firstbutton(tk.Button):
    def __init__(self,master=None,cnf={},**kw):
        tk.Button.__init__(self,master,cnf,**kw)
        self.configure(font=("",15),height=1, width=2, relief="ridge",fg="black",bg="white")

def jsonset(filepath,booldata):
    eulajson = {"eulaset":"false"}
    if booldata:
        eulajson = {"eulaset":"true"}
    else:
        eulajson = {"eulaset":"false"}
    with open(filepath, mode='wt', encoding='utf-8') as file:
        json.dump(eulajson, file, ensure_ascii=False, indent=3)

def readjson(filepath):
    try:
        with open(filepath, mode='rt', encoding='utf-8') as file:
            eulaset = json.load(file)["eulaset"]
        if eulaset == "true":
            return True
        else:
            return False
    except:
        return False

dlwin.withdraw()
mypath = os.path.dirname(os.path.abspath(sys.argv[0]))
eula = readjson(os.path.join(mypath,"setting.json"))
if eula:
    pass
else:
    douiwin = tk.Toplevel()
    douiwin.title("免責事項")
    douiwin.resizable(0,0)
    douiwin.attributes("-topmost",True)
    lisencelbl = tk.Label(douiwin,text="""                  とりあえず作ったmp3プレイヤー
    このmp3プレイヤーは何となくで作ったソフトですのでところどころ作りこみが甘いです
    また、予期せぬバグとうがあると思います、バージョンアップ等は気が向いたら作ります

                Copyright (c) <2021> <マッツウー>

    以下に定める条件に従い、本ソフトウェアおよび関連文書のファイル（以下「ソフトウェア」）の複製を取得するすべての人に対し、ソフトウェアを無制限に扱うことを無償で許可します。

    これには、ソフトウェアの複製を使用、複写、変更、結合、掲載、頒布、サブライセンス、および/または販売する権利、およびソフトウェアを提供する相手に同じことを許可する権利も無制限に含まれます。
    上記の著作権表示および本許諾表示を、ソフトウェアのすべての複製または重要な部分に記載するものとします。

    ソフトウェアは「現状のまま」で、明示であるか暗黙であるかを問わず、何らの保証もなく提供されます。
    ここでいう保証とは、商品性、特定の目的への適合性、および権利非侵害についての保証も含みますが、それに限定されるものではありません。 
    作者または著作権者は、契約行為、不法行為、またはそれ以外であろうと、ソフトウェアに起因または関連し、
    あるいはソフトウェアの使用またはその他の扱いによって生じる一切の請求、損害、その他の義務について何らの責任も負わないものとします。
    実行する場合は上記の内容に同意してください""",font=("",15))
    def douiok():
        if eulaset.get():
            jsonset(os.path.join(mypath,"setting.json"),True)
        else:
            jsonset(os.path.join(mypath,"setting.json"),False)
        closeset.set(True)
        douiwin.destroy()
    def douinotok():
        jsonset(os.path.join(mypath,"setting.json"),False)
        closeset.set(True)
        sys.exit(1)
    lisencelbl.pack(fill=tk.BOTH,expand=True)
    eulaset = tk.BooleanVar()
    eulaset.set(True)
    closeset = tk.BooleanVar()
    closeset.set(False)
    chkbtn = ttk.Checkbutton(douiwin,variable=eulaset,text="この画面を次回から表示しない(同意しないを選択した場合は次回も表示されます)")
    chkbtn.pack(fill=tk.X,expand=True)
    btn = firstbutton(douiwin,text="同意しない",command=douinotok)
    btn.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
    btn = firstbutton(douiwin,text="同意する",command=douiok)
    btn.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
    douiwin.protocol("WM_DELETE_WINDOW", douinotok)
    while True:
        if closeset.get():
            break
        douiwin.update()
root.deiconify()
video = Video()
audio = Audio()
def MP3(path):
    tag = TinyTag.get(path)
    return tag.duration
if os.path.exists(mypath + "\\config.ini"):
    pass
else:
    with open(os.path.join(mypath,"config.ini"),"w") as ini:
        ini.write("[keydata]\n")
        ini.write("pausekey = pause\n")
        ini.write("volupkey = f12\n")
        ini.write("voldownkey = f9\n")
    config_ini = configparser.ConfigParser()
    config_ini.read(os.path.join(mypath,'config.ini'), encoding='utf-8')
if os.path.exists(os.path.join(mypath,"usefile.log")):
    pass
else:
    templist = {}
    with open(mypath + "\\usefile.log",mode='wt',encoding='utf-8') as usedata:
        json.dump(templist,usedata, ensure_ascii=False, indent=2)
playlistlist = []
def usejsonadd(data):
    global uselist
    listcount = len(uselist)
    dt_now = datetime.datetime.now()
    uselist.setdefault(str(dt_now),str(data))
def skeyset():
    skeywin = tk.Toplevel()
    skeywin.resizable(0,0)
    skeywin.attributes("-topmost",True)
    pausechkset.set(True)
    upset.set(True)
    downset.set(True)
    config_ini = configparser.ConfigParser()
    config_ini.read(os.path.join(mypath,'config.ini'), encoding='utf-8')
    pausetkey.set(config_ini['keydata']['pausekey'])
    volupkey.set(config_ini['keydata']['volupkey'])
    voldownkey.set(config_ini['keydata']['voldownkey'])
    frame = tk.Frame(skeywin,width=500,height=300)
    frame.grid(row=0,column=0)
    pausekey = tk.Entry(frame,width=10,textvariable=pausetkey,state="readonly")
    pausekey.grid(row=0,column=0)
    upchk = tk.Checkbutton(frame,text="一時停止/再生　変更キー",variable=pausechkset)
    upchk.grid(row=0,column=1)
    gridlbl = tk.Label(frame)
    gridlbl.grid(row=1,column=0)
    upkey = tk.Entry(frame,width=10,textvariable=volupkey,state="readonly")
    upkey.grid(row=3,column=0)
    upchk = tk.Checkbutton(frame,text="\t音量　増加キー",variable=upset)
    upchk.grid(row=3,column=1)
    gridlbl = tk.Label(frame)
    gridlbl.grid(row=5,column=0)
    downkey = tk.Entry(frame,width=10,textvariable=voldownkey,state="readonly")
    downkey.grid(row=6,column=0)
    downchk = tk.Checkbutton(frame,text="\t音量　減少キー",variable=downset)
    downchk.grid(row=6,column=1)
    def keywclose():
        if messagebox.askokcancel("確認", "キー設定を保存しますか?"):
            with open("config.ini","w") as ini:
                ini.write("[keydata]\n")
                ini.write("pausekey = " + str(pausetkey.get()) + "\n")
                ini.write("volupkey = " + str(volupkey.get()) + "\n")
                ini.write("voldownkey = " + str(voldownkey.get()) + "\n")
            skeywin.destroy()
        else:
            pausetkey.set(config_ini['keydata']['pausekey'])
            volupkey.set(config_ini['keydata']['volupkey'])
            voldownkey.set(config_ini['keydata']['voldownkey'])
            skeywin.destroy()
    skeywin.protocol("WM_DELETE_WINDOW", keywclose)
def loadwin(path):
    loadw = tk.Toplevel()
    loadw.resizable(0,0)
    loadw.attributes("-topmost",True)
    loadprogress = ttk.Progressbar(loadw,length=600)
    loadprogress.grid(row=0,column=0)
    loadtree = ttk.Treeview(loadw)
    loadtree.grid(row=1,column=0)
    loadtree["column"] = (1,2)
    loadtree["show"] = "headings"
    loadtree.heading(1,text="ファイルパス")
    loadtree.heading(2,text="状況")
    loadtree.column(1, width=500)
    loadtree.column(2, width=100)
    def fload(path):
        pauseset.set(False)
        lenlist = []
        lenlist.clear()
        flist = glob.glob(str(path) + "/**.mp4",recursive=True)
        count = 0
        loadprogress.config(maximum=len(flist))
        loadprogress.update()
        root.withdraw()
        for data in flist:
            try:
                loadtree.yview_moveto(1)
                audio = MP3(str(data))
                mp3len = str(round(audio,0)) +  "秒"
                count = count + 1
                tree.insert("", "end", values=(str(os.path.basename(data)), str(data),str(mp3len),"デフォルト"))
                root.update()
                fdata2.append(str(data))
                fdata2.append(audio)
                loadtree.insert("", "end", values=(str(data), str("読み込み成功◎")))
                loadprogress.config(value=count)
                loadprogress.update()
                usejsonadd(str(data))
            except:
                count = count + 1
                loadtree.insert("", "end", values=(str(data), str("読み込み失敗")))
                loadw.update()
                loadprogress.config(value=count)
                loadprogress.update()
        with open(mypath + "\\usefile.log",mode='wt',encoding='utf-8') as usedata:
            json.dump(uselist,usedata, ensure_ascii=False, indent=2)
    fload(path)
    root.deiconify()
    loadw.destroy()
def loadwin2(path):
    loadw = tk.Toplevel()
    loadw.resizable(0,0)
    loadw.attributes("-topmost",True)
    loadprogress = ttk.Progressbar(loadw,length=600)
    loadprogress.grid(row=0,column=0)
    loadtree = ttk.Treeview(loadw)
    loadtree.grid(row=1,column=0)
    loadtree["column"] = (1,2)
    loadtree["show"] = "headings"
    loadtree.heading(1,text="ファイルパス")
    loadtree.heading(2,text="状況")
    loadtree.column(1, width=500)
    loadtree.column(2, width=100)
    window.withdraw()
    def fload2(path):
        pauseset.set(False)
        lenlist = []
        lenlist.clear()
        flist = glob.glob(str(path) + "/**.mp4",recursive=True)
        loadprogress.config(maximum=len(flist))
        loadprogress.update()
        count = 0
        usejsonadd(path)
        for data in flist:
            try:
                loadtree.yview_moveto(1)
                makeaudio = MP3(str(data))
                makemp3len = str(round(makeaudio,0)) +  "秒"
                maketree.insert("", "end", values=(str(os.path.basename(data)), str(data),str(makemp3len)))
                maketree.update()
                playlistdata.append(str(data))
                loadtree.insert("", "end", values=(str(data), str("読み込み成功◎")))
                count = count + 1
                loadprogress.config(value=count)
                loadprogress.update()
                usejsonadd(str(data))
            except:
                import traceback
                traceback.print_exc()
                count = count + 1
                loadtree.insert("", "end", values=(str(data), str("読み込み失敗")))
                loadw.update()
                loadprogress.config(value=count)
                loadprogress.update()
        with open(mypath + "\\usefile.log",mode='wt',encoding='utf-8') as usedata:
            json.dump(uselist,usedata,ensure_ascii=False, indent=2)
    fload2(path)
    window.deiconify()
    loadw.destroy()
def buttonbox():
    global window
    window = tk.Toplevel()
    window.resizable(0,0)
    window.attributes("-topmost",True)
    def askff():
        idir = 'C:\\python_test'
        file_path = tk.filedialog.askdirectory(initialdir = idir)
        if file_path == "":
            pass
        else:
            loadwin2(file_path)
    def playaddfile():
        fTyp = [("音声ファイル", ".mp4")]
        iDir = os.path.abspath(os.path.dirname(__file__))
        file_name = tk.filedialog.askopenfilename(filetypes=fTyp, initialdir=iDir)
        if file_name == "":
            pass
        else:
            makeaudio = MP3(str(file_name))
            makemp3len = str(round(makeaudio,0)) +  "秒"
            maketree.insert("", "end", values=(str(os.path.basename(file_name)), str(file_name),str(makemp3len)))
            playlistdata.append(str(file_name))

    def delete(): 
        selected_items = maketree.selection()
        if not selected_items:
            pass
        else:
            selected_item = maketree.selection()[0]
            values = maketree.item(selected_items[0])['values'][1] 
            maketree.delete(selected_item)
            playlistdata.remove(str(values))
    def playlistload():
        fTyp = [("プレイリストファイル","*.Enclosed.playlist"),("すべてのファイル","*")]
        iDir = os.path.abspath(os.path.dirname(__file__))
        file = tk.filedialog.askopenfilename(filetypes = fTyp,initialdir = iDir)
        if file == "":
            pass
        else:
            pauseset.set(False)
            lenlist = []
            lenlist.clear()
            playdata = []
            flist = glob.glob(str(os.path.dirname(__file__) + "\\tempfile\\tempplaylistdir") + "/**.mp4",recursive=True)
            for fname in flist:
                os.remove(str(fname))
            with open(str(file),"r",encoding="utf-8") as readplay:
                playdatatemp = readplay.readlines()
            a = 1 
            while True:
                try:
                    if len(playdatatemp) < a:
                        break
                    base64decodef(str(str(os.path.dirname(__file__) + "\\tempfile\\tempplaylistdir") + "\\" + playdatatemp[a]).replace("\n",""),str(playdatatemp[a+1]))
                    a = a + 2
                except:
                    a = a + 2
            loadwin2(str(os.path.dirname(__file__) + "\\tempfile\\tempplaylistdir"))
    def playlistaddfile():
        filename =  filedialog.asksaveasfilename(title = "同封済みプレイリスト保存",filetypes=[("同封済みプレイリストファイル","*.Enclosed.playlist")])
        if filename == "":
            pass
        else:
            filename = filename + ".Enclosed.playlist"
            with open(str(filename),"w",encoding="utf-8") as Eplaylist:
                Eplaylist.write(str(len(playlistdata)) + "\n")
                for fname in playlistdata:
                    try:
                        fno = str(os.path.basename(fname))
                        with open(str(fname),"rb") as bdata:
                            binaryd = bdata.read()
                        bout = base64.b64encode(binaryd)
                        Eplaylist.write(str(fno) + "\n")
                        Eplaylist.write(bout.decode("utf-8") + "\n")
                    except:
                        pass
    def playurladd():
        urldata = simpledialog.askstring("URL","YoutubeのURLを入力してください")
        if urldata == None:
            pass
        
    def riset():
        for i in maketree.get_children():
            maketree.delete(i)
        playlistdata.clear()
    box = tk.Frame(window)
    setmainframe = tk.Frame(box,width=500,height=300)
    setmainframe.pack(fill=tk.BOTH,expand=True)
    makelbl = tk.LabelFrame(setmainframe,text="プレイリスト作成")
    makelbl.pack(fill=tk.X)
    global maketree
    maketree = ttk.Treeview(makelbl)
    for data in playlistdata:
        try:
            makeaudio = MP3(str(data))
            makemp3len = str(round(makeaudio,0)) +  "秒"
            maketree.insert("", "end", values=(str(os.path.basename(data)), str(data),str(makemp3len)))
        except:
            pass
    treelbl = tk.LabelFrame(makelbl)
    treelbl.pack(fill=tk.X)
    btn = tk.Button(treelbl,text="プレイリストに追加(ファイル)",width=19,command=playaddfile)
    btn.pack(fill=tk.X,side=tk.LEFT)
    btn = tk.Button(treelbl,text="プレイリストに追加(フォルダ)",width=19,command=askff)
    btn.pack(fill=tk.X,side=tk.LEFT)
    btn = tk.Button(treelbl,text="プレイリストから削除",width=19,command=delete)
    btn.pack(fill=tk.X,side=tk.LEFT)
    btn = tk.Button(treelbl,text="リセット",fg="red",width=19,command=riset)
    btn.pack(fill=tk.X,side=tk.LEFT)
    btn = tk.Button(treelbl,text="プレイリストを読み込む",width=19,command=playlistload)
    btn.pack(fill=tk.X,side=tk.LEFT)
    btn = tk.Button(treelbl,text="プレイリストを出力する",width=19,command=playlistaddfile)
    btn.pack(fill=tk.X,side=tk.LEFT)
    outprogress = ttk.Progressbar(window)
    outprogress.pack(fill=tk.X)
    maketree.pack(fill=tk.BOTH,expand=True)
    maketree["column"] = (1,2,3)
    maketree["show"] = "headings"
    maketree.heading(1,text="ファイル名")
    maketree.heading(2,text="ファイルパス")
    maketree.heading(3,text="長さ")
    maketree.column(1, width=380)
    maketree.column(2, width=380)
    maketree.column(3, width=100)
    secret_password = b'lost art of keeping a secret'
    box.pack()
def listriset():
    askdata = messagebox.askokcancel("確認","リセットしますか?")
    if askdata:
        for i in tree.get_children():
            tree.delete(i)
        fdata2.clear()
    soundstop()
def base64decodef(filename,base64string):
    with open(str(filename),"wb") as mp3decode:
        mp3decode.write(base64.b64decode(base64string))
def zipplayloadth():
    fTyp = [("プレイリストファイル","*.Enclosed.playlist"),("すべてのファイル","*")]
    iDir = os.path.abspath(os.path.dirname(__file__))
    file = tk.filedialog.askopenfilename(filetypes = fTyp,initialdir = iDir)
    if file == "":
        pass
    else:
        usejsonadd(str(file))
        pauseset.set(False)
        lenlist = []
        lenlist.clear()
        playdata = []
        flist = glob.glob(str(os.path.dirname(__file__) + "\\tempfile\\tempplaylistdir") + "/**.mp4",recursive=True)
        for fname in flist:
            os.remove(str(fname))
        with open(str(file),"r",encoding="utf-8") as readplay:
            playdatatemp = readplay.readlines()
        a = 1 
        while True:
            try:
                if len(playdatatemp) < a:
                    break
                base64decodef(str(str(os.path.dirname(__file__) + "\\tempfile\\tempplaylistdir") + "\\" + playdatatemp[a]).replace("\n",""),str(playdatatemp[a+1]))
                a = a + 2
            except:
                import traceback
                traceback.print_exc()
                a = a + 2
        flist = glob.glob(str(os.path.dirname(__file__) + "\\tempfile\\tempplaylistdir") + "/**.mp4",recursive=True)
        count = 0
        for data in flist:
            try:
                audio = MP3(str(data))
                mp3len = str(round(audio,0)) +  "秒"
                count = count + 1
                tree.insert("", "end", values=(str(os.path.basename(data)), str(data),str(mp3len),"デフォルト"))
                fdata2.append(str(data))
                fdata2.append(audio)
            except:
                pass
def zipplayload():
    loadth = threading.Thread(target=zipplayloadth)
    loadth.setDaemon(True)
    loadth.start()
def listdel():
    selected_items = tree.selection()
    if not selected_items:
        pass
    values = tree.selection()
    valuedata = tree.item(selected_items[0])['values'][1]
    tree.delete(values)
    posi = fdata2.index(valuedata)
    del fdata2[posi:posi+2]
def dchange():
    idir = 'C:\\python_test'
    file_path = tk.filedialog.askdirectory(initialdir = idir)
    if file_path == "":
        pass
    else:
        loadwin(file_path)
def logplayadd():
    selected_items = logtree.selection()
    if not selected_items:
        return
    values = logtree.item(selected_items[0])['values']
    data = values[0]
    if os.path.exists(data):
        if data.endswith('.Enclosed.playlist'):
            pauseset.set(False)
            lenlist = []
            lenlist.clear()
            playdata = []
            flist = glob.glob(str(os.path.dirname(__file__) + "\\tempfile\\tempplaylistdir") + "/**.mp4",recursive=True)
            for fname in flist:
                os.remove(str(fname))
            with open(str(data),"r",encoding="utf-8") as readplay:
                playdatatemp = readplay.readlines()
            a = 1 
            while True:
                try:
                    if len(playdatatemp) < a:
                        break
                    base64decodef(str(str(os.path.dirname(__file__) + "\\tempplaylistdir") + "\\" + playdatatemp[a]).replace("\n",""),str(playdatatemp[a+1]))
                    a = a + 2
                except:
                    a = a + 2
            flist = glob.glob(str(os.path.dirname(__file__) + "\\tempfile\\tempplaylistdir") + "/**.mp4",recursive=True)
            count = 0
            for data in flist:
                try:
                    audio = MP3(str(data))
                    mp3len = str(round(audio,0)) +  "秒"
                    count = count + 1
                    tree.insert("", "end", values=(str(os.path.basename(data)), str(data),str(mp3len),"デフォルト"))
                    fdata2.append(str(data))
                    fdata2.append(audio)
                except:
                    pass
        else:
            audio = MP3(str(data))
            mp3len = str(round(audio,0)) +  "秒"
            tree.insert("", "end", values=(str(os.path.basename(data)), str(data),str(mp3len),"デフォルト"))
            fdata2.append(str(data))
            fdata2.append(audio)
            with open(mypath + "\\usefile.log",mode='wt',encoding='utf-8') as usedata:
                json.dump(uselist,usedata,ensure_ascii=False, indent=2)
        usejsonadd(data)
    else:
        askdellog = messagebox.askokcancel("確認","ファイルが存在しません\nこの履歴を削除しますか?")
        if askdellog:
            values = logtree.item(selected_items[0])['values']
            data = values[0]
            del uselist[data]
            logtree.delete(selected_items)
            with open(mypath + "\\usefile.log",mode='wt',encoding='utf-8') as usedata:
                json.dump(uselist,usedata,ensure_ascii=False, indent=2)

def logplaydel():
    selected_items = logtree.selection()
    if not selected_items:
        return
    values = logtree.item(selected_items[0])['values']
    data = values[1]
    del uselist[data]
    logtree.delete(selected_items)
    with open(mypath + "\\usefile.log",mode='wt',encoding='utf-8') as usedata:
        json.dump(uselist,usedata,ensure_ascii=False, indent=2)
def logriset():
    askriset = messagebox.askokcancel("確認","ログをリセットしますか？")
    if askriset:
        for i in logtree.get_children():
            logtree.delete(i)
        uselist.clear()
        with open(mypath + "\\usefile.log",mode='wt',encoding='utf-8') as usedata:
            json.dump(uselist,usedata,ensure_ascii=False, indent=2)
def logwindow():
    logwin = tk.Toplevel()
    logwin.resizable(0,0)
    logwin.attributes("-topmost",True) 
    global logtree
    logtree = ttk.Treeview(logwin)
    loadlogprogress = ttk.Progressbar(logwin)
    loadlogprogress.grid(row=0,column=0,sticky=tk.E+tk.W)
    logtree.grid(row=1,column=0)
    logtree["column"] = (1,2)
    logtree["show"] = "headings"
    logtree.heading(1,text="ファイルパス")
    logtree.heading(2,text="使用時間")
    logtree.column(1, width=520)
    logtree.column(2, width=200)
    btnlbl = tk.LabelFrame(logwin)
    btnlbl.grid(row=2,column=0)
    logaddbtn = tk.Button(btnlbl,text="追加",width=35-1,command=logplayadd)
    logaddbtn.grid(row=0,column=0)
    logdelbtn = tk.Button(btnlbl,text="削除",width=35-1,command=logplaydel)
    logdelbtn.grid(row=0,column=1)
    logrisetbtn = tk.Button(btnlbl,text="リセット",width=35-1,command=logriset)
    logrisetbtn.grid(row=0,column=2)
    count = 0
    count = 0
    keylist = uselist.keys()
    loadlogprogress.config(maximum=len(keylist))
    loadlogprogress.update()
    for key in keylist:
        logtree.insert("", "end", values=(str(uselist[key]), str(key)))
        logtree.yview_moveto(1)
        loadlogprogress.config(value=count)
        logwin.update()
    loadlogprogress.destroy()

def timeset():
    time = 18
    video.seek(time)
    audio.seek(time+((time/101)*9))
def fmove(event):
    fxposi.set(event.x)
    fyposi.set(event.y)

def move(event):
    xposi,yposi = mouse.get_position()
    video.sizechange(int(moviewindow.winfo_width()+5),int(moviewindow.winfo_height()+5))
    moviewindow.geometry(str(moviewindow.winfo_width()) + "x" + str(moviewindow.winfo_height()) +"+" + str(xposi-fxposi.get()) + "+" + str(yposi-fyposi.get()))
#def unpausef():
#    video.unpause()
#    audio.unpause()
#    time = pauseset.get()
#    video.seek(time)
#    audio.seek(time+((time/101)*9))
def loopstart(fa,startposin):
    endset.set(False)
    endcall.set(False)
    listlen = len(fdata2)
    startposi = startposin
    a = fa
    playcount = 1
    mp3changeset.set(False)
    try:
        moviewindow.deiconify()
    except:
        pass
    print(startposi)
    while True:
        if not startposi == 0:
            timeposi = startposi
            video.seek(timeposi)
            audio.seek(timeposi+((timeposi/100)*9))
        else:
            try:
                video.stop()
            except:
                pass
            try:
                audio.stop()
            except:
                pass
            video.openfile(fdata2[a],movielabel)
            audio.openfile(fdata2[a])
            audio.audioplay()
            video.play()
            audio.setvolume(setvar.get())
        listlen = len(fdata2)
        if a >= listlen:
            a = a - 2
        nowplaypath.set(fdata2.index(fdata2[a]))
        nowlbl["text"] = os.path.basename(fdata2[a])
        popnowlbl["text"] = os.path.basename(fdata2[a])
        asl = 0
        aftime = time.time() + fdata2[a+1]
        nowtime = time.time()
        zdata = aftime - nowtime
        timeprogress["to_"] = int(round(aftime-nowtime,1))
        nowtimeture = int(round(round(zdata,1)-round(aftime-nowtime,1),1)+startposi)
        mp3changeset.set(False)
        if endset.get():
            audio.stop()
            video.stop()
            endcall.set(True)
            break
        lasttime = 0
        while True:
            nowtime = time.time()
            asl = asl + 0.01
            if not mp3changeset.get():
                soundset.set(round(round(zdata,1)-round(aftime-nowtime,1),1)+startposi)
            nowtimeture = round(round(zdata,1)-round(aftime-nowtime,1),1)+startposi
            try:
                root.update()
            except:
                pass
            pauseb = time.time()
            if endset.get():
                audio.stop()
                video.stop()
                endcall.set(True)
                break
            while True:
                if endset.get():
                    audio.stop()
                    video.stop()
                    endcall.set(True)
                    break
                try:
                    root.update()
                except:
                    pass
                if pauseset.get():
                    audio.pause()
                    video.pause()
                    pausef = time.time()
                else:
                    pausef = time.time()
                    audio.unpause()
                    video.unpause()
                    aftime = aftime + round(pausef-pauseb,1)
                    break
            if nowtimeture > zdata:
                if loopset.get() == "nextaudio":
                    a = a + 2
                elif loopset.get() == "loop":
                    pass
                elif loopset.get() == "appexit":
                    soundswitchbtn["text"] = "連続再生"
                    soundplayset.set(False)
                    soundstop()
                elif loopset.get() == "runcmd":
                    try:
                        subprocess.Popen(runcmdbox.get().split(" "),shell=True)
                    except:
                        pass
                    a = a + 2
                #playcount = playcount + 1
                playcount = random.randint(0,listlen)
                startposi = 0
                try:
                    audio.stop()
                    video.stop()
                except:
                    pass
                break
        if a >= listlen:
            try:
                audio.stop()
                video.stop()
            except:
                pass
            playcount = 1
            a = 0
        if endset.get():
            audio.stop()
            video.stop()
            endcall.set(True)
            break
    endcall.set(True)
    audio.stop()
    video.stop()
def volumechange(w):
    try:
        pygame.mixer.music.set_volume(setvar.get())
    except:
        pass
def pausef():
    if pauseset.get():
        stopsetbtn["text"] = "⏸"
        pausebtn["text"] = "⏸"
        pauseset.set(False)
    else:
        stopsetbtn["text"] = "▶"
        pausebtn["text"] = "▶"
        pauseset.set(True)
    root.update()
def soundswitch():
    try:
        if soundplayset.get():
            soundswitchbtn["text"] = "連続再生"
            soundplayset.set(False)
            soundstop()
        else:
            soundswitchbtn["text"] = "再生停止"
            soundplayset.set(True)
            soundth()
    except:
        import traceback
        traceback.print_exc()
def soundth():
    try:
        pygame.mixer.music.stop()
    except:
        pass
    try:
        pygame.mixer.music.unload()
    except:
        pass
    loopstart(0,0)
def clicked(event):
    global thendset,thrunset
    selected_items = tree.selection()
    if not selected_items:
        pass
    values = tree.item(selected_items[0])['values'][1]
    indexs = fdata2.index(values)
    try:
        pygame.mixer.music.stop()
    except:
        pass
    loopstart(indexs,0)
def soundstop():
    try:
        audio.stop()
    except:
        pass
    endset.set(True)
    try:
        video.stop()
    except:
        pass
    moviewindow.withdraw()
    nowlbl["text"] = ""
    popnowlbl["text"] = ""
def mp3dataget(filepath):
    tag = TinyTag.get(filepath,image=True)
    data = []
    datalist = [tag.album,tag.albumartist,tag.artist,tag.audio_offset,tag.bitrate,tag.comment,tag.composer,tag.disc,tag.disc_total,tag.duration,tag.filesize,tag.genre,tag.samplerate,tag.title,tag.track,tag.track_total,tag.year]
    for datac in datalist:
        try:
            data.append(datac)
        except:
            misscount = misscount + 1 
    return data
def fileread():
    fTyp = [("音声ファイル", "*.mp4")]
    iDir = os.path.abspath(os.path.dirname(__file__))
    data = filedialog.askopenfilename(filetypes=fTyp, initialdir=iDir)
    try:
        audio = MP3(str(data))
        mp3len = str(round(audio,0)) +  "秒"
        tree.insert("", "end", values=(str(os.path.basename(data)), str(data),str(mp3len),"デフォルト"))
        root.update()
        fdata2.append(str(data))
        fdata2.append(audio)
        usejsonadd(str(data))
    except:
        import traceback
        traceback.print_exc()
    with open(mypath + "\\usefile.log",mode='wt',encoding='utf-8') as usedata:
        json.dump(uselist,usedata,ensure_ascii=False, indent=2)
def soundposichange(event):
    loopstart(nowplaypath.get(),float(timeprogress.get()))
    mp3changeset.set(False)
def soundchangef(aaa):
    mp3changeset.set(True)
class dataDialog(simpledialog.Dialog):
    def buttonbox(self):
        self.resizable(0,0)
        self.attributes("-topmost",True)
        box = tk.Frame(self)
        datatree = ttk.Treeview(box)
        datatree["column"] = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18)
        datatree["show"] = "headings"
        count = 1
        datalist = ["ファイルパス","アルバム","アルバムアーティスト","アーティスト名","オーディオオフセット","ビットレート","コメント","作曲家","ディスク番号","ディスクの総数","曲の長さ(秒)","ファイルサイズ(bytes)","ジャンル","サンプルレート","タイトル","トラック","トラックトータル","年"]
        for dataname in datalist:
            datatree.heading(count,text=dataname)
            count = count + 1
        for num in str("1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18").split(","):
            datatree.column(int(float(num)), width=100)
        datatree.grid(row=0,column=0)
        count = 0
        while True:
            try:
                fname = fdata2[count]
                listmax = len(fdata2)
                if count >= listmax:
                    break
                data = mp3dataget(fname)
                try:
                    datatree.insert("", "end", values=(fname,data[0],data[1],data[2],data[3],data[2+2],data[5],data[6],data[7],data[8],round(data[9],1),data[10],data[11],data[12],data[13],data[14],data[15],data[16]))
                except:
                    pass
                count = count + 2
            except:
                break
        box.pack()

script_dir = os.path.dirname(sys.argv[0])

try:
    os.mkdir(os.path.join(os.path.dirname(sys.argv[0]),"tempfile"))
except:
    pass

class popenr:
    def __init__(self):
        self.popenobj = ""
        self.qudata = queue.Queue()
        self.readth = ""
        self.endset = False
    def runcmd(self,command):
        self.endset = False
        self.readth = threading.Thread(target=self.rstdout,args=(command,))
        self.readth.setDaemon(True)
        self.readth.start()
    def rstdout(self,command):
        try:
            startupinfo = subprocess.STARTUPINFO()
            startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
            self.popenobj = subprocess.Popen(command,startupinfo=startupinfo,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,stdin=subprocess.DEVNULL,shell=True)
            while True:
                try:
                    line = self.popenobj.stdout.readline()
                    if line:
                        self.qudata.put(line)

                    if not line and self.popenobj.poll() is not None:
                        break
                except:
                    import traceback
                    traceback.print_exc()
                    break
        except:
            import traceback
            traceback.print_exc()
        self.endset = True
    def killp(self):
        try:
            if self.endset:
                try:
                    self.popenobj.kill()
                except:
                    pass
            else:
                startupinfo = subprocess.STARTUPINFO()
                startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
                subprocess.run(["taskkill","/f","/t","/pid",str(self.popenobj.pid)],startupinfo=startupinfo,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL,stdin=subprocess.DEVNULL)
            self.readth.join()
        except:
            import traceback
            traceback.print_exc()
        return self.qudata


#初期設定
runobj = popenr()
savedir = tk.StringVar(root)

openset = tk.BooleanVar(root)
openset.set(False)
playfileset = tk.BooleanVar(root)
playfileset.set(True)

#関数関連
def checkmain():
    checkbtn.config(state="disabled")
    try:
        for i in formattree.get_children():
            formattree.delete(i)
        url = urlentry.get()
        with youtube_dl.YoutubeDL({"quiet":True}) as ydl:
            info_dict = ydl.extract_info(url,download=False)
            titlelbl["text"] = info_dict.get('title',"None")
            for format in info_dict["formats"]:
                id = format['format_id']
                kaizoudo = ""
                if format["format_note"] == "tiny":
                    formattype = "音声"
                    kaizoudo = "None"
                else:
                    formattype = "動画"
                    kaizoudo = format.get("format_note","None")
                filesize = format.get("filesize","None")
                extdata = format.get("ext","None")
                formattree.insert("", "end", values=(id,formattype,kaizoudo,filesize,extdata))
                formattree.update()
    except:
        pass
    checkbtn.config(state="normal")
def check():
    checkth = threading.Thread(target=checkmain)
    checkth.setDaemon(True)
    checkth.start()
def closewin():
    global runobj
    try:
        runobj.killp()
    except:
        pass
    downloadwin.withdraw()

def closeadd():
    global runobj
    try:
        runobj.killp()
    except:
        pass
    root.deiconify()
    addwin.withdraw()
    downloadwin.withdraw()

def downloadmain():
    global runobj
    dlbtn["state"] = tk.DISABLED
    try:
        nowpath = os.getcwd()
        try:
            os.makedirs(savedir.get())
        except:
            pass

        downloadwin.deiconify()
        selected_items = formattree.selection()
        if not selected_items:
            messagebox.showerror("エラー","ダウンロードフォーマットを選択してください")
            raise ValueError("no selection")
        # SelectModeがBrowseなので、複数選択を考慮しない
        values = formattree.item(selected_items[0])['values']
        
        url = urlentry.get()
        filename = ""
        videoformat = str(values[0])
        audioformat = "bestaudio/best"
        exepath = os.path.join(os.path.dirname(sys.argv[0]),"bin\\yt-dlp.exe")
        with youtube_dl.YoutubeDL({"quiet":True}) as ydl:
            info_dict = ydl.extract_info(url,download=False)
            video_url = info_dict.get("url", None)
            video_title = info_dict.get('title', None)
        nowpath = os.getcwd()
        os.chdir(savedir.get())
        if video_url == None:
            video_url = url
        if values[1] == "動画":
            audioformat = "bestaudio/best"
            formattype = "mp4"
            outpath = repr("{}.{}".format(video_title,formattype)).replace("\\","/").replace("/","_").replace(" ","_").replace("'","")
            runobj.runcmd(f'{exepath} --newline -f {videoformat}+{audioformat} {video_url} --merge-output-format {formattype} -o {outpath}')
        elif values[1] == "音声":
            audioformat = str(values[0])
            formattype = "mp3"
            outpath = repr("{}.{}".format(video_title,formattype)).replace("\\","/").replace("/","_").replace(" ","_").replace("'","")
            runobj.runcmd(f'{exepath} --newline -f {audioformat} {video_url} -x --audio-format {formattype} -o {outpath}')
        resultlist.delete(0,tk.END)
        playfilepath = os.path.abspath(outpath)
        while not runobj.endset:
            while not runobj.qudata.empty():
                getdata = runobj.qudata.get()
                try:
                    decdata = getdata.decode("utf-8")
                except:
                    try:
                        decdata = getdata.decode("cp932")
                    except:
                        pass
                try:
                    resultlist.insert(tk.END,str(decdata))
                    resultlist.yview_moveto(1)
                except:
                    pass
        audio = MP3(str(playfilepath))
        mp3len = str(round(audio,0)) +  "秒"
        tree.insert("", "end", values=(str(os.path.basename(playfilepath)), str(playfilepath),str(mp3len),"デフォルト"))
        root.update()
        fdata2.append(str(playfilepath))
        fdata2.append(audio)
        usejsonadd(str(playfilepath))
            
    except:
        pass
    try:
        os.chdir(nowpath)
    except:
        pass
    dlbtn["state"] = tk.NORMAL
    root.deiconify()
    addwin.withdraw()
    downloadwin.withdraw()
def download():
    downloadth = threading.Thread(target=downloadmain)
    downloadth.setDaemon(True)
    downloadth.start()

addwin = tk.Toplevel(root)
addwin.attributes("-topmost",True)
addwin.title("URLから追加")
addwin.geometry("700x500")
addwin.withdraw()
addwin.protocol("WM_DELETE_WINDOW",closeadd)

downloadwin = tk.Toplevel(root)
downloadwin.attributes("-topmost",True)
downloadwin.title("ダウンロード中...")
downloadwin.geometry("500x300")
downloadwin.withdraw()
downloadwin.protocol("WM_DELETE_WINDOW",closewin)

resultlist = tk.Listbox(downloadwin)
resultlist.pack(fill=tk.BOTH,expand=True)

#初期設定
fileslist = []

#動画ダウンローダー
dlframe = tk.Frame(addwin)
dlframe.pack(fill=tk.BOTH,expand=True)

urlentry = tk.Entry(dlframe,font=("",20))
urlentry.pack(fill=tk.X)

checkbtn = ttk.Button(dlframe,text="利用可能なフォーマットを調べる",command=check)
checkbtn.pack(fill=tk.X)

titlelbl = tk.Label(dlframe,text="動画のタイトル",font=("",15))
titlelbl.pack(fill=tk.X)

treeframe = tk.Frame(dlframe)
treeframe.pack(fill=tk.BOTH,expand=True)

formattree = ttk.Treeview(treeframe)
formattree.pack(fill=tk.BOTH,expand=True,side=tk.LEFT)

scroll = tk.Scrollbar(treeframe,orient=tk.VERTICAL)
scroll.pack(fill=tk.Y,side=tk.LEFT)

scroll.config(command=formattree.yview)
formattree.config(yscrollcommand=scroll.set)

formattree["columns"] = (1,2,3,2+2,5)
# ヘッダーの設定
formattree["show"] = "headings"
formattree.heading(1,text="id")
formattree.heading(2,text="タイプ")
formattree.heading(3,text="画質")
formattree.heading(2+2,text="サイズ")
formattree.heading(5,text="拡張子")
# 各列の幅設定
formattree.column(1,width=50)
formattree.column(2,width=100)
formattree.column(3,width=100)
formattree.column(2+2,width=100)
formattree.column(5,width=100)

dlbtn = ttk.Button(dlframe,text="URLから追加",command=download)
dlbtn.pack(fill=tk.X)
browserrunset = tk.BooleanVar(root)
browserrunset.set(True)
browserendset = tk.BooleanVar(root)
browserfxposi = tk.IntVar(root)
browserfyposi = tk.IntVar(root)
moviewindow = tk.Toplevel()
#moviewindow.overrideredirect(1)
#moviewindow.resizable(0,0)
moviewindow.attributes("-topmost",True)
moviewindow.geometry("500x300")
moviewindow.update_idletasks()

video.sizechange(int(moviewindow.winfo_width()+5),int(moviewindow.winfo_height()+5))
movielabel = tk.Label(moviewindow)
movielabel.place(x=-3,y=-3)
menu_top = tk.Menu(moviewindow,tearoff=False)
menu_2nd = tk.Menu(menu_top,tearoff=0)
menu_3nd = tk.Menu(menu_top,tearoff=0)
def clickvolume(volume):
    setvar.set(float(volume/10))
    volumechange(0)
def showPopup(event):
    menu_top.post(event.x_root,event.y_root)

videoboolset = tk.BooleanVar()
videoboolset.set(True)
def urlread():
    root.withdraw()
    addwin.deiconify()
def videoset():
    if videoboolset.get():
        moviewindow.withdraw()
        videobtn["text"] = "ビデオ画面を表示する"
        videoboolset.set(False)
    else:
        moviewindow.deiconify()
        videobtn["text"] = "ビデオ画面を非表示にする"
        videoboolset.set(True)

movielabel["bg"] = "black"
moviewindow["bg"] = "black"
moviewindow.bind('<Button-3>',showPopup)
moviewindow.bind("<B1-Motion>",move)
moviewindow.bind("<1>",fmove)
moviewindow.protocol('WM_DELETE_WINDOW', (lambda: 'pass')())
moviewindow.withdraw()
fxposi = tk.IntVar()
fyposi = tk.IntVar()
pauseset = tk.IntVar()
mainframe = tk.Frame(root)
mainframe.pack(fill=tk.BOTH,expand=True)

wlist = []

thrunset = False
thendset = False
playlistdata = []
config_ini = configparser.ConfigParser()
config_ini.read(mypath + '\\config.ini', encoding='utf-8')
setlbl = tk.LabelFrame(mainframe,text="設定",width=5)
setlbl.pack(fill=tk.BOTH)
pauseset = tk.BooleanVar(master=root)
pauseset.set(False)
pausebtn = tk.Button(setlbl,text="⏸",command=pausef,font=("",20))
pausebtn.pack(fill=tk.BOTH,expand=True)
viewframe = tk.Frame(setlbl)
viewframe.pack(fill=tk.BOTH,expand=True)
viewoneframe = tk.Frame(viewframe)
viewoneframe.pack(fill=tk.BOTH,expand=True)
soundswitchbtn = tk.Button(viewoneframe,text="連続再生",command=soundswitch)
soundswitchbtn.pack(fill=tk.BOTH,expand=True,side=tk.LEFT)
btn = tk.Button(viewoneframe,text="フォルダを開く",command=dchange,width=20)
btn.pack(fill=tk.BOTH,expand=True,side=tk.LEFT)
viewtwoframe = tk.Frame(viewframe)
viewtwoframe.pack(fill=tk.BOTH,expand=True)
btn = tk.Button(viewtwoframe,text="ファイルを開く",command=fileread)
btn.pack(fill=tk.BOTH,expand=True,side=tk.LEFT)
urlbtn = tk.Button(viewtwoframe,text="URLを開く",command=urlread)
urlbtn.pack(fill=tk.BOTH,expand=True,side=tk.LEFT)
setvar = tk.DoubleVar(master=root)
setvar.set(0.2)
sz = tk.Scale(master=setlbl,showvalue=True,variable=setvar,from_=0,to_=1,tickinterval=True,orient="horizontal",resolution=0.01,command=volumechange)
sz.pack(fill=tk.BOTH,expand=True)
playloadlbl = tk.LabelFrame(setlbl,text="プレイリスト")
playloadlbl.pack(fill=tk.BOTH,expand=True)
loadbtn = tk.Button(playloadlbl,text="プレイリスト読み込み",command=zipplayload,width=20)
loadbtn.pack(fill=tk.BOTH,expand=True)
endframe = tk.LabelFrame(setlbl,text="曲が終わった時にどうするか")
endframe.pack(fill=tk.BOTH,expand=True)
loopset = tk.StringVar()
loopset.set("nextaudio")
templbl = tk.LabelFrame(endframe)
templbl.pack(fill=tk.BOTH,expand=True)
loopchk = tk.Radiobutton(templbl,text="次の曲を再生する",var=loopset,value="nextaudio")
loopchk.pack(fill=tk.BOTH,expand=True,side=tk.LEFT)
loopchk = tk.Radiobutton(templbl,text="現在の曲をループする",var=loopset,value="loop")
loopchk.pack(fill=tk.BOTH,expand=True,side=tk.LEFT)
loopchk = tk.Radiobutton(templbl,text="再生を停止する",var=loopset,value="appexit")
loopchk.pack(fill=tk.BOTH,expand=True,side=tk.LEFT)
runcmdbox = tk.Entry(endframe)
runcmdbox.pack(fill=tk.BOTH,expand=True,side=tk.BOTTOM)
loopchk = tk.Radiobutton(endframe,text="任意のコマンド↓を実行する(コマンドプロンプト)セキュリティイ的に気を付けてください",var=loopset,value="runcmd")
loopchk.pack(fill=tk.BOTH,expand=True,side=tk.BOTTOM)
soundset = tk.DoubleVar()
progresslbl = tk.LabelFrame(mainframe)
progresslbl.pack(fill=tk.BOTH)
timeprogress = tk.Scale(progresslbl,from_=1,length=700,variable=soundset,orient="horizontal",repeatinterval=0,repeatdelay=0,width=20)
listsetlbl = tk.LabelFrame(setlbl,text="プレイリスト")
listsetlbl.pack(fill=tk.BOTH,expand=True)
delbtn = tk.Button(listsetlbl,text="リストから削除する",command=listdel,width=20)
delbtn.pack(fill=tk.BOTH,expand=True,side=tk.LEFT)
risetbtn = tk.Button(listsetlbl,text="リストをリセットする",fg="red",command=listriset,width=20)
risetbtn.pack(fill=tk.BOTH,expand=True,side=tk.LEFT)
videobtn = tk.Button(setlbl,text="ビデオ画面を非表示にする",command=videoset,width=20)
videobtn.pack(fill=tk.BOTH,expand=True)
musicsetlbl = tk.LabelFrame(setlbl,text="曲の設定")
musicsetlbl.pack(fill=tk.BOTH,expand=True)

nowlbl = tk.Label(progresslbl,text="ファイル名")
nowlbl.pack(fill=tk.BOTH,expand=True)
timeprogress.pack(fill=tk.BOTH,expand=True)
timeprogress.bind("<Button>",soundchangef)
timeprogress.bind("<ButtonRelease>",soundposichange)
treeframe1 = tk.Frame(mainframe)
tree = ttk.Treeview(mainframe,height=8)
tree.bind("<Double-1>",clicked)
tree.pack(fill=tk.BOTH,expand=True)
tree["column"] = (1,2,3,2+2)
tree["show"] = "headings"
tree.heading(1,text="ファイル名")
tree.heading(2,text="ファイルパス")
tree.heading(3,text="長さ")
tree.heading(2+2,text="音量")
tree.column(1, width=300)
tree.column(2, width=300)
tree.column(3, width=100)
tree.column(2+2, width=100)
#ドラック＆ドロップ
tree.filenames = {}
tree.nextcoords = [50, 20]
tree.dragging = False

def drag_end(event):
    tree.dragging = False
def drop_enter(event):
    event.widget.focus_force()
    return event.action
def loadplay(file):
    usejsonadd(str(file))
    pauseset.set(False)
    lenlist = []
    lenlist.clear()
    playdata = []
    flist = glob.glob(str(os.path.dirname(__file__) + "\\tempplaylistdir") + "/**.mp4",recursive=True)
    for fname in flist:
        try:
            os.remove(str(fname))
        except:
            pass
    with open(str(file),"r",encoding="utf-8") as readplay:
        playdatatemp = readplay.readlines()
    a = 1 
    while True:
        try:
            if len(playdatatemp) < a:
                break
            base64decodef(str(str(os.path.dirname(__file__) + "\\tempfile\\tempplaylistdir") + "\\" + playdatatemp[a]).replace("\n",""),str(playdatatemp[a+1]))
            a = a + 2
        except:
            import traceback
            traceback.print_exc()
            a = a + 2
    flist = glob.glob(str(os.path.dirname(__file__) + "\\tempfile\\tempplaylistdir") + "/**.mp4",recursive=True)
    count = 0
    for data in flist:
        try:
            audio = MP3(str(data))
            mp3len = str(round(audio,0)) +  "秒"
            count = count + 1
            tree.insert("", "end", values=(str(os.path.basename(data)), str(data),str(mp3len),"デフォルト"))
            fdata2.append(str(data))
            fdata2.append(audio)
        except:
            pass
def drop_position(event):
    return event.action

def drop_leave(event):
    return event.action
def drop(event):
    if tree.dragging:
        return tkinterdnd2.REFUSE_DROP
    if event.data:
        items = tree.tk.splitlist(event.data)
        for item in items:
            if os.path.isdir(item):
                loadwin(item)
            else:
                if item.endswith(".playlist"):
                    loadth = threading.Thread(target=loadplay,args=(item,))
                    loadth.setDaemon(True)
                    loadth.start()
                else:
                    data = item
                    try:
                        audio = MP3(str(data))
                        mp3len = str(round(audio,0)) +  "秒"
                        tree.insert("", "end", values=(str(os.path.basename(data)), str(data),str(mp3len),"デフォルト"))
                        root.update()
                        fdata2.append(str(data))
                        fdata2.append(audio)
                        usejsonadd(str(data))
                    except:
                        import traceback
                        traceback.print_exc()
                    with open(mypath + "\\usefile.log",mode='wt',encoding='utf-8') as usedata:
                        json.dump(uselist,usedata,ensure_ascii=False, indent=2)
    return event.action
def drag_init(event):
    try:
        data = ()
        sel = tree.select_item()
        if sel:
            data = (tree.filenames[sel],)
            tree.dragging = True
            return ((tkinterdnd2.ASK, tkinterdnd2.COPY), (tkinterdnd2.DND_FILES, tkinterdnd2.DND_TEXT), data)
        else:
            return 'break'
    except:
        pass

tree.drop_target_register(tkinterdnd2.DND_FILES)
tree.dnd_bind('<<DropEnter>>', drop_enter)
tree.dnd_bind('<<DropPosition>>', drop_position)
tree.dnd_bind('<<DropLeave>>', drop_leave)
tree.dnd_bind('<<Drop>>', drop)
tree.drag_source_register(1, tkinterdnd2.DND_FILES)
tree.dnd_bind('<<DragInitCmd>>', drag_init)
tree.dnd_bind('<<DragEndCmd>>', drag_end)
#右クリックメニューバー
menu_top.add_cascade(label='音量を変える',menu=menu_2nd,under=5)
menu_top.add_separator()
menu_top.add_cascade(label='一時停止/一時停止解除',command=pausef)
menu_2nd.add_command(label='0.0',command=lambda:clickvolume(0))
menu_2nd.add_command(label='0.1',command=lambda:clickvolume(1))
menu_2nd.add_command(label='0.2',command=lambda:clickvolume(2))
menu_2nd.add_command(label='0.3',command=lambda:clickvolume(3))
menu_2nd.add_command(label='0.4',command=lambda:clickvolume(2+2))
menu_2nd.add_command(label='0.5',command=lambda:clickvolume(5))
menu_2nd.add_command(label='0.6',command=lambda:clickvolume(6))
menu_2nd.add_command(label='0.7',command=lambda:clickvolume(7))
menu_2nd.add_command(label='0.8',command=lambda:clickvolume(8))
menu_2nd.add_command(label='0.9',command=lambda:clickvolume(9))
menu_2nd.add_command(label='1.0',command=lambda:clickvolume(10))

def sizechange(size):
    moviewindow.geometry(str(size))
    moviewindow.update_idletasks()
    video.sizechange(int(moviewindow.winfo_width()+5),int(moviewindow.winfo_height()+5))
def maxsize():
    moviewindow.overrideredirect(0)
    zoomset.set(not zoomset.get())
    moviewindow.attributes("-fullscreen",zoomset.get())
    moviewindow.update_idletasks()
    video.sizechange(int(moviewindow.winfo_width()+5),int(moviewindow.winfo_height()+5))
def changetitle():
    pass
zoomset = tk.BooleanVar()
zoomset.set(False)
menu_top.add_cascade(label='画面サイズを変える',menu=menu_3nd,under=5)
menu_3nd.add_command(label='500x300',command=lambda:sizechange("500x300"))
menu_3nd.add_command(label="800x500",command=lambda:sizechange("800x500"))
menu_3nd.add_command(label='1200x720',command=lambda:sizechange('1200x720'))
menu_3nd.add_command(label='1500x820',command=lambda:sizechange('1500x820'))
menu_3nd.add_command(label='1980x1080',command=lambda:sizechange('1980x1080'))
menu_3nd.add_command(label='最大化/最大化解除',command=maxsize)
menu_top.add_cascade(label='タイトルを表示する/しない',command=changetitle)
def on_closing():
    try:
        video.stop()
    except:
        pass
    try:
        audio.stop()
    except:
        pass
    endset.set(True)
    try:
        shutil.rmtree(os.path.dirname(__file__) + "\\tempfile\\tempplaylistdir")
    except:
        import traceback
        traceback.print_exc()
    try:
        with open(mypath + "\\usefile.log",mode='wt',encoding='utf-8') as usedata:
            json.dump(uselist,usedata,ensure_ascii=False, indent=2)
    except:
        pass
    root.destroy()
root.protocol("WM_DELETE_WINDOW", on_closing)
def popup():
    popwindiw.deiconify()
    root.withdraw()
tree.pack(fill=tk.BOTH,expand=True)
setbtnlbl = tk.LabelFrame(mainframe,text="そのほか",width=30)
setbtnlbl.pack(fill=tk.BOTH)
btn = tk.Button(setbtnlbl,text="プレイリスト設定",font=("",10),width=20,fg="blue",command=buttonbox)
btn.pack(fill=tk.BOTH,expand=True)
btn = tk.Button(setbtnlbl,text="操作パネル変更",font=("",10),width=20,fg="blue",command=popup)
btn.pack(fill=tk.BOTH,expand=True)
nowplaypath = tk.IntVar(master=root)
mp3maxset = tk.DoubleVar()
mp3changeset = tk.BooleanVar()
endset = tk.BooleanVar(master=root)
endset.set(False)
endcall = tk.BooleanVar(master=root)
endcall.set(False)
def linkclick(event):
    webbrowser.open("https://docs.python.org/ja/3/library/tkinter.html")
def linkclick2(event):
    webbrowser.open("https://www.pygame.org/docs/LGPL.txt")
def linkclick3(event):
    webbrowser.open("https://raw.githubusercontent.com/boppreh/keyboard/master/LICENSE.txt")
class MyDialog(simpledialog.Dialog):
    def buttonbox(self):
        self.resizable(0,0)
        self.attributes("-topmost",True)
        box = tk.Frame(self)
        lbl = tk.Label(box,text="主要ライブラリ",font=("",15))
        lbl.grid(row=0,column=0)
        tklbl = tk.Label(box,text="tkinter  GUIライブラリ",font=("",15),fg="blue")
        tklbl.grid(row=1,column=0)
        tklbl.bind("<1>",linkclick)
        tklbl2 = tk.Label(box,text="pygame  mp3再生のため",font=("",15),fg="blue")
        tklbl2.grid(row=2,column=0)
        tklbl2.bind("<1>",linkclick2)
        tklbl3 = tk.Label(box,text="keyboard  キーのフックのため",font=("",15),fg="blue")
        tklbl3.grid(row=3,column=0)
        tklbl3.bind("<1>",linkclick3)
        lisencelbl = tk.LabelFrame(box,text="ライブラリのライセンス")
        lisencelbl2 = tk.Label(lisencelbl,text=
        """Copyright（c）2016 Lucas Boppre Niehues
        Copyright（c）2014-2017 Tom Wallroth
        Copyright（C）1991、1999 Free Software Foundation、Inc。
        Copyright © 2001-2020 Python Software Foundation; All Rights Reserved"""
        ,font=("",13),fg="green")
        lisencelbl2.grid(row=0,column=0)
        lisencelbl.grid(row=5,column=0)
        box.pack()
def vdata(root=root):
    d = MyDialog(root)
def datad(root=root):
    d = dataDialog(root)
men = tk.Menu(root) 
root.config(menu=men)
menu_file = tk.Menu(root)
men.add_cascade(label='music-playerについて',command=vdata)
men.add_cascade(label='ファイル情報',command=datad)
men.add_cascade(label='ファイル使用履歴',command=logwindow)
global pausechkset,upset,downset,musicdata,fdata2,uselist
useist = []
with open(mypath + "\\usefile.log",mode='rt',encoding='utf-8') as usedata:
    uselist = json.load(usedata)
fdata2 = []
pausetkey = tk.StringVar()
pausetkey.set(config_ini['keydata']['pausekey'])
volupkey = tk.StringVar()
volupkey.set(config_ini['keydata']['volupkey'])
voldownkey = tk.StringVar()
voldownkey.set(config_ini['keydata']['voldownkey'])
sleepset = tk.DoubleVar()
sleepset.set(0.05)

soundplayset = tk.BooleanVar(master=root)
soundplayset.set(False)
pausechkset = tk.BooleanVar(master=root)
pausechkset.set(True)
upset = tk.BooleanVar(master=root)
upset.set(True)
downset = tk.BooleanVar(master=root)
downset.set(True)
def keyhook():
    while True:
        try:
            if pausechkset.get():
                if keyboard.is_pressed(pausetkey.get()):
                    pausef()
            else:
                pausetkey.set(str(keyboard.read_key()))
            if upset.get():
                if keyboard.is_pressed(volupkey.get()):
                    if 1.0 >= setvar.get():
                        setvar.set(setvar.get()+0.01)
                        volumechange(1)
            else:
                volupkey.set(str(keyboard.read_key()))
            if downset.get():
                if keyboard.is_pressed(voldownkey.get()):
                    if 0 <= setvar.get():
                        setvar.set(setvar.get()-0.01)
                        volumechange(1)
            else:
                voldownkey.set(str(keyboard.read_key()))
            time.sleep(sleepset.get())
        except:
            pass

keyth = threading.Thread(target=keyhook)
keyth.setDaemon(True)
keyth.start()
popwindiw = tk.Toplevel()
popwindiw.attributes("-topmost",True)
popwindiw.resizable(0,0)
popsetlbl = tk.LabelFrame(popwindiw)
popsetlbl.pack(fill=tk.BOTH,expand=True)
stopsetbtn = tk.Button(popsetlbl,text="⏸",font=("",20),command=pausef)
stopsetbtn.pack(fill=tk.BOTH,expand=True)
popscale = tk.Scale(master=popsetlbl,showvalue=True,variable=setvar,from_=0,to_=1,tickinterval=True,orient="horizontal",resolution=0.1,command=volumechange)
popscale.pack(fill=tk.BOTH,expand=True)
poptimelbl = tk.Label(popsetlbl,textvariable=soundset)
popnowlbl = tk.Label(popwindiw)
popnowlbl.pack(fill=tk.BOTH,expand=True)
poptimelbl.pack(fill=tk.BOTH,expand=True)
popwindiw.withdraw()
def popclose():
    root.deiconify()
    popwindiw.withdraw()
popwindiw.protocol("WM_DELETE_WINDOW", popclose)

try:
    os.makedirs("tempfile/audio")
except:
    pass
try:
    os.makedirs("tempfile\\tempplaylistdir")
except:
    pass

try:
    fp = sys.argv[1]
    if fp.endswith('.playlist'):
        lenlist = []
        lenlist.clear()
        playdata = []
        flist = glob.glob(str(os.path.dirname(__file__) + "\\tempfile\\tempplaylistdir") + "/**.mp4",recursive=True)
        for fname in flist:
            os.remove(str(fname))
        with open(str(fp),"r",encoding="utf-8") as readplay:
            playdatatemp = readplay.readlines()
        a = 1 
        while True:
            try:
                if len(playdatatemp) < a:
                    break
                base64decodef(str(str(os.path.dirname(__file__) + "\\tempfile\\tempplaylistdir") + "\\" + playdatatemp[a]).replace("\n",""),str(playdatatemp[a+1]))
                a = a + 2
            except:
                a = a + 2
        for i in tree.get_children():
            tree.delete(i)
        flist = glob.glob(str(os.path.dirname(__file__) + "\\tempfile\\tempplaylistdir") + "/**.mp4",recursive=True)
        count = 0
        fdata2.clear()
        for data in flist:
            try:
                audio = MP3(str(data))
                mp3len = str(round(audio,0)) +  "秒"
                count = count + 1
                tree.insert("", "end", values=(str(os.path.basename(data)), str(data),str(mp3len),"デフォルト"))
                fdata2.append(str(data))
                fdata2.append(audio)
            except:
                pass
    elif fp.endswith('.mp4'):
        data = fp
        audio = MP3(str(data))
        mp3len = str(round(audio,0)) +  "秒"
        tree.insert("", "end", values=(str(os.path.basename(data)), str(data),str(mp3len),"デフォルト"))
        fdata2.append(str(data))
        fdata2.append(audio)
        usejsonadd(str(data))
        setvar.set(0.3)
        volumechange(0.3)
        loopstart(0,0)
except:
    pass
def makename(dirpath,extension):
    count = 0
    while True:
        count += 1
        fpath = dirpath + "\\download" + str(count) + str(extension)
        if os.path.exists(fpath):
            pass
        else:
            break
    return fpath

temppath = mypath + "\\tempfile\\ytdl-temp"
savedir.set(temppath)
try:
    os.mkdir(temppath)
except:
    pass
try:
    for rootdir,subdir,files in os.walk(temppath):
        for file in files:
            delpath = os.path.join(rootdir,file)
            try:
                os.remove(delpath)
            except:
                pass
except:
    pass
try:
    dlwin.withdraw()
except:
    pass
root.deiconify()
root.update_idletasks()

root.mainloop()
