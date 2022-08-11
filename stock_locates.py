import pandas as pd
import os
import re

def main():
	os.chdir('C:/Users/Lomzem/Desktop/')
	csv_file = [file for file in os.listdir() if file.startswith('CashJournal')][0]
	data = pd.read_csv(csv_file)
	df = pd.DataFrame({'Ticker': [], 'Locate': []})

	for index, row in data.iterrows():
		ticker = re.findall(r'(?:Locate \d+\ |Locate credit \d+\ )(\w+)', row.Note)[0]
		value = row.Withdraw - row.Deposit
		df = pd.concat([df, pd.DataFrame({'Ticker': [ticker], 'Locate': [value]})])
	
	# print(df)
	print(df.groupby('Ticker').sum())
	os.system('pause')

main()