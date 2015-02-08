#!/usr/bin/python
# -*- coding: utf-8 -*-

from dependencies import nltk, wn, wt, lesk

# inputs: synset of target word, tree depth
# outputs: synsets of words related by depth nodes in hyper/hyponym tree
def getSimilarWords(synset, numMatches = 10) :

	similars = [synset]
	stack = [synset]
	matched = 0
 
	# pop from traverse stack
	# traverse all items in stack
	while len(stack) > 0 and matched < numMatches :
		node = stack.pop()

		# add hypernyms and hyponyms to similars array if not already there
		hypernyms = node.hypernyms()
		hyponyms = node.hyponyms()
		for item in hypernyms :
			if item not in similars :
				similars.append(item)
				matches ++
		for item in hyponyms :
			if item not in similars :
				similars.append(item)
				matches ++

	return similars


# inputs: a word, its speech, and the phrase it occurred in
# outputs: list of similar synsets
def getDisambigSimilars(word, pos, phrase) :

	#get correct synset for word in phrase
	disambig = lesk(wt(phrase), word, pos)
	return getSimilars(disambig)



# inputs: candidate sentence list of tokenized words and a keyword to check similarity against
# outputs: the candidate tokenized sentence with highest similarity value

def maxSentenceSimilarity(candidates, keyword) :

	# vector of similarities ( candidates[sentence][similarity of word] )
	similarityVectors = []

	for sentence in candidates :
		simV = [] # temp array for entry into similarityVectors
		for word in sentence :
			simV.append( bigramSim(keyword, word) ) # append similarity value into temp array

		similarityVectors.append(simV) # append temp array into similarityVectors

	# separate array with the average similarity value of words in each candidate sentence
	sumVec = [ ( sum(vec) / len(vec) ) for vec in similarityVectors]
	
	# find index of maximum
	max_index = 0
	max_val = 0
	for index in range( len(candidates) ) :
		val = sumVec[index]
		if val > max_val :
			max_val = val
			max_index = index

	# return candidate with max value
	return candidates[max_index]











