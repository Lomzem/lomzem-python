import os
import shutil

for file in os.listdir():
	if file.endswith('.m4a'):
		shutil.move(file, 'newest-songs/')
	elif file.endswith('.png') or file.endswith('.jpg') or file.endswith('.jpeg'):
		shutil.move(file, 'song-pics/')