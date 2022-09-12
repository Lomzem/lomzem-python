import os
import pandas as pd

os.chdir('C:/Users/Lomzem/Desktop')
file = [file for file in os.listdir() if file.startswith('TradeHistory')][0]

df = pd.read_csv(file)

sdf = df.loc[(df.Side == 'SS')]
cdf = df.loc[(df.Side == 'BC')]

def w_avg(dataf):
	dataf['WX'] = dataf.Qty * dataf.Price
	w_avg = dataf.WX.sum() / dataf.Qty.sum()
	return w_avg

final_text = f'Entry: {w_avg(sdf)}\nExit: {w_avg(cdf)}'
print(final_text)