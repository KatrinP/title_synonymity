#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import psycopg2
import config


def connect_to_db(db_type):
    """
    Connect to DB according the configuration in config.py file
    :param db_type: name (dict key) of the DB configuration
    :return: connection, cursor
    """
    db = config.db_login_dict[db_type]
    con = psycopg2.connect(database=db.database, user=db.user, password=db.password, host=db.host)
    cur = con.cursor()
    return con, cur
