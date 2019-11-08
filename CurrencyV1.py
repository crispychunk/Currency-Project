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

######################################



### Choose Base currency ###
basechoice= input("What Base currency? -->")
basechoice =  basechoice.upper()



def DataRecieve(basechoice):
        ticker = r.get("https://api.exchangeratesapi.io/latest?base=" + basechoice)
        print(ticker)
        if ticker.status_code == 400:
                print("Invalid input")
                basechoice= input("What Base currency?")
                basechoice =  basechoice.upper()
                DataRecieve(basechoice)                
                return
            
        tickerjson = ticker.text
        data = pd.read_json(tickerjson)
        print(data)
        print("###############################")
        return data
# Recieve data out of function
data = DataRecieve(basechoice)




    

    

