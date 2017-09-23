# Music Organizer
Many times I want to sort my song according to the time I downloaded them, this is because we tend to 
hear latest songs more.
All of my downloaded songs are in windows partition because it is accessible in both OS. 
I download songs from `YouTube` using `youtube-dl`, so all the songs are organized in directories by the name of uploader.

This script organize my songs according to their download time and create a symlink to each song in music folder.

# Usage
If you want to use the script you must have `python2` or `python3` installed.

All you need to do is to change the path of destination and source folder in the code.

You can give run permission to the script using `chmod +x path/to/music.py` and 
add `alias music="path/to/music.py` into your `.bashrc` file.
Now whenever you write `music` on your terminal it will organize your songs.

**Caution**: make sure the destination directory is empty and doesn't contain any valuable info.
Each time you run the script it will delete all the files in the destination folder.