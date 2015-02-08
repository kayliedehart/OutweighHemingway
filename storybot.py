import tweepy, time, sys

argfile = str(sys.argv[1])

CONSUMER_KEY = "6T2oQQQa9Lhp1nkha6yGMCPLU"
CONSUMER_SECRET = "qZUDPATubxwPj1UapMSZgiu7wp2nmXT1hGmKEtTvXs3o5ssopv"
ACCESS_KEY = "3023771686-9AyE23kmZBb6vcXRTS1GZP8L27sfD7v8oERo2lT"
ACCESS_SECRET = "VyAC443dOez7ZlUhtanOf1K1zUiIBvyIvqNMZUQppgms4"
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

filename=open(argfile, 'r')
f=filename.readlines()
filename.close()

for line in f:
	api.update_status(status=line)
	time.sleep(900) #Tweet every 15 minutes
