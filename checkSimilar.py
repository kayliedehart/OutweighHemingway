#!/usr/bin/python
# -*- coding: utf-8 -*-

from dependencies import nltk, wn, wt, lesk
from nltk.corpus import wordnet_ic
from wordParse import TokenMaker
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


def checkSingleSentence(tokenized_sentence) :
	periods = 0
	for token in tokenized_sentence :
		if token == "." :
			periods += 1
	return periods < 2

# inputs: a word, its part of speech, and the phrase it occurred in
# outputs: list of similar synsets
def getDisambigSimilars(word, pos, phrase) :
	# get correct synset for word in phrase
	disambig = lesk(wt(phrase), word, pos)
	return getSimilars(disambig)

def getWord(w) :
	if 'V' in w[1] :
		return str(w[0]+'.v.01')
	elif 'JJ' in w[1] :
		return str(w[0]+'.a.01')
	elif 'N' in w[1] :
		return str(w[0]+'.n.01')
	else :
		return 'none'


def getSimilarity(w1, w2) :
	# get Resnik Similarity based on brown
	return max(w1b.res_similarity(w2b, brown_ic), w2b.res_similarity(w1b, brown_ic))

# inputs: candidate sentence list of tokenized words and a keyword array to check similarity against
# outputs: the candidate tweet object with highest similarity value

def getSentenceSimilarity(candidates, keywords) :

	# vector of similarities ( candidates[sentence][similarity of word] )
	similarityVectors = []
	textCandidates = []
	for tweet in candidates :
		textCandidates.append(tweet.text)
	tokenizedCandidates = TokenMaker(textCandidates)

	for sentence in tokenizedCandidates :
		simV = [] # temp array for entry into similarityVectors
		for word in sentence :
			print word
			wordd = getWord(word)
			if wordd == 'none':
				continue

			simV2 = [] # temp array for sumation entry into simV

			for keyword in keywords :
				wordd = wn.synset(wordd)
				simV2.append( getSimilarity(wn.synset(keyword), wordd) ) # calculate similarity across all keywords
			simV.append(sum(simV2)) # append similarity value into temp array

		similarityVectors.append(simV) # append temp array into similarityVectors

	# separate array with the average similarity value of words in each candidate sentence
	sumVec = [ ( sum(vec) / len(vec) ) for vec in similarityVectors ]

	# get index of maximum
	max_index = 0
	max_val = 0
	for index in range(0, len(sumVec)) :
		val = sumVec[index]
		if val > max_val :
			max_val = val
			max_index = index

	# return tweet obj with max 
	return candidates[max_index]

# for now just use the most similar
# later add in sentiment and structure support
def getBest(candidates, keywords, sentiment) :
	return getSentenceSimilarity(candidates, keywords)
