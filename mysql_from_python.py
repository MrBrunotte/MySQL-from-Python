import pymysql

connection = pymysql.connect("localhost", "root", "", "chinook")
cursor = connection.cursor()


try:
    cursor.execute("DELETE FROM Friends WHERE name = 'Stefan';")
    connection.commit()

finally:
    # close the connection
    connection.close()
