import pymysql

connection = pymysql.connect("localhost", "root", "", "chinook")
cursor = connection.cursor()


try:
    list_of_names = ['fred', 'fred', 'Rebecca']
    # prepare a string with the same number of placeholders as in list_of_names
    format_strings = ','.join(['%s']*len(list_of_names))
    cursor.execute("DELETE FROM Friends WHERE name in ({});".format(format_strings), list_of_names)
    connection.commit()

finally:
    # close the connection
    connection.close()
