#!/usr/bin/python
# -*- coding: utf-8 -*-import random

from pprint import pprint
from string import punctuation as pnct
import numpy as np
import time, sys

import nltk
from nltk.wsd import lesk
from nltk.corpus import wordnet as wn
from nltk import word_tokenize as wt
from nltk.tokenize import RegexpTokenizer

nltk.download('punkt')
nltk.download('maxent_treebank_pos_tagger')

#useful dependencies used throughout 