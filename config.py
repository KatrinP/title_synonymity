#!/usr/bin/python3
# -*- coding: UTF-8 -*-

CLASSSIFIER_MODLE = '/usr/share/stanford-ner/classifiers/english.all.3class.distsim.crf.ser.gz'
NER_JAR = '/usr/share/stanford-ner/stanford-ner.jar'


class DBlogin():
    def __init__(self, database, user, password, host):
        self.database = database
        self.user = user
        self.password = password
        self.host = host


db_login_dict = {
    "localhost": DBlogin("title_synonymity", "postgres", "1561991",
                         "127.0.0.1")
}
