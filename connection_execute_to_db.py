import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    '''creating connection to db file'''
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn

def execute_sql(conn,sql):
    '''execute sql
    :param conn: connection object
    :param sql: a SQL script
    :return:
    '''
    try:
        c = conn.cursor()
        c.execute(sql)
    except Error as e:
        print(e)