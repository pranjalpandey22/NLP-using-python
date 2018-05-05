# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 02:26:53 2018

@author: Pranjal
"""

import nltk
from nltk.corpus import gutenberg

# =============================================================================
# Gutenberg Corpus
# =============================================================================

nltk.corpus.gutenberg.fileids()
nltk.corpus.gutenberg.words('austen-emma.txt')

### NUmber of words in emma
emma = gutenberg.words('austen-emma.txt')
len(emma)
emma = nltk.Text(emma)
emma.concordance('surprize')

for fileid in gutenberg.fileids():
    num_chars = len(gutenberg.raw(fileid))
    num_words = len(gutenberg.words(fileid))
    num_sents = len(gutenberg.sents(fileid))
    num_vocab = len(set([w.lower() for w in gutenberg.words(fileid)]))
    print(fileid, ":", "\nAverage word length: ", int(num_chars/num_words), 
          "\nAverage sentence length: ", int(num_words/num_sents), 
          "\nNumber of times each word appears in text: ", int(num_words/num_vocab))


### Complete text of Shakepeare's Macbeth
print(gutenberg.raw('shakespeare-macbeth.txt'))


# =============================================================================

# Brown Corpus
# Resource for studying systematic differences between genres, a kind of linguistic 
# inquiry known as stylistics.

# =============================================================================

from nltk.corpus import brown

brown.categories()
news_text = brown.words(categories='news')

# Comparison of modals in news

fdist = nltk.FreqDist([w.lower() for w in news_text])
modals = ['can', 'could', 'may', 'might', 'shall', 'should', 'will', 'would', 'must']

for m in modals:
    print(m, ":", fdist[m])

wh_words = ['what', 'when', 'where', 'who', 'why']

for w in wh_words:
    print(w, ":", fdist[w])


for genre in brown.categories():
    for word in brown.words(categories=genre):
        print(genre, word)


# CONDITIONAL FREQUENCY DISTRIBUTION
# nltk.ConditionalFreqDist()

cfdist = nltk.ConditionalFreqDist((genre, word)
                                  for genre in brown.categories()
                                  for word in brown.words(categories=genre))

genres = ['news', 'religion', 'hobbies', 'science_fiction', 'romance', 'humor']
cfdist.tabulate(conditions=genres, samples=modals)

# =============================================================================
 
# REUTERS CORPUS

# =============================================================================

from nltk.corpus import reuters

reuters.fileids()
reuters.categories()

# To know the categories of a single file or multiple files
reuters.categories('training/9865')
reuters.categories(['training/9865', 'training/9880'])


# =============================================================================

# INAUGURAL ADDRESS CORPUS

# =============================================================================

from nltk.corpus import inaugural

inaugural.fileids()

# Years
[fileid[:4] for fileid in inaugural.fileids()]

# Usage of words 'America' and 'citizen'

cfd = nltk.ConditionalFreqDist(
           (target, fileid[:4])
           for fileid in inaugural.fileids()
           for w in inaugural.words(fileid)
           for target in ['america', 'citizen']
           if w.lower().startswith(target))
cfd
cfd.plot()

# =============================================================================

# CONDITIONAL FREQUENCY DISTRIBUTION
# When the texts of a corpus are divided into several categories (by genre, topic, author,
# etc.), we can maintain separate frequency distributions for each category. This will
# allow us to study systematic differences between the categories. In the previous section,
# we achieved this using NLTK’s ConditionalFreqDist data type. A conditional frequency
# distribution is a collection of frequency distributions, each one for a different
# “condition.” The condition will often be the category of the text.

# =============================================================================


# =============================================================================
# Check for unusual words
# =============================================================================

def unusual_words(text):
    text_vocab = set(w.lower() for w in text if w.isalpha())
    english_vocab = set(w.lower() for w in nltk.corpus.words.words())
    unusual = text_vocab.difference(english_vocab)
    return sorted(unusual)

dondu = "haraka baraka gaya tel lene dondu just chill"
dondu = dondu.split(' ')
unusual_words(dondu)

# =============================================================================
# STOPWORDS
# =============================================================================

from nltk.corpus import stopwords

stopwords = nltk.corpus.stopwords.words('english')

# check for stopwords
sample_text = 'cross my heart and hope to die to my lover i never lie. i got the good side.'

def content_fraction(text):
    content = [w for w in text if w.lower() not in stopwords]
    return len(content)/len(text)

content_fraction(sample_text.split(' '))


# =============================================================================
# TARGET GAME - "egivrvonl"
# =============================================================================

game_letters = nltk.FreqDist('egivrvonl')

sample = nltk.FreqDist('abcdefghijklmnop')
sample2 = nltk.FreqDist('qrstuvwxyz')
sample > sample2

obligatory = 'r' # 'r' should be present in every word
wordlist = nltk.corpus.words.words()

# Given the operator <=, it is looking for words that have a frequency 
# less than/equal to those in the sample, letters.
[w for w in wordlist if len(w)>=4 and obligatory in w and nltk.FreqDist(w) <= game_letters]


fdist = nltk.FreqDist('abcdefg')

[w for w in wordlist if nltk.FreqDist(w) <= fdist]

# =============================================================================
# PRONOUNCING DICTIONARY BY CMU
# =============================================================================

from nltk.corpus import cmudict

entries = cmudict.entries()
entries[:20]

### Stress
# The phones contain digits to represent primary stress (1), secondary stress (2), and no
# stress (0)

def stress(pron):
    return [char for phone in pron for char in phone if char.isdigit()]

[w for w, pron in entries if stress(pron) == ['0', '1', '0', '2', '0']]

# Minimally contrasting sets of words

p3 = [(pron[0]+'-'+pron[2], word) for (word, pron) in entries if pron[0]=='P' and len(pron)==3]
p3

cfd = nltk.ConditionalFreqDist(p3)

cfd.conditions()
# cfd.plot()

for template in cfd.conditions():
    if (len(cfd[template]) > 10):
        wordslist = ' '.join(cfd[template].keys())
        print(template, wordslist)
        
# To know the pronunciation of a particular word

prondict = nltk.corpus.cmudict.dict()
prondict['fall']

# To get the pronunciation of a sample text
text = ['natural', 'language', 'processing']
[ph for w in text for ph in prondict[w]] 
# this will give all the available pronunciations for a words
# To get only one per word: [ph for w in text for ph in prondict[w][0]]

# =============================================================================
#  WORDNET
# =============================================================================


from nltk.corpus import wordnet as wn

# Set of synonyms for motorcar
wn.synsets('motorcar')

# Individual set car.n.01
wn.synset('car.n.01')
wn.synset('car.n.01').definition()
wn.synset('car.n.01').examples()
# Lemmas in the set
wn.synset('car.n.01').lemmas()
wn.synset('car.n.01').lemma_names()
wn.lemma('car.n.01.automobile')

# For football
wn.synsets('football')
wn.synsets('football')[0]
wn.synsets('football')[0].lemmas()
wn.synsets('football')[1]
wn.synsets('football')[1].lemmas()
wn.synset('football.n.01').definition()
wn.synset('football.n.02').definition()

# For Artefacts
wn.synsets('artefact')
wn.synset('artefact.n.01').lemmas()

# To know the hierarchy - Hyponyms(immediately below) and hypernyms(immediately above)
motorcar = wn.synset('car.n.01')
types_of_motocars = motorcar.hyponyms()
types_of_motocars
types_of_motocars[0].lemmas()
sorted(lemma.name() for synset in types_of_motocars for lemma in synset.lemmas())

motorcar.hypernyms()

# path for car - there are 2 paths from car back to root
# wheeled_container can have 2 different parents
[synset.name() for synset in motorcar.hypernym_paths()[0]] # path 1
[synset.name() for synset in motorcar.hypernym_paths()[1]] # path 2

# =============================================================================
# More lexical relations
# =============================================================================

# Meronyms - network from items to components
# Holonyms - things they are contained in

# tree
wn.synsets('tree')
# Parts of a tree:
wn.synset('tree.n.01').part_meronyms()
# Tree made of substances:
wn.synset('tree.n.01').substance_meronyms()
# Forest - collection of trees : 'tree.n.01' member of 'forest.n.01'
wn.synset('tree.n.01').member_holonyms() 

# =============================================================================

# SEMANTIC SIMILARITY
# Knowing which words are semantically related is useful for indexing a collection
# of texts, so that a search for a general term such as vehicle will match documents
# containing specific terms such as limousine.

# =============================================================================

# Two synsets linked to the same root may have several hypernyms in common. 
# If two synsets share a very specific hypernym—one that is low down in the
# hypernym hierarchy—they must be closely related.

wn.synsets('plane')
wn.synsets('ship')

plane = wn.synset('airplane.n.01')
ship = wn.synset('ship.n.01')

# Looking up the hierarchy
plane.hypernym_paths()

# Output
# 
# [[Synset('entity.n.01'),
#   Synset('physical_entity.n.01'),
#   Synset('object.n.01'),
#   Synset('whole.n.02'),
#   Synset('artifact.n.01'),
#   Synset('instrumentality.n.03'),
#   Synset('conveyance.n.03'),
#   Synset('vehicle.n.01'),
#   Synset('craft.n.02'),
#   Synset('aircraft.n.01'),
#   Synset('heavier-than-air_craft.n.01'),
#   Synset('airplane.n.01')]]

# Looking up the path
ship.hypernym_paths()

# Output
# [[Synset('entity.n.01'),
#   Synset('physical_entity.n.01'),
#   Synset('object.n.01'),
#   Synset('whole.n.02'),
#   Synset('artifact.n.01'),
#   Synset('instrumentality.n.03'),
#   Synset('conveyance.n.03'),
#   Synset('vehicle.n.01'),
#   Synset('craft.n.02'),
#   Synset('vessel.n.02'),
#   Synset('ship.n.01')]]

# to calculate the path depth
plane.min_depth()
ship.min_depth()

# Looking down the hierarchy
plane.lowest_common_hypernyms(ship) 
# Output : 'craft.n.02'

# =============================================================================

# PATH SIMILARITY
# path_similarity assigns a score in the range 0–1 based on the shortest 
# path that connects the concepts in the hypernym hierarchy
# (-1 is returned in those cases where a path cannot be found).

# =============================================================================

plane.path_similarity(ship)

# Output : 0.1666666666





