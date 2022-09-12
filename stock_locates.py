import pandas as pd
import os
import re
import pyperclip

def main():
	os.chdir('C:/Users/Lomzem/Desktop/')
	df = pd.DataFrame({'Date': [], 'Ticker': [], 'Locate': []})

	all_files = [file for file in os.listdir() if file.startswith('CashJournal')]
	for csv_file in all_files:
		data = pd.read_csv(csv_file)

		for index, row in data.iterrows():
			if row.Note == 'ZeroPro' or row.Note.startswith('ACH'):
				continue
			date = pd.to_datetime(row['E/D']).date()
			ticker = re.findall(r'(?:Locate [\d.]+\ |Locate credit [\d.]+\ |Borrow [\d.]+\ )(\w+)', row.Note)[0]
			value = row.Withdraw - row.Deposit
			entry = pd.DataFrame({'Date': [date], 'Ticker': [ticker], 'Locate': [value]})
			# print(entry)
			df = pd.concat([df, entry])
	
	# df.sort_values('Ticker', inplace=True)
	df = df.groupby(['Date', 'Ticker']).sum()
	print(df)

	final_text = ''

	for index, row in df.iterrows():
		# print(row)
		# print(row.Locate)
		final_text += f'\n{row.Locate}'

	final_text = final_text[1:]
	pyperclip.copy(final_text)
	# print(repr(final_text))
	os.system('pause')

main()