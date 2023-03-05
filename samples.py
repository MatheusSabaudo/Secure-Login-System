#/*******************************************************************\
#/                     CREATING THE DATABASE                         \
#/*******************************************************************\

import sqlite3
import hashlib

conn = sqlite3.connect("userdata.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS userdata (
    id INTEGER PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
)
""")

username1, password1 = "matteo", hashlib.sha256("matteopwd".encode()).hexdigest()
username2, password2 = "john", hashlib.sha256("johnpwd".encode()).hexdigest()
username3, password3 = "admin", hashlib.sha256("adminpwd".encode()).hexdigest()
username4, password4 = "test", hashlib.sha256("testpwd".encode()).hexdigest()

cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username1, password1))
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username2, password2))
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username3, password3))
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username4, password4))

conn.commit()