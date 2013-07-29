#!/usr/bin/env python

"""
Count Words in a String - Counts the number of individual
words in a string and display the top n most used words.
"""

import re

class WordCount:
    def __init__(self, infile):
        self.infile = infile

    '''
       http://stackoverflow.com/questions/3496518/python-using-a-dictionary-to-count-the-items-in-a-list
    '''
    def count_words(self, most_used):
        tokenized = re.split(r'\W+', (open(self.infile).read()).strip())  #Split the text by non-words
        

        sresult = sorted((dict([(i, tokenized.count(i)) for i in set(tokenized)])).items(), key=lambda x: -x[1])  #Sort reverse



        print "The text contains %d words where %d are unique words" % (len(tokenized), len(sresult) )

        print "Top words by frequency:"
        print [el[0] for el in sresult][:most_used]


if __name__ == '__main__':
    wc = WordCount('text')
    wc.count_words(5)
