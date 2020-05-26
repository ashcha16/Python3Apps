
import time
from datetime import datetime as dt 

host_temp = r"C:\Users\Ashish\Desktop\Python_3\App3_Web_Block\hosts"
host_path = r"C:\Windows\System32\drivers\etc\hosts" # r will treat it as a row 
redirect = "127.0.0.1"
web_list = ["www.facebook.com","facebook.com"] 


while True:
    #converting tuple to datetime to compare with current time
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,17):
        print("Working Hours")
        with open(host_path,"r+") as fl:
            content = fl.read()#reads as string
            for website in web_list:
                if website in content:
                    pass
                else:
                  fl.write(redirect+" "+website+"\n")       

    else:
        print("Fun hours")
        with open(host_path,"r+") as fl:
            content = fl.readlines()#reads lines and creates a list
            fl.seek(0)
            for line in content:
                if not any(website in line for website in web_list):
                    fl.write(line)
            fl.truncate()        
    time.sleep(5)
    

