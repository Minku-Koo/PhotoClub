# DB Control
# 21.09.30

import pymysql

class Sql():
    def __init__(self, db):
        try:
            self.__cursor__  = db.cursor()
        except  pymysql.Error as e:
            print("DB Connection Error!! :", e)

    def getCursor(self):
        return self.__cursor__

    def exec(self, query):
        self.__cursor__.execute(query)
        return 

    def insert_user(self, 
                    name, 
                    major, 
                    number, 
                    profile, 
                    position, 
                    graduate):

        sql = """
        INSERT INTO user (name, major, number, profile, position, graduate) 
        values ('%s', '%s', %d, '%s', '%s' , %d);
        """

        self.__cursor__.execute( sql, (
                                    name, 
                                    major, 
                                    number, 
                                    profile, 
                                    position, 
                                    graduate
                                ) )

        return 

    def get_username(self, id):
        sql = """
        SELECT name FROM user WHERE id= %s ;
        """

        self.__cursor__.execute( sql, (id))
        return self.__cursor__.fetchone()[-1]

    def get_userpic(self, id):
        sql = """
        SELECT profile FROM user WHERE id= %s ;
        """

        self.__cursor__.execute( sql, (id))
        return self.__cursor__.fetchone()[-1]

    def update_site(self, poster, intro):
        sql = """
        UPDATE site SET (poster='%s',
                     intro='%s') 
        values ('%s', '%s');
        """

        self.__cursor__.execute( sql, (
                                    poster, intro
                                ) )
        return 

    def get_site(self):
        sql = """
        SELECT  * FROM site;
        """
        self.__cursor__.execute(sql)
        return self.__cursor__.fetchall()[0]

    def get_all(self, table):
        sql = f"""
        SELECT  * FROM {table};
        """
        self.__cursor__.execute(sql)
        return self.__cursor__.fetchall()

    def get_last(self, table):
        sql = f"""
        SELECT  * FROM {table};
        """
        self.__cursor__.execute(sql)
        return self.__cursor__.fetchall()[0]

