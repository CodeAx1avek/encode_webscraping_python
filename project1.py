#!/usr/bin/env python3
#-*- coding: utf-8 -*-
#github.com/CodeAx1avek
import requests
from bs4 import BeautifulSoup
import os  
try :
  import requests
except ImportError:
  os.system ("pip install requests")
try:
  import bs4
except:
  os.system('pip install beautifulsoup4')
try:
  import pyfiglet
except:
  os.system('pip install pyfiglet')
R = "\033[1;31m"
G = "\033[1;32m"
B = "\033[0;94m"
Y = "\033[1;33m"
br = pyfiglet.figlet_format("CodeAx1")
print(B+br)
print('''
[URL ENCODER]
Coded By : CodeAX1
________________________________________
''')

url = 'https://www.scopulus.co.uk/tools/hexconverter.htm'
req = requests.session()
count = 1
file = open('file.txt','r').readlines()
for count,i in enumerate(file):
  data = {
    'codetype':'base64', 
    'code':i,
    'decrypt':'Decode'
  }
  source = req.post(url,data=data)
  sourcetext = str(source.text)
  soup = BeautifulSoup(sourcetext, 'html.parser')
  # print(soup.title.string)
  stringencoded = soup.textarea.string
  bothstring = str(count)+"."+stringencoded+" :"+i
  with open('encoded.txt','a') as f:
    f.write(bothstring)
    f.write('\n')
    f.close()
    print(Y+"[Encoded of]",count,end='\r')
print(R"we have created encoded.txt file in this folder check:)")
print("Finally Encoded All the Text")