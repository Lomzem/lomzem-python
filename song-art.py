import os
from mutagen.mp4 import MP4, MP4Cover

artwork_path = 'C:/Users/Lomzem/Desktop/song-pics/'
song_path = 'C:/Users/Lomzem/Desktop/newest-songs/'

abspath_song = lambda file: song_path + file
abspath_art = lambda file: artwork_path + file

def get_pairs():
	pair_list = []

	for song_file in os.listdir(song_path):
		song_file_name, song_file_ext = os.path.splitext(song_file)

		for art_file in os.listdir(artwork_path):
			art_file_name, art_file_ext = os.path.splitext(art_file)

			if song_file_name == art_file_name:
				complete_pair = (abspath_song(song_file), abspath_art(art_file))
				pair_list.append(complete_pair)

	return pair_list

pair_list = get_pairs()

for pair in pair_list:
	song_file, art_file = pair

	audio = MP4(song_file)
	with open(art_file, 'rb') as f:
		audio['covr'] = [
			MP4Cover(f.read())
		]
	audio.save()