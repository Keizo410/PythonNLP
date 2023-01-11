#set up nltk tools and examples to practice
from __future__ import division
import nltk
nltk.download('all')

# example books to use
from nltk.book import *
import matplotlib.pyplot as plt
import numpy as np

# Search key words
text1.concordance("monstrous")

# find words used in the similar context
text1.similar("monstrous")
#OUTPUT:
#mean part maddens doleful gamesome subtly uncommon careful untoward
#exasperate loving passing mouldy christian few true mystifying
#imperial modifies contemptible

# find common contexts using the specified words
text1.common_contexts(["monstrous","mystifying"])

# display dispersion plot of the keyword
text1.dispersion_plot("monstrous") #this gives dispersion of m o n s t . ...

text1.dispersion_plot(["monstrous"])  #this gives dispersion of monstrous as a token

#counting vocab
len(text1)

#counting distinct vocab
sorted(set(text1))
len(set(text1)) #number of distinct keywords

#lexical richness --- number of distinct vocab / number of entire text vocab

len(set(text1))/len(text1)

#count a specific keyword appearance
text1.count("wise")

#percentage of the keyword taking up the text
100 * text1.count("wise")/len(text1)

#create function for this process
def lexical_diversity(text):
    return len(set(text)) / len(text)

def percentage(count, total):
    return 100 * count / total

#Frequency distribution
fdist1 = FreqDist(text1)
print(fdist1)
fdist1.most_common(50)

fdist1['whale']

#Selection of words with properties
V = set(text1)
long_words = [w for w in V if len(w) > 15]
sorted(long_words)
print(long_words) # this list includes unique words in the text, which occurs only once

sorted(w for w in V if len(w) > 7 and fdist1[w] >7) #gives more strict property

#Collocation and Bigrams
text1.collocations()