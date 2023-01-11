#set up nltk tools and examples to practice
import nltk
nltk.download('all')

# example books to use
from nltk.book import *
import matplotlib.pyplot as plt
import numpy as np
from __future__ import division

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

