##Outweigh Hemingway: a story-telling twitterbot
#authors kayliedehart, alexhersh, alexia7, boltcutter

#Main is executed with a "keyword" argument- the story topic
from tweepyFunctions import *
from checkSimilar import checkSimilar, getBest
import sys, time

kw = sys.argv[1]
storyArch = []
i = 0

######Story Beginning logic
#One Tweet: pull in tweet
first = keywordSearch(kw, 1)[0]
#update story
storyArch.append(first)
i++
#send keyword to checkSimilar for comparison
checkSimilar()

######Intermediate tweets
for i in range (1,10) :
	candidateTweets = []

	if (i < 4):
		#The "Choose Your Own Adventure" Phase: Choose Three
		candidateTweets = keywordSearch(kw, 20)
		thisTweet = getBest(candidates = candidateTweets, keywords=[kw], sentiment='neutral') # getBest will use tokenizer functions

	else if (i < 6) :
		##Conflict
		#Limit to "Negative" tweets: Two
		candidateTweets = keywordSearch(kw, 20)
		thisTweet = getBest(candidates = candidateTweets, keywords=[kw], sentiment='negative') # getBest will use tokenizer functions

	else :
		##Resolution
		#Limit to "Positive" tweets: Two
		candidateTweets = keywordSearch(kw, 20)
		thisTweet = getBest(candidates = candidateTweets, keywords=[kw], sentiment='positive') # getBest will use tokenizer functions

	storyArch.append(thisTweet)
	# story words

#Tweet each tweet in 2 minute intervals
for tweetObj in storyArch :
	print tweetObj.text
	#retweet(tweetObj) #dont retweet until it works!
	wait(1200)

#######Story ending tweet
tweet("#FIN #OverweighHemingway")

