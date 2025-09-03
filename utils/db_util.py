import pymysql
from config.config import DB_CONFIG

def execute_query(sql):
    conn = pymysql.connect(**DB_CONFIG)
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql)
            return cursor.fetchall()
    finally:
        conn.close()
