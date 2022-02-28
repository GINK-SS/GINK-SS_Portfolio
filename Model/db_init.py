from flask import g
from pymysql import *

# DB 연결
def get_db():
    if 'db' not in g:
        g.db = connect(
            host="localhost", 
            user="root", 
            password="0000",
            db="Portfolio",
            charset='utf8mb4', 
            cursorclass=cursors.DictCursor
        )

# DB 해제
def close_db():
    db = g.pop('db', None)
    if db is not None:
        if db.open:
            db.close()