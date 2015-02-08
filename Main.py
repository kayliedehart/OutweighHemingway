##Outweigh Hemingway: a story-telling twitterbot
#authors kayliedehart, alexhersh, alexia7, boltcutter

#Main is executed with a "keyword" argument- the story topic
from tweepyFunctions import *
import checkSimilar
import sys, time, random

kw = sys.argv[1]
keylist = [kw]
storyArch = []

######Story Beginning logic
#One Tweet: pull in tweet
first = keywordSearch(kw, 1)[0]
#update story
storyArch.append(first)

string = parser.tokenize(first.text)
for noun in getNouns(string) :
	keylist.append(noun)


## add similar words to shopping list
# for sim in getSimilarWords(kw, 5) :
# 	keylist.append(sim.name)

######Intermediate tweets
for i in range (1,10) :
	candidateTweets = []

	if (i < 4):
		#The "Choose Your Own Adventure" Phase: Choose Three
		candidateTweets = checkSimilar.keywordSearch(keylist[random.randint(0, len(keylist) - 1)], 20)
		thisTweet = checkSimilar.getBest(candidates = candidateTweets, keywords=[kw], sentiment='neutral') # getBest will use tokenizer functions

	else if (i < 6) :
		##Conflict
		#Limit to "Negative" tweets: Two
		candidateTweets = checkSimilar.keywordSearch(keylist.pop(random.randint(0, len(keylist) - 1)), 20)
		thisTweet = checkSimilar.getBest(candidates = candidateTweets, keywords=[kw], sentiment='negative') # getBest will use tokenizer functions

	else :
		##Resolution
		#Limit to "Positive" tweets: Two
		candidateTweets = checkSimilar.keywordSearch(keylist.pop(random.randint(0, len(keylist) - 1)), 20)
		thisTweet = checkSimilar.getBest(candidates = candidateTweets, keywords=[kw], sentiment='positive') # getBest will use tokenizer functions

	storyArch.append(thisTweet)
	# story words

#Tweet each tweet in 2 minute intervals
for tweetObj in storyArch :
	print tweetObj.text
	#retweet(tweetObj) #dont retweet until it works!
	wait(1200)

#######Story ending tweet
# tweet("#FIN #OverweighHemingway")

