import nltk, re, pprint
from nltk import word_tokenize
from urllib import request
url = "http://www.gutenberg.org/files/2554/2554-0.txt"
response =request.urlopen(url)
raw = response.read().decode('utf-8-sig') #utf8 gives ufeff to the top of the string...
type(raw)
len(raw)
raw[:75]

#tokenization
tokens = word_tokenize(raw)
type(tokens)
len(tokens)
tokens[:10]

#regular operation with tokenization
text = nltk.Text(tokens)
text[1024:1062]
text.collocations()

#manual inspection
raw.find("PART I")
raw.rfind("End of Project Gutenberg's Crime")
raw = raw[5338:1157743]
raw.find("PART I")

#webpage html handling
url = "http://news.bbc.co.uk/2/hi/health/2284783.stm"
html = request.urlopen(url).read().decode('utf-8-sig')
html[:60]

#beautiful soup
from bs4 import BeautifulSoup
raw = BeautifulSoup(html,'html.parser').get_text()
tokens = word_tokenize(raw)
tokens

tokens = tokens[110:390]
text = nltk.Text(tokens)
text.concordance('gene')

