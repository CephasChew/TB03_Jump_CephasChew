import json
import requests

api_key= "DAL5U3E14Y45E3DK"
url=f"https://www.alphavantage.co/query?function=FX_WEEKLY&from_symbol=USD&to_symbol=SGD&apikey={api_key}"

response=requests.get(url)
data=response.json()
# print(json.dumps(data, indent=4))
# print(len(data["Time Series FX (Weekly)"]))
open_list=[]
for date in data["Time Series FX (Weekly)"]:
    open_list.append(data["Time Series FX (Weekly)"][date]["1. open"])
    open_list.append(data["Time Series FX (Weekly)"][date]["2. high"])
    open_list.append(data["Time Series FX (Weekly)"][date]["3. low"])
    open_list.append(data["Time Series FX (Weekly)"][date]["4. close"])
print(len(open_list))
empty_list=[]
for number in open_list:
    number=float(number)
    empty_list.append(number)
average_USD_to_SGD=(sum(empty_list)/len(open_list))
print(average_USD_to_SGD)