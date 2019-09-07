import datetime
import pymysql

connection = pymysql.connect("localhost", "root", "", "chinook")
cursor = connection.cursor() 


try:
    # create a table called Friends
    cursor.execute(""" CREATE TABLE IF NOT EXISTS
                    Friends(name char(20), age int, DOB datetime);""")
    for row in cursor:
        print(row)

finally:
    # close the connection
    connection.close()
