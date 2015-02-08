#!/usr/bin/env python
import random
import nltk
from pprint import pprint
from string import punctuation
from nltk.corpus import wordnet as wn
from nltk.wsd import lesk
from nltk.tokenize import RegexpTokenizer

WORD = "\w+[\'-]?\w*"
PRICE = "\$[\d.]+"
PUNCTUATION_EXCEPT_HYPHEN = '[' + punctuation.replace('-', '') + ']'
REGEX = "|".join([WORD, PRICE, PUNCTUATION_EXCEPT_HYPHEN])

dickens = 'data/dickens.txt'
hemingway = 'data/hemingway.txt'
shakespeare = 'data/shakespeare.txt'

dickens_out = 'data/dickens_corpus.txt'
hemingway_out = 'data/hemingway_corpus.txt'
shakespeare_out = 'data/shakespeare_corpus.txt'

corpus_in = [dickens, hemingway, shakespeare]
corpus_out = [dickens_out, hemingway_out, shakespeare_out]


def tokenize_string(line):
	tokenizer = RegexpTokenizer(REGEX)
	return tokenizer.tokenize(line)

def build_corpus():
	"""
	Tokenize an input file to use for a corpus
	Saves the output file to the data folder
	"""
	for i in range(len(corpus_in)) :
		inf = corpus_in[i]
		outf = corpus_out[i]
		with open(inf, 'r') as infile, open(outf, 'w') as outfile:
			for line in infile:
				line = line.replace("'", '')
				outfile.write(" ".join(tokenize_string(line)) + "\n")

build_corpus()
