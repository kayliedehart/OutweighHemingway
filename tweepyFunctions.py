#!/usr/bin/python
# -*- coding: utf-8 -*-

from TwitterSetup import api

# Takes a keyword and a number of results and returns an array of resultant tweet objects
def keywordSearch(keyword, numResults) :
	return api.search(q=keyword, count=numResults)

# pulls text from tweet object
def getTextFromTweet(tweet) :
	return tweet.text

# pulls id number from tweet object
def getIdFromTweet(tweet) :
	return tweet.id

# pulls Author from tweet object
def getAuthorFromTweet(tweet) :
	return tweet.user.screen_name

# pull replied from username
def repliedFrom(tweet) :
	return tweet.in_reply_to_screen_name

# is retweet?
def isRetweet(tweet) :
	return tweet.retweeted

# is truncated? (we probs don't want truncated twee...)
def isTruncated(tweet) :
	return tweet.truncated

# Tweet the given text
def tweet(text) :
	api.update_status(status=text)

# retweet the given tweet
def retweet(tweet) :
	api.retweet(getIdFromTweet(tweet))