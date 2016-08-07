#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import graph
import db_connect
import config



def group_by_ner():

    con, cur = db_connect.connect_to_db("localhost")
    cur.execute("SELECT article_id, "
                "       compared_article_id "
                "FROM articles.ner_score "
                "WHERE score >= {threshold}"
                .format(threshold=config.NER_THRESHOLD
                        )
                )
    results = cur.fetchall()

    connections = set()
    for res in results:
        connections.add((res[0], res[1]))

    ner_graph = graph.Graph(list(connections))
    groups = ner_graph.return_connections()
    for group in groups:
        title_group = []
        for article_id in group:
            cur.execute("SELECT title "
                        "FROM articles.meta_info "
                        "WHERE id='{}'".format(article_id))
            try:
                result = cur.fetchone()[0]
                title_group.append(result)
            except IndexError:
                print("Id is not in DB.")
        print(title_group)
