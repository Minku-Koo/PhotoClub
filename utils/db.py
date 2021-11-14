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

        query = """
        INSERT INTO user (name, major, number, profile, position, graduate)  
        VALUES (%s, %s, %s, %s, %s , %s);
        """
        
        self.__cursor__.execute( query, (
                                    name, 
                                    major, 
                                    number, 
                                    profile, 
                                    position, 
                                    graduate
                                ) )

        return 


    def check_user_exist(self, number, name):
        query = """
        SELECT * FROM user
        WHERE number=%s  AND name=%s;
        """
        self.__cursor__.execute( query, ( number, name) )
        if self.__cursor__.fetchone(): 
            return True
        return False

    def update_user(self, number, major, name, profile):
        query = """
        UPDATE user SET major=%s , profile=%s 
        WHERE number=%s  AND name=%s;
        """
        self.__cursor__.execute( query, ( major,  profile, number, name ) )
        return

    def insert_photo(self, user_id, file):
        query = """
        INSERT INTO photo (user_id, file) 
        values (%s, %s);
        """

        self.__cursor__.execute( query, (user_id, file) )
        return 

    def get_fresh_student(self):
        query = """
        SELECT MAX(number) FROM user ;
        """
        self.__cursor__.execute(query)
        return int(self.__cursor__.fetchone()[0])
    
    def get_user_name_num(self, user_id):
        query = """
        SELECT name, number, graduate FROM user where id= %s ;
        """
        self.__cursor__.execute( query, (user_id))
        # print(self.__cursor__.fetchone())
        return self.__cursor__.fetchone()

    def get_user_id(self, number, name):
        query = """
        SELECT id FROM user where number= %s AND name=%s ;
        """
        self.__cursor__.execute( query, (number, name))
        #print(self.__cursor__.fetchone())
        return self.__cursor__.fetchone()[0]

    def get_user_photo_info(self):
        # 재학생 신입생 동호인
        student, freshman, clubman = [], [], []
        fresh_num = self.get_fresh_student()

        query = """
        SELECT user_id, file FROM photo ;
        """

        self.__cursor__.execute(query)
        for user_id, filename in self.__cursor__.fetchall():
            data = {"artist":"" , "image":""}
            #print("user_id",user_id)
            name, num, graduate = self.get_user_name_num(user_id)
            data["image"] = filename
            data["artist"] = "th ".join( [str(num), name] )
            if num==fresh_num: # 신입생
                freshman.append( data )
            elif graduate == 1: #동호인
                clubman.append( data )
            else:
                student.append( data )
        
        return (student, freshman, clubman)
    
    
    def insert_club_event(self, title, year):
        sql = """
        INSERT INTO club_event (title, year) 
        values (%s, %s);
        """
        self.__cursor__.execute(sql, (title, int(year)))
        return 

    def get_club_event(self):
        query = """
        SELECT title, year FROM club_event ORDER BY year DESC;
        """
        self.__cursor__.execute( query)
        return self.__cursor__.fetchall()

    def get_username(self, id):
        query = """
        SELECT name FROM user WHERE id= %s ;
        """

        self.__cursor__.execute( query, (id))
        return self.__cursor__.fetchone()[-1]

    def get_chairs(self):
        result = {"student":[],"club_member":[]}
        query = """
        SELECT name, major, number FROM user WHERE position='chair' AND graduate=0 ;
        """
        self.__cursor__.execute( query)
        result["student"] = list(self.__cursor__.fetchone())

        query = """
        SELECT name, number FROM user WHERE position='chair' AND graduate=1 ;
        """
        self.__cursor__.execute( query)
        result["club_member"] = list(self.__cursor__.fetchone())

        return result

    def get_other_users(self):
        result = {"student":[],"club_member":[]}
        query = """
        SELECT name, major, number FROM user WHERE position!='chair' AND graduate=0 ;
        """
        self.__cursor__.execute( query)
        result["student"] = list(self.__cursor__.fetchall())

        query = """
        SELECT name, number FROM user WHERE position!='chair' AND graduate=1 ;
        """
        self.__cursor__.execute( query)
        result["club_member"] = list(self.__cursor__.fetchall())

        return result

    def get_userpic(self, name, number):
        query = """
        SELECT profile FROM user WHERE name= %s AND number=%s ;
        """

        self.__cursor__.execute( query, (name, number))
        return self.__cursor__.fetchone()[-1]

    def update_site(self, poster, intro, student_intro, grad_intro):
        query = """
        UPDATE site SET poster=%s,
                     intro=%s,
                     student_intro=%s,
                     graduated_intro=%s 
        WHERE no=1;
        """

        self.__cursor__.execute( query, (
                                    poster, intro, student_intro, grad_intro
                                ) )
        return 

    def get_site(self):
        sql = """
        SELECT poster, intro, student_intro, graduated_intro FROM site;
        """
        self.__cursor__.execute(sql)
        return self.__cursor__.fetchone()

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

    def faq_insert(self, question, answer):
        sql = """
        INSERT INTO faq (question, answer) 
        values (%s, %s);
        """
        self.__cursor__.execute(sql, (question, answer))
        return 

    def get_faq(self):
        query = f"""
        SELECT question, answer FROM faq;
        """
        self.__cursor__.execute(query)
        return self.__cursor__.fetchall()

    def insert_history(self, filename, title, year):
        sql = """
        INSERT INTO history (file, event_title, year) 
        values (%s, %s, %s);
        """
        self.__cursor__.execute(sql, (filename, title, year))
        return 

    def get_history(self):
        query = f"""
        SELECT file, year, event_title FROM history
        ORDER BY year;
        """
        self.__cursor__.execute(query)
        return self.__cursor__.fetchall()

    def update_chair(self, 
                    student_num,
                    student_name,
                    graduate_num,
                    graduate_name):
                    
        query = """
        UPDATE user SET position='chair' 
        WHERE number=%s AND name=%s ;
        """
        self.__cursor__.execute(query, (int(student_num), student_name))
        self.__cursor__.execute(query, (int(graduate_num), graduate_name))
        return