# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 03:50:13 2018

@author: Pranjal
"""

import nltk

### corpus

from nltk.book import *

# =============================================================================
# *** Introductory Examples for the NLTK Book ***
# Loading text1, ..., text9 and sent1, ..., sent9
# Type the name of the text or sentence to view it.
# Type: 'texts()' or 'sents()' to list the materials.
# text1: Moby Dick by Herman Melville 1851
# text2: Sense and Sensibility by Jane Austen 1811
# text3: The Book of Genesis
# text4: Inaugural Address Corpus
# text5: Chat Corpus
# text6: Monty Python and the Holy Grail
# text7: Wall Street Journal
# text8: Personals Corpus
# text9: The Man Who Was Thursday by G . K . Chesterton 1908
# 
# =============================================================================

# =============================================================================
# 
# CONTEXT
# 
# =============================================================================

text5.concordance("hell")

# =============================================================================
# 
# SIMILAR WORDS
# 
# =============================================================================

text2.similar("monstrous")

# =============================================================================
# 
# COMMON CONTEXT
# 
# =============================================================================

text2.common_contexts(["monstrous", "very"])

# =============================================================================
#
### Location of each word: Number of words from the beginning
# DISPERSION PLOT
# Stripe represents an instance of a word, Row represents the entire text 
#
# =============================================================================

text4.dispersion_plot(["hello", "liberty", "freedom", "poverty", "tyranny", "poor"])


# =============================================================================
# 
# Generate random text
#
# =============================================================================

text3.generate(text3) # METHOD REMOVED


# =============================================================================

### TOKEN
# A technical name for a sequence of characters that we want to treat as a group
# When we count the number of tokens in a text, say, the phrase to
# be or not to be, we are counting occurrences of these sequences. Thus, in our example
# phrase there are two occurrences of to, two of be, and one each of or and not.

### VOCABULARY
# Vocabuary of a text is just the set of tokens that it uses, since in a set, 
# all duplicates are collappsed together.  

# =============================================================================

### Vocabulary
set(text3)

### Number of words
len(set(text3))

# =============================================================================
# 
# WORD TYPE
# A word type is the form or
# spelling of the word independently of its specific occurrences in a text—that is, the
# word considered as a unique item of vocabulary. Our count of 2,789 items will include
# punctuation symbols, so we will generally call these unique items types instead of word
# types.
#
# =============================================================================


# =============================================================================
# 
# LEXICAL RICHNESS
# AVERAGE TIMES A WORD IS USED
# 
# =============================================================================

### Every word appears an average 16 times
int(len(text3)/len(set(text3)))

# =============================================================================
# 
### COUNT
# Count of any word 
# 
# =============================================================================

text5.count("lol")
percentage_of_lol_in_total = 100 * (text5.count("lol")/len(text5))
print(percentage_of_lol_in_total)

# =============================================================================
# 
# ### 50 Most Frequent Words
# # FreqDist
# 
# =============================================================================

fdist1 = FreqDist(text2)
print(fdist1)

vocab1 = fdist1.keys()
print(vocab1)
fdist1.plot(70, cumulative=True)

# =============================================================================
# 
# ### HAPAXES
# # Words which appear only once
#  
# =============================================================================

fdist1.hapaxes()

# =============================================================================
# 
# Words that more than 15 characters long
# Often Hapaxes
#
# =============================================================================

V = set(text4)
long_words = [w for w in V if len(w) > 15]
print(sorted(long_words))

# =============================================================================
# 
# Relatively long words occuring frequently (>7)
# 
# =============================================================================

fdist2 = FreqDist(text5)
sorted([w for w in fdist2.keys() if len(w) > 7 and fdist2[w]>7])

# =============================================================================
# 
# COLLOCATION
# A sequence of words that occur together unusually often. Eg: Red Wine 
# They are resistant to substitution with words that have similar senses; 
# Eg: maroon wine sounds very odd. 
#
# BIGRAMS: List of word pairs
#
# Collocations are essentially just frequent bigrams, except that we want to pay more
# attention to the rare words
#
# =============================================================================

from nltk import bigrams
bigram_obj = bigrams(['more', 'is', 'said', 'than', 'done'])
list(bigram_obj)

text4.collocations()

# =============================================================================
#
# Example Description
# fdist = FreqDist(samples)- Create a frequency distribution containing the given samples
# fdist.inc(sample)- Increment the count for this sample
# fdist['monstrous']- Count of the number of times a given sample occurred
# fdist.freq('monstrous')- Frequency of a given sample
# fdist.N()- Total number of samples
# fdist.keys()- The samples sorted in order of decreasing frequency
# for sample in fdist:- Iterate over the samples, in order of decreasing frequency
# fdist.max()- Sample with the greatest count
# fdist.tabulate()- Tabulate the frequency distribution
# fdist.plot()- Graphical plot of the frequency distribution
# fdist.plot(cumulative=True)- Cumulative plot of the frequency distribution
# fdist1 < fdist2- Test if samples in fdist1 occur less frequently than in fdist2
#
# =============================================================================

# =============================================================================
# 
# WORD SENSE DISAMBIGUATION
# Working out which sense of a word was intended in a given context
# we automatically disambiguate words using context, exploiting the simple fact 
# that nearby words have closely related meanings.
# =============================================================================

# =============================================================================
# 
# PRONOUN RESOLUTION
# To work out “who did what to whom,”: to detect the subjects and objects of verbs.
# Consider three possible following sentences and try to determine what was 
# sold, caught, and found (one case is ambiguous).
#
# a. The thieves stole the paintings. They were subsequently sold.
# b. The thieves stole the paintings. They were subsequently caught.
# c. The thieves stole the paintings. They were subsequently found.
#
# Answering this question involves finding the antecedent of the pronoun they,
# either thieves or paintings. Computational techniques for tackling this problem 
# include anaphora resolution—identifying what a pronoun or noun phrase refers 
# to—and semantic role labeling—identifying how a noun phrase relates to the verb 
# (as agent, patient, instrument, and so on).
#
# =============================================================================
