#!/usr/bin/env python
# @author = 53 68 79 61 6D 61 6C 
# date	  = 06/08/2017

"""
This script organize my songs according to their download time and create a symlink to each song in music folder.
"""

import os

def main():
    path = '/media/shyamal/Windows/Users/Shyamal/Music'         # path to folder containing all the songs
    songs = []
    for folder, subfolder, files in os.walk(path):
        for filename in files:
            if filename != 'desktop.ini':
                filepath = os.path.join(folder, filename)
                songs.append(filepath)  
    songs.sort(key=os.path.getctime, reverse=True)
    dst = '/home/shyamal/Music'                                 # path to folder in which we need to create symlink
    for files in os.listdir(dst):
        os.remove(os.path.join(dst, files))
    for num, song in enumerate(songs):
        fname = song.split('/')[-1]
        fname = str(num+1) + '  ' + fname
        link = os.path.join(dst, fname)
        os.symlink(song, link)
if __name__ == "__main__":
    main()
