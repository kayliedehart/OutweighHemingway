##Outweigh Hemingway: a story-telling twitterbot
#authors kayliedehart, alexhersh, alexia7, boltcutter

#Main is executed with a "keyword" argument- the story topic
import tweepy
import wordParse
import checkSimilar
import sys

kw = sys.argv[1]
storyArch = [None]*10
i = 0

######Story Beginning logic
#One Tweet: pull in tweet
first = tweepy.keywordSearch(kw, 1)[0]
#update story
storyArch[i] = first.text
i++
#send keyword to checkSimilar for comparison
checkSimilar...(kw)



######Intermediate tweets
for i <=9:
	currentTweets = [None]*20
	if (i <4):
		#The "Choose Your Own Adventure" Phase: Choose Three
		currentTweets = tweepy.keywordSearch(kw, 20)
		#send to parse
		wordParse.sendScrape(currentTweets)
		currentText = wordParse.getBest()

	else if (i <6)
		##Conflict
		#Limit to "Negative" tweets: Two
		currentTweets = tweepy.keywordSearch(kw, 20)
		#send to parse
		wordParse.sendScrape(currentTweets)
		currentText = wordParse.getBest()
	else
		##Resolution
		#Limit to "Positive" tweets: Two
		#send to parse
		wordParse.sendScrape(currentTweets)
		currentText = wordParse.getBest()
	storyArch[i] = currentText
	i++


#######Story ending logic
storyArch[i] = "#FIN"

#Tweet each tweet in 2 minute intervals
for x in storyArch:
	tweetOut(x)
	wait(1200)

