# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 19:12:39 2021

@author: jahtzee
"""

from os import *
from moviepy.editor import *
path = "C:/Users/admin/Music/tmp"
output = "C:/Users/admin/Music/tmp/output"

def extractMP3fromMP4(mp4, mp3):
    videoclip=VideoFileClip(mp4)
    audioclip=videoclip.audio
    audioclip.write_audiofile(mp3)
    audioclip.close()
    videoclip.close()
    
if __name__ == "__main__":
    filelist = listdir(path)
    for file in filelist:
        if file.endswith(".mp4"):
            extractMP3fromMP4(path+"/"+file, output+"/"+file+'.mp3')
            
    