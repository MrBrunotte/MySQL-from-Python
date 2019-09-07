import datetime
import pymysql

connection = pymysql.connect("localhost", "root", "", "chinook")
cursor = connection.cursor()


try:
    rows = [("Stefan", 47, "1972-02-17 01:15:45"),
            ("Rebecca", 47, "1972-04-11 03:45:25"),
            ("Fred", 19, "2000-10-05 15:17:50")]
    cursor.executemany("INSERT INTO Friends VALUES(%s, %s, %s);", rows)
    connection.commit()

finally:
    # close the connection
    connection.close()
