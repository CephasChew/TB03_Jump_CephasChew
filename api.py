import json,requests
from pathlib import Path

def api_function():
   
   #Assign the free api key to a variable to add in the website later
   api_key= "DAL5U3E14Y45E3DK"
   #The URL link with the function, from_currency and to_currency correctly assigned
   url=f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey={api_key}"
   #This line allows me to access the data from alphavantage
   response=requests.get(url)
   #Use . json() to retrieve data and stored as JSON object from the API.
   #Python will convert the JSON object as dictionary automatically.
   data=response.json()
   #Lastly, I access the current exchange rate from USD to SGD. 
   #If you look at the nested dictionary, it starts with "Realtime Currency Exchange Rate", thus I access that first.
   #Next I access the current exchange rate hidden behind "5. Exchange Rate"
   #Then I just print out the exchange rate 
   xchange_rate=(data["Realtime Currency Exchange Rate"]["5. Exchange Rate"])
   #Making the value a float so it can be calculated later
   xchange_rate=float(xchange_rate)

   summary_path = Path.cwd()/"CSV_reports"/"summary_report.txt"
   with summary_path.open(mode="a", encoding="UTF-8", newline="") as file:
      file.write(f"[REAL TIME CURRENCY CONVERSION RATE] USD1 = SGD{xchange_rate}")
   #making a function
   def calculation(values):
      #xchange rate multipy by USD to get SGD
      new_value=xchange_rate*values
      #return the value after calculation
      return new_value

api_function()





    

