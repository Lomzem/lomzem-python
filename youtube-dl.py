import os
import pyperclip
import sys

youtube_url = pyperclip.paste()
arguments = sys.argv

# By default, youtube-dl will extract a single video
EXTRACT_AUDIO = True
SINGLE_OR_PLAYLIST = 'single'

for arg in arguments[1:]:
	if arg == 'help':
		print('Current Options: "single", "playlist", "audio"\nBy default: Downloads single video')
		exit()
	elif arg == 'single':
		SINGLE_OR_PLAYLIST = 'single'
	elif arg == 'playlist':
		SINGLE_OR_PLAYLIST = 'playlist'
	elif arg == 'audio':
		EXTRACT_AUDIO = True

final_arguments = ''

if EXTRACT_AUDIO == True:
	final_arguments += '--extract-audio '

if SINGLE_OR_PLAYLIST == 'single':
	final_arguments += '--no-playlist '

elif SINGLE_OR_PLAYLIST == 'playlist':
	final_arguments += '--yes-playlist '

if EXTRACT_AUDIO == False:
	os.system(f'youtube-dl --format "bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4" --output "%(title)s.%(ext)s" {final_arguments}"{youtube_url}"')

elif EXTRACT_AUDIO == True:
	os.system(f'youtube-dl --format "bestaudio[ext=m4a]" --output "%(title)s.%(ext)s" {final_arguments}"{youtube_url}"')