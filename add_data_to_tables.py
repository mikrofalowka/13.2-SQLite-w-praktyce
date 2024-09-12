import sqlite3

def create_connection(db_file):
    '''creating connection to db file'''
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(e)
    return conn

def add_todo(conn, todo):
    '''
    Create new todo task into the todo table
    :param conn:
    :param todo:
    :return: todo id'''

    sql = '''INSERT INTO todo(zadanie, start_date) VALUES(?,?)'''
    cur = conn.cursor()
    cur.execute(sql,todo)
    conn.commit()
    return cur.lastrowid

def add_todo_details(conn, todo_details):
    '''
    create todo_details for the todo table
    :param conn:
    :param todo_details:
    :return: todo_details id
    '''

    sql = '''INSERT INTO todo_details(todo_id, zadanie, opis, status)
                VALUES(?,?,?,?)'''
    cur = conn.cursor()
    cur.execute(sql,todo_details)
    conn.commit()
    return cur.lastrowid

if __name__ == '__main__':

    todo = ("zmiana oleju w samochodzie",'2024-09-11 00:00:00')
    todo2 = ('zmiana chlodnicy', '2024-09-09 00:00:00')

    conn = create_connection('todo_database.db')
    td_id = add_todo(conn,todo)
    td_id2 = add_todo(conn, todo2)

    details = (
        td_id,
        "kupic olej i filtr",
        "spuscic caly olej, wymienic filtr i wlac nowy olej",
        "not started"
    )

    details2 = (
        td_id2,
        'kupic nowa chlodnice i plyn',
        'odkrecic stara chlodnice, zamontowac nowa i zalac ja plynem',
        'started'
    )

    details_id = add_todo_details(conn,details)
    print(td_id, details_id)
    conn.commit()

    details2_id = add_todo_details(conn,details2)
    print(td_id2, details2_id)
    conn.commit()