#!/usr/bin/env python
# -*- coding: utf-8 -*-
from nltk.tokenize import treebank
import tweepyFunctions
from nltk.tag import pos_tag  

from dependencies import *


#tokenize by spaces
def TokenMaker(tweets):
	tokens = []
	for tweet in tweets:
		x = tweet.split(" ")
		tokens.append(x)
	#part of speech analysis (for each token in sentence)
	##TAKES tokens (list(str))
	#RETURNS list(tuple(str, str)) tagged
	tagged = []
	for t in tokens:
		temp = pos_tag(t)
		tagged.append(temp)
	return tagged

first = tweepyFunctions.keywordSearch('dog', 1)[0].text
