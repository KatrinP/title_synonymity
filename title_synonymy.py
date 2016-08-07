#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import sys
import argparse
import db_connect
import ner_manager
import rss_downloader
import grouping


def parse_command_line():
    parser = argparse.ArgumentParser(description="Title Synonymy compares two newspaper titles "
                                                 "and gives a probability, that the two "
                                                 "articles are of the same topic."
                                     )

    parser.add_argument("-l", "--language",
                        help="Sorry, guy. Just English is supported right now...",
                        default="en"
                        )
    parser.add_argument('-v', '--version', action='version', version='%(prog)s 1.0')
    #parser.add_argument("first_sentence", help="First sentence to compare")
    #parser.add_argument("second_sentence", help="Second sentence to compare")

    return parser.parse_args()


def store_titles(news_meta):
    con, cur = db_connect.connect_to_db("localhost")
    for news in news_meta:
        cur.execute("SELECT id "
                    "FROM articles.meta_info "
                    "WHERE title='{title}' "
                    "  AND url='{url}'"
                    .format(title=news.title,
                            url=news.url)
                    )
        results = cur.fetchall()
        if not results:
            ner_sentence = ner_manager.ner_evaluate(news.title)
            bug_of_words = ner_manager.create_ner_bug_of_words(ner_sentence)

            cur.execute("INSERT INTO articles.meta_info "
                        "    (title,"
                        "     url,"
                        "     published_at,"
                        "     ner"
                        ")"
                        "VALUES ('{title}',"
                        "        '{url}',"
                        "        '{published_at}',"
                        "        ARRAY[{ner}]::VARCHAR[]"
                        ") RETURNING id"
                        .format(title=news.title,
                                url=news.url,
                                published_at=news.published,
                                ner=list(bug_of_words)
                                )
                        )
            article_id = cur.fetchone()[0]
            con.commit()

            ner_manager.count_ner_score(article_id, bug_of_words)

        else:
            for res in results:
                cur.execute("UPDATE articles.meta_info "
                            "SET published_at='{published_at}' "
                            "WHERE id='{id}'"
                            .format(published_at=news.published,
                                    id=res[0]))
    con.close()


if __name__ == '__main__':
    cl_args = parse_command_line()
    #new_meta = rss_downloader.get_feeds()
    #store_titles(new_meta)
    grouping.group_by_ner()
