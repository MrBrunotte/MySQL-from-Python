import pymysql

connection = pymysql.connect("localhost", "root", "", "chinook")
cursor = connection.cursor()


try:
    rows = cursor.executemany("DELETE FROM Friends WHERE name = %s;", ['Fred', 'Stefan'])
    connection.commit()

finally:
    # close the connection
    connection.close()
