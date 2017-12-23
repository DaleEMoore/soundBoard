#!/usr/bin/env python2

# From: https://www.reddit.com/r/beginnerprojects/comments/4mwwxx/soundboard_x_post_rlearnpython/
# From: https://pastebin.com/TUm3L2PX

'''
Does not work on python 3 (yet)
Program finds all wav files in current directory and adds them to the soundboard
   TODO:  add sound directory with several different subdirectories
   for different soundboards. I couldn't get this to work this morning
   so I'll try again later
Example Sounds: https://drive.google.com/file/d/0B6px7XJxu6qYYjg0Y0l1T2oxeFk/view?usp=sharing
'''
import os
import Tkinter
# import winsound # Windows sound player. I should find something for Linux too. Maybe kivy or pygame.

soundlist = os.listdir(os.curdir)


def playsoundfunction(soundfile):
    def functiontemplate(*args):
        winsound.PlaySound(soundfile, winsound.SND_ASYNC | winsound.SND_FILENAME)

    return functiontemplate


top = Tkinter.Tk()
for item in soundlist:
    if "wav" in item:
        soundfile = item
        soundfunction = item.split(".")[0]
        soundcommand = item.split(".")[0]
        buttonname = soundcommand.replace("_", " ")
        soundfunction = playsoundfunction(soundfile)
        soundcommand = Tkinter.Button(top, text=buttonname, command=soundfunction)
        soundcommand.pack()

top.mainloop()