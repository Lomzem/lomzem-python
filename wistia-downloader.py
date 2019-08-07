import json
import os
import pyperclip
import re
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen


class WistiaDL:
    def __init__(self):
        self.downloadPath = 'C:/Users/Lomzem/Desktop/Documents By Readdle/Boiler Room Trading'
        os.chdir(self.downloadPath)

    def run(self):
        embedLink = pyperclip.paste()
        wvideoID = re.search(r'\?wvideo=([a-zA-Z0-9]+)"', embedLink).group(1)
        link = 'https://fast.wistia.com/embed/iframe/' + wvideoID

        website = urlopen(link)
        webHTML = website.read()
        website.close()

        videoTitle = re.findall(r'<a href="[a-zA-Z0-9:/.=?&-]+">([a-zA-Z0-9|/\s;:&()#.?"!\'-]+)</a>', embedLink)[0]
        videoTitle = videoTitle.replace('&amp;', '&')
        videoTitle = videoTitle.replace(' | ', ' - ')
        videoTitle = re.sub(r'(\\|/|:|\*|\?|"|<|>)', '', videoTitle)

        soupPage = soup(webHTML, 'html.parser')
        webScript = soupPage.findAll('script')[4].string
        videoJson = re.findall(r'"type":"original".+?(?=,"created_at")', webScript)[0]
        videoJson = f'{{{videoJson}}}'
        videoJson = json.loads(videoJson)
        videoLink = videoJson['url'][:-3] + videoJson['ext']
        videoTitle = videoTitle + '.' + videoJson['ext']

        os.system(f'pget "{videoLink}" "{videoTitle}"')

if __name__ == '__main__':
    WistiaDL().run()