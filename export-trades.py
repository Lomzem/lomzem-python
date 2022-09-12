import os
import pandas as pd
import pyperclip

os.chdir('C:/Users/Lomzem/Desktop/')

file = [file for file in os.listdir() if file.startswith('tz')][-1]
final_text = ''

df = pd.read_excel(file)
tab = '\t'
print(df)
# df.sort_values('Symbol', inplace=True)

print(df)

for index, row in df.iterrows():
	final_text += f'{row.PriceIn}{tab}{row.PriceOut}{tab*2}{row["Shares In"]}\n'

pyperclip.copy(final_text)
os.system('pause')