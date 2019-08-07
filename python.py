import os
import re

os.chdir('C:/Users/Lomzem/Desktop/Documents By Readdle/Game Grumps - Detroit Become Human')

for file in os.listdir():
	game, title, part, show = file.split(' - ')
	show, ext = show.split('.')
	part = part.title()
	new_name = f'{part} - {title}.{ext}'
	os.rename(file, new_name)