from kiteconnect import KiteConnect
from kiteconnect import KiteTicker
import pdb
import pandas as pd
import datetime
import os


api_k = "put_your_api_key_here"  # api_key
api_s = "put_your_api_secret_here"  # api_secret
filename = str(datetime.datetime.now().date()) + ' token' + '.txt'




def read_access_token_from_file():
	file = open(filename, 'r+')
	access_token = file.read()
	file.close()
	return access_token


def send_access_token_to_file(access_token):	
	file = open(filename, 'w')
	file.write(access_token)
	file.close()


def get_login(api_k, api_s):
	global kws, kite
	kite = KiteConnect(api_key=api_k)
	print("Logging into zerodha")


	if filename not in os.listdir():

		print("you haven't logged it for today")
		print("[*] Generate Request Token : ", kite.login_url())
		request_tkn = input("[*] Enter Your Request Token Here : ")
		data = kite.generate_session(request_tkn, api_secret=api_s)
		access_token = data["access_token"]
		kite.set_access_token(access_token)
		kws = KiteTicker(api_k, access_token)
		send_access_token_to_file(access_token)

	elif filename in os.listdir():
		access_token = read_access_token_from_file()
		kite.set_access_token(access_token)
		kws = KiteTicker(api_k, access_token)
		print("You have already loggged in for today")

	return kite

kite = get_login(api_k, api_s)


niftyfno = ["PFC", "TITAN", "RECLTD", "JUBLFOOD", "EXIDEIND", "BOSCHLTD", "SUNTV", "MARUTI", "HINDUNILVR", "IBULHSGFIN", "MUTHOOTFIN", "PETRONET", "SUNPHARMA", "GODREJPROP", "LUPIN", "APOLLOHOSP", "AMARAJABAT", "DRREDDY", "CADILAHC", "TORNTPOWER", "DABUR", "ASIANPAINT", "TATACHEM", "CIPLA", "SHREECEM", "COALINDIA", "IGL", "BIOCON", "MGL", "TATACONSUM", "INFY", "M&M", "PNB", "MRF", "INFRATEL", "DLF", "BALKRISIND", "ICICIPRULI", "TVSMOTOR", "RAMCOCEM", "HEROMOTOCO", "RELIANCE", "CUMMINSIND", "DIVISLAB", "ESCORTS", "BRITANNIA", "NESTLEIND", "ZEEL", "GLENMARK", "GRASIM", "GMRINFRA", "UBL", "IDEA", "M&MFIN", "SBILIFE", "BATAINDIA", "AUROPHARMA", "BERGEPAINT", "HAVELLS", "VOLTAS", "GODREJCP", "TORNTPHARM", "MANAPPURAM", "ACC", "BHARATFORG", "MARICO", "PIDILITIND", "GAIL", "ICICIGI", "UPL", "NATIONALUM", "ADANIPORTS", "NMDC", "BHEL", "HDFCBANK", "APOLLOTYRE", "HCLTECH", "BAJAJ-AUTO", "PEL", "KOTAKBANK", "JSWSTEEL", "CONCOR", "MFSL", "JINDALSTEL", "WIPRO", "COFORGE", "L&TFH", "BEL", "ADANIENT", "ITC", "VEDL", "ULTRACEMCO", "BANKBARODA", "ASHOKLEY", "POWERGRID", "TATASTEEL", "ONGC", "HINDPETRO", "SAIL", "AMBUJACEM", "HDFC", "MCDOWELL-N", "TCS", "BHARTIARTL", "TECHM", "PAGEIND", "LICHSGFIN", "NAUKRI", "BPCL", "COLPAL", "LT", "AXISBANK", "TATAMOTORS", "SBIN", "CHOLAFIN", "SRTRANSFIN", "ICICIBANK", "HDFCLIFE", "SRF", "SIEMENS", "NTPC", "FEDERALBNK", "BAJFINANCE", "IDFCFIRSTB", "TATAPOWER", "MINDTREE", "INDUSINDBK", "MOTHERSUMI", "BAJAJFINSV", "HINDALCO", "EICHERMOT", "BANDHANBNK", "INDIGO", "CANBK", "IOC", "PVR", "RBLBANK"]
