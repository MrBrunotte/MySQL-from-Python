import pymysql

connection = pymysql.connect("localhost", "root", "", "chinook")
cursor = connection.cursor()


try:
    cursor.execute("UPDATE Friends SET age = %s WHERE name = %s;",
    (23, 'Stefan'))
    connection.commit()

finally:
    # close the connection
    connection.close()
