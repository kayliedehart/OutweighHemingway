#!/usr/bin/env python
import nltk
from pprint import pprint
from nltk.corpus import wordnet
from nltk.wsd import lesk
pprint(wordnet.synsets('true'))