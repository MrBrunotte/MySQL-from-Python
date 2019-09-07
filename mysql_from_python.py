import pymysql

connection = pymysql.connect("localhost", "root", "", "chinook")
cursor = connection.cursor(pymysql.cursors.DictCursor) 
# The advantage of using the DictCursor is that the rows now include the column names.


try:
    sql_query = "SELECT * FROM Genre;"
    # the curser is the object that we use to execute queries
    cursor.execute(sql_query)
    for row in cursor:
        print(row)

finally:
    # close the connection
    connection.close()
