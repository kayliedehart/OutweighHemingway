#!/usr/bin/python
# -*- coding: utf-8 -*-

from dependencies import nltk, wn, wt, lesk

SIMILARITY_DEPTH = 1

# inputs: synset of target word, tree depth
# outputs: synsets of words related by depth nodes in hyper/hyponym tree
def getSimilars(synset, numMatches) :

	similars = [synset]
	stack = [synset
	]

	# pop from traverse stack
	# traverse all items in stack
	while len(stack) > 0 :
		node = stack.pop()

		# add hypernyms and hyponyms to similars array if not already there
		if node not in similars :
			hypernyms = node.hypernyms()
			hyponyms = node.hyponyms()//////////////////////////////////////
			for item in hypernyms :
				if item not in similars :
					similars.append(item)
			for item in hyponyms :
				if item not in similars :
					similars.append(item)

	return similars


# inputs: a word, its speech, and the phrase it occurred in
# outputs: list of similar synsets
def getDisambigSimilars(word, pos, phrase) :

	#get correct synset for word in phrase
	disambig = lesk(wt(phrase), word, pos)
	return getSimilars(disambig)

print getSimilars(wn.synset('dog.n.01'))
