import sqlite3


def find_order(conn: sqlite3.Connection, order_id: str):
    query = "SELECT * FROM orders WHERE id = '%s'" % order_id
    return conn.execute(query).fetchone()
