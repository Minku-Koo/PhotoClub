
'''
# Database Setting
# Creating Database and Table
'''

import db_info
import pymysql

# Connect Database and Get Cursor
def getCursor():
    db = pymysql.connect(
        host = db_info.host,
        user = db_info.user,
        password = db_info.pwd,
        charset = db_info.charset,
        port = 3306
    )
    return db.cursor()

# Check DB exist
def checkDB(cursor, db_name):
    cursor.execute(f"SHOW DATABASES LIKE '{db_name}';")
    if cursor.fetchone(): return True
    else: return False

# Create DB
def createDB(cursor):
    db_name = db_info.db_name
    query = "CREATE DATABASE %s default CHARACTER SET UTF8;"
    cursor.execute(query %(db_name))
    return

# Check Table exist
def checkTable(cursor, table_name):
    cursor.execute(f"SHOW TABLES LIKE '{table_name}';")
    if cursor.fetchone(): return True
    else: return False

# Create Table
def createTable(cursor, table_name):
    query = f"CREATE TABLE {table_name} ({db_info.tables[table_name]});"
    cursor.execute(query)
    return 



if __name__ == "__main__":
    # Get DB name
    db_name = db_info.db_name
    # Connect DB and Get cursor
    cursor = getCursor()
    
    # Create DB if not DB exist
    if not checkDB(cursor, db_name):
        createDB(cursor)

    # Use DB
    cursor.execute(f"USE {db_name};")

    # Create Table if not Table exist
    for table in db_info.tables.keys():
        if not checkTable(cursor, table):
            createTable(cursor, table)
    