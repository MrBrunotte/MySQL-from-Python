import datetime
import pymysql

connection = pymysql.connect("localhost", "root", "", "chinook")
cursor = connection.cursor()


try:
    cursor.execute("UPDATE Friends SET age = 22 WHERE name = 'Stefan';")
    connection.commit()

finally:
    # close the connection
    connection.close()
