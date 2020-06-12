from flask import Flask,render_template,request
import pandas as pd
import requests as rs
from bs4 import BeautifulSoup

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/',methods=['POST'])
def my_form_post():
    x=request.form['number']
    item=request.form['name']

    cols=["Name","price"]
    df=pd.DataFrame(columns=cols)
    print(item)
    if x=='1':
        df= mobile_phones(item)
    else:
        df=other_products(item)
    print(df)
    return render_template("index.html", column_names=df.columns.values, row_data=list(df.values.tolist()),zip=zip)

def other_products(key):
    url="https://www.flipkart.com/search?q="
    url2="&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
    final_url=url+key+url2
    data=rs.get(final_url)
    soup=BeautifulSoup(data.text,'html.parser')
    namesf=[]
    pricef=[]
    for a in soup.findAll('div',attrs={'class':'_3liAhj'}):
        price=a.find('div',attrs={'class':'_1vC4OE'})
        pricef.append(price.string)
        name=a.find('a',attrs={'class':'_2cLu-l'})
        namesf.append(name.string)
    data1_table=pd.DataFrame(list(zip(namesf,pricef)),columns=["Name","Price"])
    return (data1_table.head(5))

def mobile_phones(key):
    url="https://www.flipkart.com/search?q="
    url2="&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
    final_url=url+key+url2
    data=rs.get(final_url)
    soup=BeautifulSoup(data.text,'html.parser')
    namesf=[]
    pricef=[]
    for line in soup.findAll('div',attrs={'class':'_3O0U0u'}):
        names=line.find('div',attrs={'class':'_3wU53n'})
        phone_name=names.string.split('(')[0]
        namesf.append(phone_name)
        names2=line.find('div',attrs={'class':'_1vC4OE _2rQ-NK'})
        pricef.append(names2.string)
    data_table=pd.DataFrame(list(zip(namesf,pricef)),columns=["Names","Price"])
    return (data_table.head(5))

def paytm(key):
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
        return data1.head(5)
    


if __name__=='main_':
    app.run(debug=True)