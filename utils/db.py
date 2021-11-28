# DB Control
# 21.09.30

import pymysql

class Sql():
    def __init__(self, db):
        try:
            self.db = db
            self.__cursor__  = db.cursor()
        except  pymysql.Error as e:
            print("DB Connection Error!! :", e)

    def closeCursor(self):
        self.__cursor__.close()
        return

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
        self.__cursor__  = self.db.cursor()
        self.__cursor__.execute( query, (
                                    name, 
                                    major, 
                                    number, 
                                    profile, 
                                    position, 
                                    graduate
                                ) )
        self.__cursor__.close()
        return 


    def check_user_exist(self, number, name):
        self.__cursor__  = self.db.cursor()
        query = """
        SELECT * FROM user
        WHERE number=%s  AND name=%s;
        """
        self.__cursor__.execute( query, ( number, name) )
        if self.__cursor__.fetchone(): 
            return True
        return False

    def update_user(self, number, major, name, profile):
        self.__cursor__  = self.db.cursor()
        query = """
        UPDATE user SET major=%s , profile=%s 
        WHERE number=%s  AND name=%s;
        """
        self.__cursor__.execute( query, ( major,  profile, number, name ) )
        self.__cursor__.close()
        return

    def insert_photo(self, user_id, file):
        self.__cursor__  = self.db.cursor()
        query = """
        INSERT INTO photo (user_id, file) 
        values (%s, %s);
        """

        self.__cursor__.execute( query, (user_id, file) )
        self.__cursor__.close()
        return 

    def get_fresh_student(self):
        self.__cursor__  = self.db.cursor()
        query = """
        SELECT MAX(number) FROM user ;
        """
        self.__cursor__.execute(query)
        result = int(self.__cursor__.fetchone()[0])
        self.__cursor__.close()
        return  result
    
    def get_user_name_num(self, user_id):
        self.__cursor__  = self.db.cursor()
        query = """
        SELECT name, number, graduate FROM user where id= %s ;
        """
        self.__cursor__.execute( query, (user_id))
        result = self.__cursor__.fetchone() 
        self.__cursor__.close()
        return result

    def get_user_id(self, number, name):
        self.__cursor__  = self.db.cursor()
        query = """
        SELECT id FROM user where number= %s AND name=%s ;
        """
        self.__cursor__.execute( query, (number, name))
        result = self.__cursor__.fetchone()[0]
        self.__cursor__.close()
        return  result

    def get_user_photo_info(self):
        
        # 재학생 신입생 동호인
        student, freshman, clubman = [], [], []
        fresh_num = self.get_fresh_student()
        self.__cursor__  = self.db.cursor()
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
        
        self.__cursor__.close()
        return (student, freshman, clubman)
    
    
    def insert_club_event(self, title, year):
        self.__cursor__  = self.db.cursor()
        sql = """
        INSERT INTO club_event (title, year) 
        values (%s, %s);
        """
        self.__cursor__.execute(sql, (title, int(year)))
        self.__cursor__.close()
        return 

    def get_club_event(self):
        self.__cursor__  = self.db.cursor()
        query = """
        SELECT title, year FROM club_event ORDER BY year DESC;
        """
        self.__cursor__.execute( query)
        result = self.__cursor__.fetchall()
        self.__cursor__.close()
        return  result

    def get_username(self, id):
        self.__cursor__  = self.db.cursor()
        query = """
        SELECT name FROM user WHERE id= %s ;
        """

        self.__cursor__.execute( query, (id))
        result = self.__cursor__.fetchone()[-1] 
        self.__cursor__.close()
        return  result

    def get_chairs(self):
        self.__cursor__  = self.db.cursor()
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
        self.__cursor__.close()
        return result

    def get_other_users(self):
        self.__cursor__  = self.db.cursor()
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
        self.__cursor__.close()
        return result

    def get_userpic(self, name, number):
        self.__cursor__  = self.db.cursor()
        query = """
        SELECT profile FROM user WHERE name= %s AND number=%s ;
        """

        self.__cursor__.execute( query, (name, number))
        result = self.__cursor__.fetchone()[-1]
        self.__cursor__.close()
        return  result

    def update_site(self, poster, intro, student_intro, grad_intro):
        self.__cursor__  = self.db.cursor()
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
        self.__cursor__.close()
        return 

    def get_site(self):
        self.__cursor__  = self.db.cursor()
        sql = """
        SELECT poster, intro, student_intro, graduated_intro FROM site;
        """
        self.__cursor__.execute(sql)
        result = self.__cursor__.fetchone()
        self.__cursor__.close()
        return result

    def get_all(self, table):
        self.__cursor__  = self.db.cursor()
        sql = f"""
        SELECT  * FROM {table};
        """
        self.__cursor__.execute(sql)
        result = self.__cursor__.fetchall()
        self.__cursor__.close()
        return  result

    def get_last(self, table):
        self.__cursor__  = self.db.cursor()
        sql = f"""
        SELECT  * FROM {table};
        """
        self.__cursor__.execute(sql)
        result = self.__cursor__.fetchall()[0]
        self.__cursor__.close()
        return  result

    def faq_insert(self, question, answer):
        self.__cursor__  = self.db.cursor()
        sql = """
        INSERT INTO faq (question, answer) 
        values (%s, %s);
        """
        self.__cursor__.execute(sql, (question, answer))
        return 

    def get_faq(self):
        self.__cursor__  = self.db.cursor()
        query = f"""
        SELECT question, answer FROM faq;
        """
        self.__cursor__.execute(query)
        result = self.__cursor__.fetchall()
        self.__cursor__.close()
        return  result

    def insert_history(self, filename, title, year):
        self.__cursor__  = self.db.cursor()
        sql = """
        INSERT INTO history (file, event_title, year) 
        values (%s, %s, %s);
        """
        self.__cursor__.execute(sql, (filename, title, year))
        return 

    def get_history(self):
        self.__cursor__  = self.db.cursor()
        query = f"""
        SELECT file, year, event_title FROM history
        ORDER BY year;
        """
        self.__cursor__.execute(query)
        result = self.__cursor__.fetchall()
        self.__cursor__.close()
        return result

    def update_chair(self, 
                    student_num,
                    student_name,
                    graduate_num,
                    graduate_name):
        self.__cursor__  = self.db.cursor()         
        query = """
        UPDATE user SET position='chair' 
        WHERE number=%s AND name=%s ;
        """
        self.__cursor__.execute(query, (int(student_num), student_name))
        self.__cursor__.execute(query, (int(graduate_num), graduate_name))
        self.__cursor__.close()
        return