#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from nltk.tag.stanford import StanfordNERTagger
import config
import sys
import db_connect


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


def count_ner_score(article_id, ner):
    con, cur = db_connect.connect_to_db("localhost")
    cur.execute("SELECT id, "
                "       ner "
                "FROM articles.meta_info "
                "WHERE id!='{}'"
                .format(article_id))
    results = cur.fetchall()
    for res in results:
        id_compared_article = res[0]
        ner_compared_article = res[1]
        try:
            ner_compared_article = ner_compared_article[0]
        except IndexError:
            pass

        ner_compared_article = set(ner_compared_article)
        basic_score = len(ner_compared_article & ner)
        weighted_score = basic_score ** config.NER_WEIGHT_CONSTANT

        cur.execute("SELECT id "
                    "FROM articles.ner_score "
                    "WHERE article_id='{article_id}' "
                    "  and compared_article_id='{compared_id}' "
                    .format(article_id=article_id,
                            compared_id=id_compared_article
                            )
                    )
        results = cur.fetchall()
        if not results:
            cur.execute("INSERT INTO articles.ner_score "
                        "  (article_id,"
                        "   compared_article_id,"
                        "   score)"
                        "VALUES "
                        "  ('{article_id}',"
                        "   '{compared_article_id}',"
                        "   {score}"
                        ")"
                        .format(article_id=article_id,
                                compared_article_id=id_compared_article,
                                score=weighted_score,
                                )
                        )
            con.commit()


if __name__ == '__main__':

    try:
        ner_sentence = ner_evaluate(sys.argv[1])
        bug_of_words = create_ner_bug_of_words(ner_sentence)
        print(bug_of_words)
    except IndexError:
        print("ERROR: You forget to pass me your sentence. Just use command line argument.")
