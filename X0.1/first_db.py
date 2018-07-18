import pymysql
import datetime

host = "localhost"
username = "root"
password = "password"
db_name = "lagoux"


connection = pymysql.connect(host = host,
                             user = username,
                             password = password,
                             db = db_name,
                             charset="utf8")

def insert_db(data_company, data_positionname, area, salary, experience, industry, day):
    insert_table_sql = """INSERT INTO technologys(data_company,
                                            data_positionname,
                                            adds,
                                            salary,
                                            experience,
                                            industry,
                                            birthday) VALUES (%s, %s, %s, %s, %s, %s, %s)"""

    with connection.cursor() as cursor:
        cursor.execute(insert_table_sql, (data_company, data_positionname, area, salary, experience, industry, day))
        connection.commit()



def query_db():
    query_table_sql = """
                SELECT * FROM technologys order by id desc limit 450; 
                """
    try:
        with connection.cursor() as cursor:
            cursor.execute(query_table_sql)
            result = cursor.fetchall()
            connection.commit()

    finally:
        connection.close()
    return result
