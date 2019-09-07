import pymysql

connection = pymysql.connect("localhost", "root", "", "chinook")
cursor = connection.cursor()

sql_query = "SELECT * FROM Artist;"

try:
    cursor.execute(sql_query)
    result = cursor.fetchall()
    print(result)

finally:
    # close the connection
    connection.close()
