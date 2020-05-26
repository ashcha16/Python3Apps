#This version considers proper nouns as well such as Delhi,Texas etc.
import json
from difflib import get_close_matches

data = json.load(open("App1_Dict/data_source/data.json"))

def translate(w):
    lw = w.lower()
    if lw in data.keys():
        return data[lw]
    elif lw.title() in data.keys(): #this will check for proper noun like texas or delhi
        return data[lw.title()]
    elif len(get_close_matches(lw,data.keys(),cutoff=0.8)) > 0:
        yn = input("Did you mean {} instead? Enter Y, if yes, or N, if no: ".format(get_close_matches(lw,data.keys(),cutoff=0.8)[0]))
        if (yn == "Y" or yn == "y"):
            return data[get_close_matches(lw,data.keys(),cutoff=0.8)[0]]
        elif yn == "N" or yn == "n":
            return "The word doesn't exist, please double check it"
        else:
            return "We didn't understand your response"
    else:
        return "The word doesn't exist, please double check it"


word = input("Enter Word: ")
    
output = translate(word)
if isinstance(output,str):
    print(output)
else:
    for i in output:
        print(i)
    
     




