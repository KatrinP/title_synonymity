#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from nltk.tag.stanford import StanfordNERTagger
import config
import sys


def create_ner_bug_of_words(ner_list):
    bug_of_words = set()
    for word_tuple in ner_list:
        word = word_tuple[0]
        value = word_tuple[1]
        if value != "O":
            bug_of_words.add(word)
    return bug_of_words


def ner_evaluate(sentence):
    ner_tagger = StanfordNERTagger(config.CLASSSIFIER_MODLE,
                           config.NER_JAR)
    return ner_tagger.tag(sentence.split())

if __name__ == '__main__':

    try:
        ner_sentence = ner_evaluate(sys.argv[1])
        bug_of_words = create_ner_bug_of_words(ner_sentence)
        print(bug_of_words)
    except IndexError:
        print("ERROR: You forget to pass me your sentence. Just use command line argument.")
