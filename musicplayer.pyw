import pygame,os
import tkinter as tkr
from tkinter.filedialog import askdirectory


musicplayer = tkr.Tk()
musicplayer.title("MusPlayer")
musicplayer.geometry("420x360")


directory = askdirectory()
os.chdir(directory)
songlist = os.listdir()
playlist = tkr.Listbox(musicplayer,font="Helvetica 12 bold",bg="RoyalBlue3",selectmode=tkr.SINGLE)

for item in songlist:
    pos = 0
    playlist.insert(pos,item)
    pos = pos + 1

pygame.init()
pygame.mixer.init()


def play():
    pygame.mixer.music.load(playlist.get(tkr.ACTIVE))
    var.set(playlist.get(tkr.ACTIVE))
    pygame.mixer.music.play()

#pygame.mixer.music.load is the pygame module for controlling the streamed audio and also to load the music files to playback

def exitMP():
    pygame.mixer.music.stop()

def pause():
    pygame.mixer.music.pause()

def unpause():
    pygame.mixer.music.unpause()


button1 = tkr.Button(musicplayer,width=5,height=3,font="Helvetica 12 bold",text="PLAY",command=play,bg="PaleVioletRed1",fg="olive drab")
button2 = tkr.Button(musicplayer,width=5,height=3,font="Helvetica 12 bold",text="EXIT",command=exitMP,bg="medium sea green",fg="LightSkyBlue4")
button3 = tkr.Button(musicplayer,width=5,height=3,font="Helvetica 12 bold",text="PAUSE",command=pause,bg="burlywood2",fg="coral3")
button4 = tkr.Button(musicplayer,width=5,height=3,font="Helvetica 12 bold",text="RESUME",command=unpause,bg="HotPink2",fg="SlateGray3")

var = tkr.StringVar()
songtitle = tkr.Label(musicplayer,textvariable=var,font="Helvetica 12 bold")

songtitle.pack()

button1.pack(fill="x")
button2.pack(fill="x")
button3.pack(fill="x")
button4.pack(fill="x")
playlist.pack(fill="both",expand="yes")


musicplayer.mainloop()

