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

def query_db(name):
    query_table_sql = """
                SELECT * FROM technologys where data_positionname like '%s' order by lagoux_id desc limit 450;
                """ %(name)
    with connection.cursor() as cursor:
        cursor.execute(query_table_sql)
        result = cursor.fetchall()

    return result

# 检查数据库中是否有当天的数据
def verifica(name):
    verifica_table_sql = """
                        SELECT birthday FROM technologys where data_positionname like '%s' order by lagoux_id desc limit 1;
                        """ %(name)

    with connection.cursor() as cursor:
        cursor.execute(verifica_table_sql)
        result = cursor.fetchone()

    return str(result)
