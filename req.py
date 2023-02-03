import requests
from html.parser import HTMLParser
from bs4 import BeautifulSoup
import time

r = requests.get("https://t.me/rustili_tilini_ruscha/21195")
txt = r.content
sup = BeautifulSoup(txt,'lxml')
# soup = sup.prettify()
fn = sup.find("meta", {"name": "twitter:description"} )


# textlar = str(fn)[16:]
# cheklov = textlar.find("@")
# cheklov2 = textlar.find("Aloqa")
# cheklov3 = textlar.find("http")
# cheklov4 = textlar.find("property")
# if textlar.find("https" or "@" or "t.me") :
#   pass
# if textlar.find(sub)
# print(textlar.find("https"))
# context = str(fn["content"])
# kuchukcha = context.find("@")
# mazl = context.find("http")
# panjara = context.find("#")


staa = "saslom == sadsa ="
  

print(staa.replace("=",""))