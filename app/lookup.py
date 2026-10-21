"""Langfuse trace check (10.3 C): small, intentionally vulnerable code. Do not merge."""
import sqlite3
import subprocess


def find_user(db_path, username):
    conn = sqlite3.connect(db_path)
    # SQL injection: the username goes straight into the query
    return conn.execute(f"SELECT id, email FROM users WHERE name = '{username}'").fetchall()


def ping(host):
    # command injection: the host goes to a shell
    return subprocess.run(f"ping -c 1 {host}", shell=True, capture_output=True, text=True).stdout
