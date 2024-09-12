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

if __name__ == '__main__':
    
    create_todo_sql="""
    -- todo table
    CREATE TABLE IF NOT EXISTS todo (
        id integer PRIMARY KEY,
        zadanie text NOT NULL,
        start_date text
        );
    """

    create_todo_details='''
    -- todo_details table
    CREATE TABLE IF NOT EXISTS todo_details(
        id integer PRIMARY KEY,
        todo_id integer NOT NULL,
        zadanie text NOT NULL,
        opis TEXT,
        status BOOLEAN,
        FOREIGN KEY (todo_id) REFERENCES todo (id)
        );
        '''
    db_file = 'todo_database.db'

    conn = create_connection(db_file)
    if conn is not None:
        execute_sql(conn, create_todo_sql)
        execute_sql(conn, create_todo_details)
        conn.close()