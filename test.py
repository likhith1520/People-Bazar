# import re 
import pandas as pd
import requests as rs
from bs4 import BeautifulSoup
#flipkart site - details of products
pd.set_option("display.max_rows",6)
pd.set_option('max_colwidth',100)
cols=["Name","price"]
df=pd.DataFrame(columns=cols)
def other_products(key):
    try:
        url="https://www.flipkart.com/search?q="
        url2="&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
        final_url=url+key+url2
        data=rs.get(final_url)
        soup=BeautifulSoup(data.text,'html.parser')
        namesf=[]
        pricef=[]
        for a in soup.findAll('div',attrs={'class':['_3liAhj','_3O0U0u']}):
            price=a.find('div',attrs={'class':['_1vC4OE','_1vC4OE _2rQ-NK']})
            pricef.append(price)
            name=a.find('a',attrs={'class':['_2cLu-l','_3wU53n']})
            namesf.append(name)
        data1_table=pd.DataFrame(list(zip(namesf,pricef)),columns=["Name","Price"])
        print("Products in Flipkart Site ")
        print(data1_table.head(5))
    except:
        print("Product not found in flipkart")

    
    
def mobile_phones(key):
    try:
        url="https://www.flipkart.com/search?q="
        url2="&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
        final_url=url+key+url2
        data=rs.get(final_url)
        soup=BeautifulSoup(data.text,'html.parser')
        namesf=[]
        pricef=[]
        ram=[]
        rom=[]
        for line in soup.findAll('div',attrs={'class':'_3O0U0u'}):
            names=line.find('div',attrs={'class':'_3wU53n'})
            phone_name=names.string.split('(')[0];
            namesf.append(phone_name)
            names2=line.find('div',attrs={'class':'_1vC4OE _2rQ-NK'})
            pricef.append(names2.string)
            rams=line.find('li',attrs={'class':''})
            
        data_table=pd.DataFrame(list(zip(namesf,pricef)),columns=["Names","Price"])
        print("Products in Flipkart Site ")
        print(data_table.head(5))
    except:
        print("Product not found in flipkart ")

def paytm(key):
    try:
        url="https://paytmmall.com/shop/search?q="
        final=url+key
        data=rs.get(final)
        soup=BeautifulSoup(data.text,'html.parser')
        namess=[]
        prices=[]
        for line in soup.findAll('div',attrs={'class':'_1fje'}):
            names=line.find('div',attrs={'class':'UGUy'})
            namess.append(names)
            price=line.find('div',attrs={'class':['_1kMS','dQm2']})
            prices.append(price.span.text)
        print("Items in paytm mall : ")
        data1=pd.DataFrame(list(zip(namess,prices)),columns=["Names","Prices"])
        print(data1)
    except:
        print("product not found in paytm mall")

def snapdeal(key):
    try:
        url="https://www.shopclues.com/search?q="
        url2="&sc_z=2222&z=0&count=0"
        final=url+key+url2
        data=rs.get(final)
        prices=[]
        namess=[]
        soup=BeautifulSoup(data.text,'html.parser')
        for line in soup.findAll('div',attrs={'class':['column col3 search_blocks','column col3']}):
            price=line.find('span',attrs={'class':'p_price'})
            prices.append(price)
            name=line.find(['span','h2'],attrs={'class':['','prod_name']})
            namess.append(name)
        print('Items in Snapdeal site')
        datat=pd.DataFrame(list(zip(namess,prices)),columns=["names","Prices"])
        print(datat.head(5))
    except:
        print("Item unavailable")

        
#this we should get from the category field
x=int(input("Enter 1 for mobile details 2 for other products :"))
item=input("Enter the product name : ")
if x==1:
    mobile_phones(item)
    paytm(item)
    snapdeal(item)
else:
    other_products(item)
    paytm(item)
    snapdeal(item)