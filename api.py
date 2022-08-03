import json
import requests

#Assign the free api key to a variable to add in th website later
api_key= "DAL5U3E14Y45E3DK"
#The URL link with the function, from_currency and to_currency correctly assigned
url=f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey={api_key}"
#This line allows me to access the data from alphavantage
response=requests.get(url)
#Use . json() to retrieve data and stored as JSON object from the API.
#Python will convert the JSON object as dictionary automatically.
data=response.json()
<<<<<<< HEAD
#Lastly, I access the current exchange rate from USD to SGD. 
#If you look at the nested dictionary, it starts with "Realtime Currency Exchange Rate", thus I access that first.
#Next I access the current exchange rate hidden behind "5. Exchange Rate"
#Then I just print out the exchange rate 
print(data["Realtime Currency Exchange Rate"]["5. Exchange Rate"])


=======
# print(json.dumps(data, indent=4))
# print(len(data["Time Series FX (Weekly)"]))
open_list=[]
for date in data["Time Series FX (Weekly)"]:
    open_list.append(data["Time Series FX (Weekly)"][date]["1. open"])
    open_list.append(data["Time Series FX (Weekly)"][date]["2. high"])
    open_list.append(data["Time Series FX (Weekly)"][date]["3. low"])
    open_list.append(data["Time Series FX (Weekly)"][date]["4. close"])

empty_list=[]
for number in open_list:
    number=float(number)
    empty_list.append(number)
average_USD_to_SGD=(sum(empty_list)/len(open_list))
print(f"[REAL TIME CURRENCY CONVERSION RATE] USD1 = SGD{average_USD_to_SGD}")
>>>>>>> 44b33ac542fb9a902930648499a859438a17cf01
