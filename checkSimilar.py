#!/usr/bin/python
# -*- coding: utf-8 -*-

from dependencies import nltk, wn, wt, lesk
from nltk.corpus import wordnet_ic
brown_ic = wordnet_ic.ic('ic-brown.dat')

# inputs: synset of target word, tree depth
# outputs: synsets of words related by depth nodes in hyper/hyponym tree
def getSimilarWords(synset, numMatches) :

	similars = [synset]
	stack = [synset]
	matches = 0
 
	# pop from traverse stack
	# traverse all items in stack
	while len(stack) > 0 and matches < numMatches :
		node = stack.pop()

		# add hypernyms and hyponyms to similars array if not already there
		hypernyms = node.hypernyms()
		hyponyms = node.hyponyms()
		for item in hypernyms :
			if item not in similars and matches < numMatches :
				similars.append(item)
				matches+=1
		for item in hyponyms :
			if item not in similars and matches < numMatches :
				similars.append(item)
				matches+=1

	return similars


# inputs: a word, its part of speech, and the phrase it occurred in
# outputs: list of similar synsets
def getDisambigSimilars(word, pos, phrase) :
	# get correct synset for word in phrase
	disambig = lesk(wt(phrase), word, pos)
	return getSimilars(disambig)


def getSimilarity(w1, w2) :
	# get Resnik Similarity based on brown
	return max(w1.res_similarity(w2, brown_ic), w2.res_similarity(w1, brown_ic))

# inputs: candidate sentence list of tokenized words and a keyword to check similarity against
# outputs: the candidate tokenized sentence with highest similarity value

def getSentenceSimilarity(candidates, keywords) :

	# vector of similarities ( candidates[sentence][similarity of word] )
	similarityVectors = []

	candidatesText = parser.tokenize(candidates)

	for sentence in candidatesText :
		simV = [] # temp array for entry into similarityVectors
		for word in sentence :
			simV2 = [] # temp array for sumation entry into simV
			for keyword in keywords :
				simV2.append( getSimilarity(keyword, word) ) # calculate similarity across all keywords
			simV.append(sum(simV2)) # append similarity value into temp array

		similarityVectors.append(simV) # append temp array into similarityVectors

	# separate array with the average similarity value of words in each candidate sentence
	sumVec = [ ( sum(vec) / len(vec) ) for vec in similarityVectors ]

	return sumVec


def getBest(candidates, keywords, sentiment) :
	return
