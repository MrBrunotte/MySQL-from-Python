import datetime
import pymysql

connection = pymysql.connect("localhost", "root", "", "chinook")
cursor = connection.cursor() 


try:
    # For readability the values will be stored in a TULP which we call row
    row = ("Stefan", 47, "1972-02-17 01:15:45")
    # to insert a single row into a table, use the standard SQL INSERT command using a cursor
    # The cursor unpacks the TULP and inserts the three VALUE into the INSERT statement
    # %s, %s, %s represents the three items in the TULP 
    cursor.execute("INSERT INTO Friends VALUES(%s, %s, %s);", row)
    connection.commit()

finally:
    # close the connection
    connection.close()
