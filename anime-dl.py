import os
import re
import sys
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup


if len(sys.argv) < 3:
	print('\n\nERROR!')
	print('Correct Usage: gogoa-dl.py <url> <episode range> <output_folder>')
	print('EX: gogoa-dl.py "https://www7.gogoanime.io/tokyo-ghoul-episode-1" 1-12 C:/Users/Lomzem/Desktop')

else:
	anime_link = sys.argv[1]
	episode_range = sys.argv[2].split('-')
	output_folder = sys.argv[3]

	first_episode = int(episode_range[0])
	last_episode = int(episode_range[-1])
	anime_link = re.sub(r'episode-\d+', 'episode-', anime_link)
	os.chdir(output_folder)

	for episode_number in range(first_episode, last_episode+1):
		episode_link = anime_link + str(episode_number)

		# episode_website_req = Request(episode_link, headers={'User-Agent': 'Mozilla/5.0'})
		episode_website = urlopen(Request(episode_link, headers={'User-Agent': 'Mozilla/5.0'}))
		# episode_website = urlopen(episode_link)
		episode_html = episode_website.read()
		episode_website.close()

		soup_page = soup(episode_html, 'html.parser')
		a_tag = soup_page.find('div', class_='download-anime').findChild()
		a_tag = str(a_tag)
		download_page = re.findall(r'href="(\S+)"', a_tag)[0]

		dl_page_website = urlopen(Request(download_page, headers={'User-Agent': 'Mozilla/5.0'}))
		dl_page_html = dl_page_website.read()
		dl_page_website.close()

		dl_page_soup = soup(dl_page_html, 'html.parser')
		download_link = dl_page_soup.find('div', class_='dowload').findChild()
		download_link = str(download_link)
		download_link = re.findall(r'href="(.+?(?="))', download_link)[0]
		download_link = download_link.replace(' ', '%20')
		download_link = download_link.replace('&amp', '&')
		download_link = download_link.replace(';', '')
		os.system(f'pget "{download_link}", "Episode {episode_number}.mp4"')