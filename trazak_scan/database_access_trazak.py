import MySQLdb

DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASS = 'root'
DB_NAME = 'trazak'


def run_query(query=''):
    db_info = [DB_HOST, DB_USER, DB_PASS, DB_NAME]

    conn = MySQLdb.connect(*db_info)  # Connect to the DB
    cursor = conn.cursor()  # Create a cursor
    cursor.execute(query)  # Execute a query

    if query.upper().startswith('SELECT'):
        data = cursor.fetchall()  # Get select results
    else:
        conn.commit()  # Do effective the writing of data
        data = None

    cursor.close()  # Close the cursor
    conn.close()  # Close the connection

    return data


def insert_values(query):
    db_info = [DB_HOST, DB_USER, DB_PASS, DB_NAME]

    conn = MySQLdb.connect(*db_info)  # Connect to the DB
    cursor = conn.cursor()  # Create a cursor

    try:
        cursor.execute(query)  # Execute a query
        conn.commit()
    except:
        conn.rollback()
        print "The record cannot be inserted in the table"
    cursor.close()  # Close the cursor
    conn.close()  # Close the connection