import re
import requests
import pyperclip
import time
from datetime import datetime
from win10toast import ToastNotifier

class AfterMarketScanner:
	def __init__(self, scanner_link):
		self.scanner_link = scanner_link
		self.loopNum = 0
		self.all_quotes = []
		self.returned_value = []

	def get_quotes(self, website_HTML):
		all_quotes = re.findall(r"quote\.ashx\?t=([A-Z]+)", website_HTML)
		all_quotes = list(dict.fromkeys(all_quotes))
		self.all_quotes += all_quotes
		if len(all_quotes) == 20:
			self.loopNum += 1
			self.main()
		else:
			self.loopNum = 0
			self.main(finished=True)

	def main(self, finished=False):
		if finished == False:
			if self.loopNum == 0:
				website_HTML = requests.get(self.scanner_link).text
			else:
				website_HTML = requests.get(self.scanner_link + "&r=" + str(self.loopNum*20+1)).text
			self.get_quotes(website_HTML)
		if finished == True:
			# completed_quote_list = str(self.all_quotes)[1:-1].replace("'", "")
			# pyperclip.copy(completed_quote_list)
			# print(f"{completed_quote_list}\n\nCopied {len(self.all_quotes)} Tickers to Clipboard!\n")
			self.returned_value = self.all_quotes

if __name__ == '__main__':
	print('Momentum Scanner\n')
	cached_tickers = []
	i = 0
	while i != 1:
		test = AfterMarketScanner("https://finviz.com/screener.ashx?v=111&f=sh_curvol_o500,ta_changeopen_u3&ft=4")
		test.main()
		for item in test.returned_value:
			if item not in cached_tickers:
				# current_time = datetime.now().strftime('%I:%M %p %m/%d/%y')
				current_time = datetime.now().strftime('%I:%M %p')
				print(f'{current_time} >> FOUND "{item}"')
				ToastNotifier().show_toast('Momentum Scanner', f'Found Ticker: "{item}"', duration=10)
				cached_tickers.append(item)
		time.sleep(20)