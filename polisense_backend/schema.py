#!/usr/bin/env python3

import sqlite3


connection = sqlite3.connect('objects.db',check_same_thread=False)
cursor = connection.cursor()


create_statement = 'CREATE TABLE objects(pk INTEGER PRIMARY KEY AUTOINCREMENT, objectid VARCHAR, filename VARCHAR);'
cursor.execute(create_statement)


cursor.close()
connection.close()