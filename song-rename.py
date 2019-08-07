import os
import sys
from mutagen.mp4 import MP4, MP4Cover


class SongRename():
	def __init__(self):
		# self.song_path = 'C:/lomzem-songs'
		try:
			self.song_path = sys.argv[1]
		except IndexError:
			self.song_path = input('Folder\n\n> ').strip('"')

	def title_separator(self, filename):
		artist, title = filename.split(' - ')
		title, file_ext = os.path.splitext(title)

		# BANNED CHARACTERS
		title = title.replace('{COLON}', ':')
		title = title.replace('{SLASH}', '/')
		title = title.replace('{ASTERISK}', '*')

		artist = artist.replace('{COLON}', ':')
		artist = artist.replace('{SLASH}', '/')
		artist = artist.replace('{ASTERISK}', '*')

		return (artist, title, file_ext)

	def update_metadata(self, file_data, filename):
		artist, title, file_ext = file_data
		audio = MP4(filename)
		audio['©ART'] = artist
		audio['©nam'] = title
		audio['©alb'] = title
		try:
			del audio['©cmt']
		except KeyError:
			pass
		try:
			del audio['©day']
		except KeyError:
			pass
		audio.save(filename)

	def main(self):
		os.chdir(self.song_path)
		for file in os.listdir():
			if file.endswith('.m4a'):
				file_data = self.title_separator(file)
				self.update_metadata(file_data, file)


if __name__ == '__main__':
	SongRename().main()
