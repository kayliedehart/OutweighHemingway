#!/usr/bin/python
# -*- coding: utf-8 -*-

from TwitterSetup import api

# Takes a keyword and a number of results and returns an array of resultant tweet objects
def keywordSearch(keyword, numResults = 1) :
	return api.search(q=keyword, count=numResults)

# pulls text from tweet object
def getTextFromTweet(tweet) :
	return tweet.text

# transforms an array of tweet objects into an array of strings
def tweetsToStrings(tweets) :
	strings = []
	while tweets :
		strings.append(tweets.pop().text)
	return strings

# pulls Author from tweet object
def getAuthorFromTweet(tweet) :
	return tweet.user.screen_name