import pymysql
import datetime

host = "localhost"
username = "root"
password = "password"
db_name = "lagoux"

create_table_sql = """CREATE TABLE first_db(
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    data-company VARCHAR(255) UNIQUE,
                    data-positionname VARCHAR(255) UNIQUE,
                    add VARCHAR(255) UNIQUE,
                    money VARCHAR(255) NOT NULL,
                    industry VARCHAR(255) UNIQUE,
                    birthday DATE)
                    """


connection = pymysql.connect(host = host,
                             user = username,
                             password = password,
                             db = db_name)

try:
    with connection.cursor() as cursor:
        print("---------------新建表--------------")
        cursor.execute(create_table_sql)
        connection.commit()

finally:
    connection.close()
