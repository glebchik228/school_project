# -*- codecs: utf-8 -*-

import argparse
import codecs
import re

#args logic
parser = argparse.ArgumentParser(description='song writer')
parser.add_argument(
    'variation',
    type=str,
    default="1",
    help='type of the song'
)
parser.add_argument(
    'count',
    type=int,
    default=10,
    help='count of words'
)
args = parser.parse_args()

#reading data
text = codecs.open("data/"+str(args.variation)+".txt", 'r', 'utf-8').read()

#data processing
pattern = re.compile('[\W_]+')
clean_text = pattern.sub(' ', text)
clean_text = clean_text.lower()
words = clean_text.split()

#train model
dictionary = dict.fromkeys(words, [])
for i in range(0, len(words) - 1):
    dictionary[words[i]] = dictionary[words[i]] + words[i+1].split()

dictionary[words[len(words)-1]] = dictionary[words[len(words)-1]] + words[0].split()

#print(dictionary)