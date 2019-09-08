import os

os.chdir('C:/lomzem-songs/combined/')

for file in os.listdir():
	artist, song = file.split(' - ')
	song, file_ext = os.path.splitext(song)

	search_query = 'you'

	search_query = search_query.lower()
	if search_query in song.lower():
		print(file)