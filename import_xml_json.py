import xml.etree.ElementTree as ET
parser = ET.XMLParser(encoding="utf-8")
tree = ET.parse("files/newsafr.xml", parser)
titles = []
root = tree.getroot()
xml_items = root.findall("channel/item/description")
#print(len(xml_items))
string_words_xml = "" 
for xmli in xml_items:
  string_words_xml =string_words_xml +xmli.text.upper()

def ByLength(inputStr):
   return len(inputStr)    

def MximumOutputFunction(string_words_new):
  list_data = string_words_new.strip().split()
  word_data = {}
  for i in range(len(list_data)):
    data_length = ByLength(list_data[i])
    if data_length > 6:
      words_lengt = word_data.get(list_data[i],0)
      word_data[list_data[i]] = words_lengt+1 
  list_data_new=list(word_data.items())
  list_data_new.sort(key=lambda i: i[1])
  words_length = int(len(list_data_new))
  print(list_data_new[words_length -10:words_length])

print("Вывод топ 10 самых часто встречающихся в новостях слов длиннее 6 символовв файле XML")
MximumOutputFunction(string_words_xml)

import json
from pprint import pprint
with open(r"files/newsafr.json") as datafile:
	json_data = json.load(datafile)
	list_data=[]
	json_data1 = json_data["rss"]["channel"]["items"] 
	string_words_json = "" 
	for descriptions in json_data1:
	    string_words_json = string_words_json+ descriptions['description'].upper()

print("")
print("Вывод топ 10 самых часто встречающихся в новостях слов длиннее 6 символовв файле JSON")
MximumOutputFunction(string_words_json)
