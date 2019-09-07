import pymysql

connection = pymysql.connect("localhost", "root", "", "chinook")
cursor = connection.cursor()


try:
    rows = [(23, 'Stefan'),
            (25, 'Rebecca'),
            (25, 'Fred')]
    cursor.executemany("UPDATE Friends SET age = %s WHERE name = %s;", rows)
    connection.commit()

finally:
    # close the connection
    connection.close()
