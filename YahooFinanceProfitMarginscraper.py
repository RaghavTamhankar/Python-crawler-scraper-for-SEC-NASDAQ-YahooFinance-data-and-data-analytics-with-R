import pandas as pd
import urllib2
df = pd.read_csv('all companies v4.csv')
del df["pm2016"],df["pm2015"],df["pm2014"],df["pm2013"],df["roe2015"],df["roe2014"],df["roe2013"],df["roe2016"]
urls = df["urls"].tolist()
temp = temp[:start]
templist = []
if temp.find("EE3524") != -1 and temp.find("47C3D3") != -1:
    while temp.find("EE3524") != -1 and temp.find("47C3D3") != -1:
        if temp.find("EE3524") < temp.find("47C3D3"):
            templist.append(-1)
            temp = temp[temp.find("EE3524")+1:]
        else:
            templist.append(1)
            temp = temp[temp.find("47C3D3")+1:]
    if temp.find("47C3D3") == -1:
        templist = templist + [-1]*(4-len(templist))
    else:
        templist = templist + [1]*(4-len(templist))
elif temp.find("EE3524") == -1:
    templist = [1,1,1,1]
else:
    templist = [-1,-1,-1,-1]

for i in range(0,len(pf)):
    if templist[i] == -1:
        pf[i] = '-' + pf[i]

import time
from urllib import FancyURLopener  # This is library that helps us create the headless browser
from random import choice #This library helps pick a random item from a list

user_agents = [
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
    'Opera/9.80 (X11; Linux i686; Ubuntu/14.10) Presto/2.12.388 Version/12.16',
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; rv:2.2) Gecko/20110201',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246'
]


pmargin = []
for link in urls:
    
    class MyOpener(FancyURLopener, object):
        version = choice(user_agents)
    
    myopener = MyOpener()
    page=myopener.open(link)
    
    html = page.read()
    
    html = html[html.find("Profit Margin"):]
    temp = html
    start = html.find("%</td>\r\n")
    end = html.find("</tr>\r\n\r\n")
    html = html[start-3:end-35]
    
    pf = html.split("</td>\r\n                                <td>")
    
    if pf == ['']:
        pf = ['','','','']
    elif pf[0][0] == "d":
        pf[0] = pf[0][2:]
    elif pf[0][0] == ">":
        pf[0] = pf[0][1:]
    else:
        pass
    
    temp = temp[:start]
    templist = []
    if temp.find("EE3524") != -1 and temp.find("47C3D3") != -1:
        while temp.find("EE3524") != -1 and temp.find("47C3D3") != -1:
            if temp.find("EE3524") < temp.find("47C3D3"):
                templist.append(-1)
                temp = temp[temp.find("EE3524")+1:]
            else:
                templist.append(1)
                temp = temp[temp.find("47C3D3")+1:]
        if temp.find("47C3D3") == -1:
            templist = templist + [-1]*(4-len(templist))
        else:
            templist = templist + [1]*(4-len(templist))
    elif temp.find("EE3524") == -1:
        templist = [1,1,1,1]
    else:
        templist = [-1,-1,-1,-1]    
    
    for i in range(0,len(pf)):
        if templist[i] == -1:
            pf[i] = '-' + pf[i] 
    
    pmargin.append(pf)
    
labels = ["pm2016","pm2015","pm2014","pm2013"]
profitMargin = pd.DataFrame.from_records(pmargin, columns = labels)
df = df.join(profitMargin)
df.to_csv('all companies v5.csv',index=False)
