# command to for mysql connector
# pip install mysql-connector-python


# frist sql to python 

import mysql.connector
def select_records():
    # connect to the databse
    connection = mysql.connector.connect(host='localhost', user='root', password= 'admin123', database= 'personsdb')
    # create a query
    query = "select id, name, address, age from perosn"

    # get the cursur(in-memory table)
    cursor = connection.cursor()

    #  execute the query
    cursor.execute(query)

    #  get query result
    result = cursor.fetchall()

    #  process the result
    print(result)

    #close the cursor 

    cursor.close()

    #close connection
    connection.close()
select_records()