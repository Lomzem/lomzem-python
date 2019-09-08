import os
import shutil
import re


os.chdir('C:/Users/Lomzem/Desktop/AbstractMusic/')
for song_file in os.listdir():
	# song_file, song_ext = os.path.splitext(song_file)
	new_song_title = re.sub(r'\s\(Prod\..+?(?=\))\)', '', song_file)
	print(repr(new_song_title))
	os.rename(song_file, new_song_title)