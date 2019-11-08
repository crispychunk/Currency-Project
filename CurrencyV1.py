#######################################
#       Currency Whatever we gonna call it                #
#                  Joshua and Crispin                                #
#                                                                                #
#                                                                                #
#######################################

#####################################################
# These are the required dependencies ########

import requests as r
import pandas as pd
import math 
######################################

### Avaiable Currency Chart ####
def Chart():
        
        print("""
Currently supported Base pair:
AUD      BGN      BRL     CAD      
CHF      CNY      CZK     DKK     
EUR      GBP      HKD     HRK    
HUF      IDR      ILS     INR     
ISK      JPY      KRW     MXN     
MYR      NOK      NZD     PHP     
PLN      RON      RUB     SGD      
THB      TRY      USD     ZAR     



""")
### Choose Base currency & call data ###
def DataRecieve():
        Chart()
        basechoice= input("What Base currency? -->")
        basechoice =  basechoice.upper()
        ticker = r.get("https://api.exchangeratesapi.io/latest?base=" + basechoice)
        # print(ticker)
        if ticker.status_code == 400:
                print("Invalid input")
                DataRecieve()                
                return
            
        tickerjson = ticker.text
        data = pd.read_json(tickerjson)
        print(data)
        print(len(data))
        print("###############################")
        return data , basechoice
# Recieve data out of function
data = DataRecieve()
print(data[0])

#### Currency Conversion ######
Chart()
convert_to = input("What currency do you wish to convert to? \n")
convert_to = convert_to.upper()
convert_c = data[0].loc[convert_to]
#print(convert_c)
rate = convert_c[0]
print("Rate is " + str(rate))
quantity = input("How much of " + data[1] + " do you wish to convert? \n")

ans = int(quantity) * rate
ans = float(ans)
ans = round(ans,2)
print("Principle amount: " + quantity + " " + data[1] )
print("Rate: " + str(rate))
print("Return: " + str(ans) + " " +convert_to)






    

    

