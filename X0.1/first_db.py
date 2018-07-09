import pymysql
import datetime

host = "localhost"
username = "root"
password = "password"
db_name = "lagoux"


connection = pymysql.connect(host = host,
                             user = username,
                             password = password,
                             db = db_name)
def create_db():
    create_table_sql = """CREATE TABLE first_db(
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        data_company VARCHAR(255) NOT NULL,
                        data_positionname VARCHAR(255) NOT NULL,
                        adds CHAR(20) NOT NULL,
                        salary VARCHAR(20) NOT NULL,
                        industry VARCHAR(255) NOT NULL,
                        birthday DATE)
                        """
    try:
        with connection.cursor() as cursor:
            cursor.execute("DROP TABLE IF EXISTS first_db")
            print("---------------新建表--------------")
            cursor.execute(create_table_sql)
            connection.commit()

    finally:
        connection.close()

def insert_db():
    insert_table_sql = """INSERT INTO first_db(data_company,
                                            data_positionname,
                                            adds,
                                            salary,
                                            industry,
                                            birthday) VALUES (%s, %s, %s, %s, %s, %s)"""

    try:
        with connection.cursor() as cursor:
            cursor.execute(insert_table_sql)
            connection.commit()

    finally:
        connection.close()

def query_db():
    query_table_sql = """
                SELECT * FROM first_db
                """
    try:
        with connection.cursor() as cursor:
            cursor.execute(query_table_sql)
            connection.commit()

    finally:
        connection.close()
