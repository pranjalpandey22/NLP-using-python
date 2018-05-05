# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 10:24:25 2018

@author: Pranjal
"""

from urllib.request import urlopen
import nltk
from bs4 import BeautifulSoup as bs

# Opening url and srcape data
url = 'http://www.gutenberg.org/files/2554/2554-0.txt'
raw = str(urlopen(url).read())

type(raw)
len(raw)
raw[:75]
raw[1258860:]

# Tokenize
tokens = nltk.word_tokenize(raw)

type(tokens)
len(tokens)
tokens[:10]

# tokens to text
text = nltk.Text(tokens)
text[1020:1060]

# find collocations
text.collocations()

# Re-setting raw text
raw.find('PART I')
raw.rfind("End of Project Gutenberg")
raw = raw[5866:1338288]


# BBC News sample

url = "http://news.bbc.co.uk/2/hi/health/2284783.stm"

# Open url
html = urlopen(url)
# Beautiful soup to read the page
raw = bs(html.read(), 'lxml')

# Get only text and convert the words to tokens
text1 = raw.get_text()
tokens = nltk.word_tokenize(text1)

# Reset the tokens to get only the article
tokens = tokens[111:402]

# convert back to text
text = nltk.Text(tokens)

text.concordance('gene')

# =============================================================================
# RSS FEEDS
# =============================================================================

import feedparser

url = "http://languagelog.ldc.upenn.edu/nll/?feed=atom"
llog = feedparser.parse(url)
llog

# Title of the feed
llog['feed']['title'] 

# To see the items/ entries in the feed
llog['items'] # or
llog['entries'] # Each entry is a dictionary

len(llog.entries) # Number of entries

# Third entry 
post = llog.entries[2] # or llog['entries'][2]

post.title # title of the third entry
content = post.content[0].value # value of the first post in the third entry 
content[:170]

# To get the text of any particular entry value (third here)
soup = bs(content, 'lxml')
# Print the html
print(soup.prettify())
# Print onnly the text value removing all the html tags
nltk.word_tokenize(soup.get_text())

# =============================================================================
# READ TEXT FORM DOCUMENT
# =============================================================================

import os

os.listdir('.')

f = open('document.txt')
raw = f.read()
raw
# But the newline characters still remain

f = open('document.txt', 'rU')
f.read()

# =============================================================================
# READ TEXT FROM PDF
# =============================================================================

import PyPDF2 as pypdf

pdf_file = open('sample.pdf', 'rb')
read_pdf = pypdf.PdfFileReader(pdf_file)

print(read_pdf.getNumPages())
read_pdf.getPage(0)


# content on the page
content = read_pdf.getPage(0).extractText()
print(content)

pdf2 = open('Natural language Processing using python.pdf', 'rb')
content2 = pypdf.PdfFileReader(pdf2).getPage(22).extractText()
print(content2)


# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# b = [' '  * 2 * (7 - i) + 'very' * i for i in a]
# for line in b:
#    print(b)

# =============================================================================
# UNICODE TRANSLATION
# =============================================================================

import codecs

path = nltk.data.find('corpora/unicode_samples/polish-lat2.txt')

f = codecs.open(path, encoding='latin2')

# decoding
for line in f:
    line = line.strip()
    print(line.encode('unicode_escape'))


# =============================================================================
# REGULAR EXPRESSIONS
    
# ^ - Start symbol
# $ - End symbol
# . - Wildcard symbol (Any symbol can be placed)
# ? - Previous character is optional
# + - One or more instances of the preceding item 
# * - Zero or more instances
    
# =============================================================================

import re

wordlist = [w for w in nltk.corpus.words.words('en') if w.islower()]

# look for words that end with 'ed'
[w for w in wordlist if re.search('ed$', w)]

# 8 letter words with p as third letter and y as sixth letter
[w for w in wordlist if re.search('^..p..y..$', w)]

chat_words = sorted(set(w for w in nltk.corpus.nps_chat.words()))

[w for w in chat_words if re.search('^m+i+n+e+$', w)]


# findall
word = 'supercalifragilisticexpialidocious'
re.findall(r'[aeiou]', word)










