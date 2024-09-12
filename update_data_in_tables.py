import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    '''creating connection to db file'''
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(e)
    return conn

def update(conn, table, id, **kwargs):
    """
   update status, begin_date, and end date of a task
   :param conn:
   :param table: table name
   :param id: row id
   :return:
   """
    parameters = [f"{k} = ?" for k in kwargs]
    parameters = ", ".join(parameters)
    values = tuple(v for v in kwargs.values())
    values += (id, )

    sql = f''' UPDATE {table}
            SET {parameters}
            WHERE id = ?'''
    try:
        cur = conn.cursor()
        cur.execute(sql, values)
        conn.commit()
        print("OK")
    except sqlite3.OperationalError as e:
        print(e)

if __name__ == "__main__":
   conn = create_connection("todo_database.db")
   update(conn, "todo_details", 1, status="started")
   update(conn, "todo_details", 3, status="not started")
   conn.close()