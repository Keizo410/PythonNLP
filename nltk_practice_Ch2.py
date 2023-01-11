#set up nltk library and 25000 free electronic books
import nltk
from nltk.corpus import gutenberg
#set the book set as emma
emma = gutenberg.words('austen-emma.txt')
len(emma)

#since books from corpus is different from book, we need to preprocess
emma = nltk.Text(gutenberg.words('austen-emma.txt'))
emma.concordance("surprize")

#short example to display some info about the books
for fileid in gutenberg.fileids():
    num_charts = len(gutenberg.raw(fileid))
    num_words = len(gutenberg.words(fileid))
    num_sents = len(gutenberg.sents(fileid))
    num_vocab = len(set(w.lower() for w in gutenberg.words(fileid)))
    print(round(num_charts/num_words),round(num_words/num_sents),round(num_words/num_vocab),fileid)

#