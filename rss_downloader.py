#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import feedparser
from datetime import datetime
import db_connect


class RSSrecord:
    def __init__(self):
        self.source = None
        self.title = None
        self.url = None
        self.timestamp = None


def read_rss_sources(file_path="rss_sources.txt"):
    with open(file_path) as rss_file:
        rss_list = rss_file.readlines()
        return rss_list


def get_feeds():
    rss_list = read_rss_sources()
    news_meta = []

    for rss_source in rss_list:
        feed = feedparser.parse(rss_source)
        for news in feed.entries:
            rss_record = RSSrecord()
            rss_record.source = feed.feed.title
            rss_record.url = news.links[0].href
            try:
                rss_record.timestamp = datetime.strptime(news.published, "%a, %d %b %Y %H:%M:%S %Z")
            except ValueError:
                rss_record.timestamp = datetime.now()
            rss_record.title = news.title
            news_meta.append(rss_record)
    return news_meta


def store_titles(news_meta):
    con, cur = db_connect.connect_to_db("localhost")


if __name__ == '__main__':
    f = get_feeds()
    print(store_titles(f))
