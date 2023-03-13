from requests import get


# api_key is generated from etherscan account
API_KEY = "4DVP4GJ5CG8JDPGD6ZQJ3HYCPDTCVAAA7E"
BASE_URL = "https://api.etherscan.io/api"
ETHER_VALUE = 10 ** 18

# function to create api url from BASE_URL and others parameters

def make_api_url(module, action, address, **kwargs):
	url = BASE_URL + f"?module={module}&action={action}&address={address}&apikey={API_KEY}"

	for key, value in kwargs.items():
		url += f"&{key}={value}"

	return url


# function to create url and get data from json file - it comes from etherscan documentations     
# in value divide by ETHER_VALUE
def get_account_balance(address):
	balance_url = make_api_url("account", "balance", address, tag="latest")
	response = get(balance_url)
	data = response.json()

	value = int(data["result"]) / ETHER_VALUE
	return value

address = '0x5F927395213ee6b95dE97bDdCb1b2B1C0F16844F'
eth = get_account_balance(address)
print(eth)