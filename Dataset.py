import string
import csv
import pandas as pd
import sys
import re
import os
print(os.getcwd())
URL=input("Enter the URL\n")
csv_path = os.getcwd() + '/project/Phishing_dataset.csv'

def serchbyURL():
    csv_file=csv.reader(open(csv_path,'r'))
    
    for row in csv_file:
        if URL ==row[0]:
            print(row)
            return 1

if serchbyURL()==1:
    sys.exit("the row already exist")
    

#Present of IP address in URL
s3=re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', URL)
if(s3):
    print("phishing = 1" )
    IP=1
else:
    print("Phishing = 0 ")
    IP=0

#Present of @ in Sysmbol
s2=URL.find("@")
print("@ prestnt in URL")
if s2==-1:
    print("phishing = 0")
    at_the_rate=0
else:
    print("Phishing = 1")
    at_the_rate=1

#Number of dotes in hostname
dots=URL.count(".")
print("Number of dotes in the URL",dots)
if dots>3:
    print("phishing = 1")
    dot=1
else:
    print("Phishing = 0")
    dot=0

#prefix and sufix seprated by - to domain
desh=URL.count("-")
print("NUmber of desh present in URl ",desh)
if desh>3:
    print("Phishing = 1")
    ps=1
else:
     print("phishing = 0")
     ps=0

#HTTPS token
print("searching for HTTPS..")
if(URL.find("https")!=-1):
    print("Phishing = 1")
    https=1
else:
    print("phishing = 0")
    at_the_rate=0
    https=0

#Information submission to Email
print("Searching of the mail() and mailto function in URL")
if((URL.find("mail()") or URL.find("mailto"))!=-1):
    print("Phishing = 1")
    mail=1
else:
    print("phishing = 0 ")
    mail=0
#Length of the HOSt name

length=len(URL)
print("Length of the URL",length)
if length>70:
    print("Phishng = 1 ")
    len=1
else:
    print("phishing = 0")
    len=0

#No of slash in URL 

slash=URL.count("/")
print("No of slash present in the url is ",slash)
if(slash>5):
    print("phishing = 1")
    sl=1
else:
    print("phishing = 0")
    sl=0

#creation of the Dataset
'''datset=[
    (URL,IP,at_the_rate,dot,ps,https,mail,len,sl)
]
df=pd.DataFrame(datset,columns=['URL','Presenc of IP ','presence of @','presence of Dot','Seprated by "-"','HTTPS present or no ','mail','length','presenc of slash'])
df.to_csv('Phishing_dataset.csv',index=False)'''

fields=[URL,IP,at_the_rate,dot,ps,https,mail,len,sl]
with open(csv_path, 'a') as f:
    writer = csv.writer(f)
    writer.writerow(fields)