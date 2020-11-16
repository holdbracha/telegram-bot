import pymysql
from config import *

connection = pymysql.connect(
    host="localhost",
    user="root",
    password=SQL_PASSWORD,
    db=SQL_DB,
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor
)

# def get_sql_connection():
#     return connection

def add_message_to_db(mes):
    with connection.cursor() as cursor:
        query = "INSERT INTO MathBotHistory VALUES(\"{}\", {})".format(mes.action, int(mes.value))
        cursor.execute(query)
        connection.commit()

def get_popular_input_number():
    with connection.cursor() as cursor:
        query = """SELECT input_number
FROM MathBotHistory  GROUP BY input_number 
order by COUNT(input_number) desc"""
        cursor.execute(query)
        result = cursor.fetchone()
        return result['input_number']
