import os
os.chdir("C:\Users\User\Desktop\Web Data Analytics\Project\WorkDir")
import pandas as pd
import urllib2
import bs4 as bs
from bs4 import SoupStrainer
df = pd.read_csv('10Klinks_final.csv')
df['BigData1']=0
df['BigData2']=0
df['Cloud']=0
df['AI']=0
df['ML']=0
df['Analytics']=0

df['Autonomous vehicles']=0
df['Robotics']=0
df['Augmented Reality']=0
df['Virtual Reality']=0
df['D3_Printing']=0
df['Drones']=0
df['Internet of Things']=0
df['Blockchain']=0
df['Nanotechnology']=0
df['Nano technology']=0
df['Quantum_Computing']=0


bigdata_list1=[]
bigdata_list2=[]
cloud_list=[]
AI_list=[]
ML_list=[]
Analytics_list=[]

Autonomous_vehicles_list=[]
Robotics_list=[]
Augmented_Reality_list=[]
Virtual_Reality_list=[]
D3_Printing_list=[]
Drones_list=[]
Internet_of_Things_list=[]
Blockchain_list=[]
Nanotechnology_list=[]
Quantum_Computing_list=[]

for link in df['Link of Document']:
# link = 'https://www.sec.gov/Archives/edgar/data/353184/000035318414000011/airt10k_033114.htm'
    html = urllib2.urlopen(link).read()
    import re
    list1=[]
    wordlist=['big data','bigdata','cloud computing','artificial intelligence','machine learning','Analytics',
             'Autonomous_vehicles',
'Robotics',
'Augmented_Reality',
'Virtual_Reality',
'3D Printing',
'Drones',
'Internet_of_Things',
'Blockchain',
'Nanotechnology',
'Quantum_Computing'
]
#     wordlist=['data','computing','artificial intelligence','machine learning','kjkjh']
    for word in wordlist:
        keyword_count=len(re.findall(word,html,re.IGNORECASE))
        if keyword_count>0:
            list1.append(keyword_count)
        else:
            list1.append(0)
    if list1[0]>0:
        bigdata_list1.append(list1[0])
    if list1[0]==0:
        bigdata_list1.append(0)
        
    if list1[1]>0:
        bigdata_list2.append(list1[1])
    if list1[1]==0:
        bigdata_list2.append(0)
        
    if list1[2]>0:
        cloud_list.append(list1[2])
    if list1[2]==0:
        cloud_list.append(0)

    if list1[3]>0:
        AI_list.append(list1[3])
    if list1[3]==0:
        AI_list.append(0)

    if list1[4]>0:
        ML_list.append(list1[4])
    if list1[4]==0:
        ML_list.append(0)
        
    if list1[5]>0:
        Analytics_list.append(list1[5])
    if list1[5]==0:
        Analytics_list.append(0)
        
    if list1[6]>0:
        Autonomous_vehicles_list.append(list1[5])
    if list1[6]==0:
        Autonomous_vehicles_list.append(0)
    if list1[7]>0:
        Robotics_list.append(list1[1])
    if list1[7]==0:
        Robotics_list.append(0)
        
    if list1[8]>0:
        Augmented_Reality_list.append(list1[2])
    if list1[8]==0:
        Augmented_Reality_list.append(0)

    if list1[9]>0:
        Virtual_Reality_list.append(list1[3])
    if list1[9]==0:
        Virtual_Reality_list.append(0)

    if list1[10]>0:
        D3_Printing_list.append(list1[4])
    if list1[10]==0:
        D3_Printing_list.append(0)
        
    if list1[11]>0:
        Drones_list.append(list1[5])
    if list1[11]==0:
        Drones_list.append(0)
    if list1[12]>0:
        Internet_of_Things_list.append(list1[1])
    if list1[12]==0:
        Internet_of_Things_list.append(0)
        
    if list1[13]>0:
        Blockchain_list.append(list1[2])
    if list1[13]==0:
        Blockchain_list.append(0)

    if list1[14]>0:
        Nanotechnology_list.append(list1[3])
    if list1[14]==0:
        Nanotechnology_list.append(0)

    if list1[15]>0:
        Quantum_Computing_list.append(list1[4])
    if list1[15]==0:
        Quantum_Computing_list.append(0)

df['BigData1'] = pd.Series(bigdata_list1)
df['BigData2'] = pd.Series(bigdata_list2)
df['Cloud']=pd.Series(cloud_list)
df['AI']=pd.Series(AI_list)
df['ML']=pd.Series(ML_list)
df['Analytics']=pd.Series(Analytics_list)
df['Autonomous_vehicles'] = pd.Series(Autonomous_vehicles_list)
df['Robotics'] = pd.Series(Robotics_list)
df['Augmented_Reality']=pd.Series(Augmented_Reality_list)
df['Virtual_Reality']=pd.Series(Virtual_Reality_list)
df['D3_Printing']=pd.Series(D3_Printing_list)
df['Drones'] = pd.Series(Drones_list)
df['Internet_of_Things'] = pd.Series(Internet_of_Things_list)
df['Blockchain']=pd.Series(Blockchain_list)
df['Nanotechnology']=pd.Series(Nanotechnology_list)
df['Quantum_Computing']=pd.Series(Quantum_Computing_list)
df.to_csv("C:\Users\User\Desktop\Web Data Analytics\Project\WorkDir\Used_wordv2.csv")
df
