#!/usr/bin/python
# -*- coding: utf-8 -*-import random

import tweepy
from secrets import *

# secrets define keys and secrets
# CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET

# setup authentication protocols
# use 'from TwitterSetup import api' to use api

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)