#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from nltk.tag.stanford import StanfordNERTagger
st = StanfordNERTagger('/usr/share/stanford-ner/classifiers/english.all.3class.distsim.crf.ser.gz',
                       '/usr/share/stanford-ner/stanford-ner.jar')
print(st.tag('Chris Mason: Owen Smith attempts to woo Corbyn backers'.split()))
print(st.tag('How should media report terror attacks?'.split()))
