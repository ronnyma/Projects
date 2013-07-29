#!/usr/bin/env python

"""
Count Words in a String - Counts the number of individual
words in a string and display the top 5/10 most used words.
"""

import re

class WordCount:
    def __init__(self, file):
        self.infile = file

    '''
       http://stackoverflow.com/questions/3496518/python-using-a-dictionary-to-count-the-items-in-a-list
    '''
    def count_words(self):
        tokenized = re.split(r'\W+', (open(self.infile).read()).strip())  #Split the text by non-words
        
        #result = dict([(i, tokenized.count(i)) for i in set(tokenized)])  #Put the tokes into a dict to count unique

        sresult = sorted((dict([(i, tokenized.count(i)) for i in set(tokenized)])).items(), key=lambda x: -x[1])  #Sort reverse

        print sresult


        print "The text contains %d words where %d are unique words" % (len(tokenized), len(sresult) )

    

if __name__ == '__main__':
    wc = WordCount('text')
    wc.count_words()

