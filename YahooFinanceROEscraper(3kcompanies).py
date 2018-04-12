import pandas as pd
import urllib2
df = pd.read_csv('all companies v5.csv')
urls = df["urls"].tolist()
html = urllib2.urlopen(urls[5]).read()
html = html[html.find("After Tax ROE"):]
temp = html
start = html.find("%</td>\r\n")
end = html.find("</td>\r\n                            </tr>\r\n")
html = html[start-3:end]
pf = html.split("</td>\r\n                                <td>")
if pf == ['']:
    pf = ['','','','']
elif pf[0][0] == "d":
    pf[0] = pf[0][2:]
elif pf[0][0] == ">":
    pf[0] = pf[0][1:]
else:
    pass
pf

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
    pf
    
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

roe = []
for link in urls:
    
    class MyOpener(FancyURLopener, object):
        version = choice(user_agents)
    
    myopener = MyOpener()
    page=myopener.open(link)
    
    html = page.read()
    
    html = html[html.find("After Tax ROE"):]
    temp = html
    start = html.find("%</td>\r\n")
    end = html.find("</td>\r\n                            </tr>\r\n")
    html = html[start-3:end]
    
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
    
    roe.append(pf)
    
labels = ["roe2016","roe2015","roe2014","roe2013"]
aftertaxroe = pd.DataFrame.from_records(roe, columns = labels)
df = df.join(aftertaxroe)
df.to_csv('all companies v6.csv',index=False)
