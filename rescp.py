#!/usr/bin/env python
# coding: utf-8

# In[14]:


import requests
from bs4 import BeautifulSoup

r = requests.get("http://www.pyclass.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/", headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
r1 = requests.get("http://www.pyclass.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/t=0&s=10.html", headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
r2 = requests.get("http://www.pyclass.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/t=0&s=20.html", headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})

soup=BeautifulSoup(r.text + r1.text + r2.text,"html.parser")
soup

fd=soup.select(".propertyRow")
x=[]

for item in fd:
    det={}
    det["Price"]=item.select(".propPrice")[0].getText().replace("\n","").replace(" ","")
    det["Address"]=item.select(".propAddressCollapse")[0].getText() + item.select(".propAddressCollapse")[1].getText()
    try:
        det["Beds"]=item.select(".infoBed")[0].b.text
    except:
        det["Beds"]="NA"
    try:
        det["Full Bath"]=item.select(".infoValueFullBath")[0].b.text
    except:
        det["Full Bath"]="NA"
    try:
        det["Size"]=item.select(".infoSqFt")[0].b.text
    except:
        det["Size"]="NA"
    try:
        det["Half Bath"]=item.select(".infoValueHalfBath")[0].b.text
    except:
        det["Half Bath"]="NA"
    
    
    #print(item.select(".columnGroup"))
    det["Age"]="NA"
    for grp,name in zip(item.select(".featureGroup"),item.select(".featureName")):
        if "Age" in grp.getText():
            det["Age"]=name.getText()
        
    x.append(det)

    
import pandas
df=pandas.DataFrame(x)

df.to_csv("details.csv")

