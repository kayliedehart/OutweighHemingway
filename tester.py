#!/usr/bin/env python
# -*- coding: utf-8 -*-

import spacy.en
from spacy.parts_of_speech import ADV
nlp = spacy.en.English()
from numpy import dot
from numpy.linalg import norm

# cosine function IDK WHY WE DO THIS
cosine = lambda v1, v2: dot(v1, v2) / (norm(v1), norm(v2))

# tokenize the word (use unicode characters)
tokens = nlp(u"‘Give it back,’ he pleaded abjectly, ‘it’s mine.’")

probs = [lex.prob for lex in nlp.vocab]
probs.sort()


pleaded = tokens[7]


# wordlistvb
words = [w for w in nlp.vocab]

# sort by cosine
words.sort(key=lambda w: cosine(w, pleaded))
words.reverse()
print('1-20', ', '.join(w.orth_ for w in words[0:20]))
print('50-60', ', '.join(w.orth_ for w in words[50:60]))
print('100-110', ', '.join(w.orth_ for w in words[100:110]))
print('1000-1010', ', '.join(w.orth_ for w in words[1000:1010]))
