import os
import re

os.chdir('C:/Users/Lomzem/Desktop/Tokyo Ghoul/Season 2')

epNames = ['Those Who Hunt']
for file in os.listdir():
	epNum = re.findall(r'Episode\s(\d+)', file)[0]
	epNum = int(epNum) - 1
	newName = (f'{file[:-4]} - {epNames[epNum]}.mp4')
	os.rename(file, newName)