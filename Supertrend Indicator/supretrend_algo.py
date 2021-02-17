import pandas as pd
import zrd_login
import pdb
import datetime
import indicators

kite = zrd_login.kite



def data_downloader(name, interval, delta):

	token = kite.ltp('NSE:'+ name)['NSE:'+ name]['instrument_token']
	to_date = datetime.datetime.now().date()
	from_date = to_date - datetime.timedelta(days = delta)
	data = kite.historical_data(instrument_token = token , from_date = from_date, to_date = to_date, interval = interval , continuous=False, oi=False)
	df = pd.DataFrame(data)
	return df


watchlist = ['ACC', 'CIPLA', 'GAIL', 'AXISBANK']

for name in watchlist:
	df = data_downloader(name,  '5minute', 10)
	df = indicators.SuperTrend(df = df, period = 7, multiplier = 3, ohlc=['open', 'high', 'low', 'close'])
	final_st_value = round(df.iloc[-1]['ST_7_3'], 1)
	final_st_dirn = df.iloc[-1]['STX_7_3']

	print(f"for {name} final_st_value , {final_st_value} , and dirn is {final_st_dirn}")

	if final_st_dirn == "up":
		buy


	if final_st_dirn == "sell":
		buy

	# pdb.set_trace()

	