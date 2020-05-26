import requests
from bs4 import BeautifulSoup
import pandas

r = requests.get("http://www.pyclass.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/", 
headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})

c = r.content

soup=BeautifulSoup(c,"html.parser")

page_num=soup.find_all("a",{"class":"Page"})[-1].text #finding the number of pages from first page tag a and getting last value

#print(soup.prettify)
#Getting all the div tags with class name propertyrow
#all = soup.find_all("div",{"class":"propertyRow"})
#to get price of property from first value of all
#first_price=all[0].find("h4",{"class":"propPrice"}).text.replace("/n","").replace(" ","")
#print(first_price)
base_url="http://www.pyclass.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/#t=0&s="
infolist = []
for page in range(0,int(page_num*10),10):
    req=requests.get(base_url+str(page)+".html",
    headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
    con=req.content
    soup = BeautifulSoup(con,"html.parser")
    all=soup.find_all("div",{"class":"propertyRow"})
    for item in all:
        dict = {}
        dict["Property Price"] = item.find("h4",{"class":"propPrice"}).text.replace("\n","").replace(" ","")
        #for below logic you can use direct index value as address is of two line by using the index [0] and [1]
        counter = 0
        for i in item.find_all("span",{"class":"propAddressCollapse"}):
            if counter == 0:
                dict["Address"]=i.text #in first iteration it will store first line of address
                counter = counter+1
            else:
                dict["Locality"]=i.text # here it will store the second line

        #print(item.find_all("span",{"class":"propAddressCollapse"})[0].text)
        #print(item.find_all("span",{"class":"propAddressCollapse"})[1].text)
        try:
            dict["Beds"]=item.find("span",{"class":"infoBed"}).find("b").text
        except:
            dict["Beds"]=None
        try:
            dict["Sq ft"]=item.find("span",{"class":"infoSqFt"}).find("b").text
        except:
            dict["Sq ft"]=None
        try:
            dict["Full Baths"]=item.find("span",{"class":"infoValueFullBath"}).find("b").text
        except:
            dict["Full Baths"]=None
        try:
            dict["Half Baths"]=item.find("span",{"class":"infoValueHalfBath"}).find("b").text
        except:
            dict["Half Baths"]=None
        try:
            for col_grp in item.find_all("div",{"class":"columnGroup"}):        
                for ftr_grp,ftr_name in zip(col_grp.find_all("span",{"class":"featureGroup"}),
                col_grp.find_all("span",{"class":"featureName"})):  
                    if "Lot Size:" in ftr_grp.text:
                        dict["Lot Size"]=ftr_name.text                     
        except:
            dict["Lot Size"]=None
        infolist.append(dict)

df=pandas.DataFrame(infolist)

df.to_csv("Property Data.csv")