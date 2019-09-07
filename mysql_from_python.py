import pymysql

connection = pymysql.connect("localhost", "root", "", "chinook")
cursor = connection.cursor()


try:
    rows = cursor.execute("DELETE FROM Friends WHERE name = %s;", 'Fred')
    connection.commit()

finally:
    # close the connection
    connection.close()
