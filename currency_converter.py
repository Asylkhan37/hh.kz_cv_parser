import urllib3
import json

api_token = 'b1fa01d084187ca69fe378dd'
url = f"https://v6.exchangerate-api.com/v6/b1fa01d084187ca69fe378dd/latest/USD"
 
def convertTenge():
	return json.loads(urllib3.PoolManager().request('GET', url).data)['conversion_rates']['KZT']
def convertEuro():
	return json.loads(urllib3.PoolManager().request('GET', url).data)['conversion_rates']['EUR']
def convertRuble():
	return json.loads(urllib3.PoolManager().request('GET', url).data)['conversion_rates']['RUB']
def convertSom():
	return json.loads(urllib3.PoolManager().request('GET', url).data)['conversion_rates']['KGS']

if __name__ == "__main__":
	pass	