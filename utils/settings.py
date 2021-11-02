
'''
# Database Setting
# Creating Database and Table
'''

import db_info
from file2db import *
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
    return db, db.cursor()

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

# Set Initial Data
def setInitData(cursor):
    query = "SELECT COUNT(*) FROM site;"
    cursor.execute(query)
    column = int(cursor.fetchone()[0])
    if column >0 : return 

    query = "INSERT INTO site (poster, intro, student_intro, graduated_intro) \
         VALUES ('MAIN_POSTER.jpg','동아리 소개글','회장 인사말','동호인 회장 인사말');"
    cursor.execute(query)
    return 


if __name__ == "__main__":
    # Get DB name
    db_name = db_info.db_name
    # Connect DB and Get cursor
    db_, cursor = getCursor()
    
    # Create DB if not DB exist
    if not checkDB(cursor, db_name):
        createDB(cursor)

    # Use DB
    cursor.execute(f"USE {db_name};")

    # Create Table if not Table exist
    for table in db_info.tables.keys():
        if not checkTable(cursor, table):
            createTable(cursor, table)

        if table == "site":
            # Input Homepage Initial Data
            setInitData(cursor)

    # storage 파일이 존재한다면, file name 통해서 db input
    member_to_db(db_)
    club_event_to_db(db_)
    profile_to_db(db_)
    photo_to_db(db_)
    # text file이 존재한다면, readlines to db
    db_.commit()