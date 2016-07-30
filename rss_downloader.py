#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import feedparser


def read_rss_sources(file_path="rss_sources.txt"):
    with open(file_path) as rss_file:
        rss_list = rss_file.readlines()
        return rss_list


def get_titles():
    rss_list = read_rss_sources()
    feeds = []
    titles = {}
    for rss_source in rss_list:
        feed = feedparser.parse(rss_source)
        feeds.extend(feed["items"])

    for feed in feeds:
        link = feed["links"][0]["href"]
        title = feed["title"]
        titles[title] = link

    return titles

if __name__ == '__main__':
    t = get_titles()
    print(t.keys())