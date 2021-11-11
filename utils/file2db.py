
import os
import db
import db_info as info

# 부원-동호인
def member_to_db(
    db_,
    path='./www/static/sample_data/', 
    filename='sample_members.csv'):
    sql = db.Sql(db_)
    # 파일 존재하면
    if os.path.exists(path + filename):
        with open(path + filename, "rt", encoding="utf-8") as f:
            for line in f.readlines():
                names = []
                for col in line.split(","):
                    if not col:
                        break
                    names.append(col)
                
                num = int(names.pop(0)[:-1])
                
                for name in sorted(names):
                    
                    sql.insert_user( name, "", num, "", "", 1)
                    # ('%s', '%s', %d, '%s', '%s' , %d)
    return

def set_chair(
    db_,
    path='./www/static/sample_data/', 
    filename='chairman.txt'):
    sql = db.Sql(db_)
    # 파일 존재하면
    if os.path.exists(path + filename):
        with open(path + filename, "rt", encoding="utf-8") as f:
            content = f.read()
            student, graduate = content.split("\n")
        sql.update_chair(student[:2], student[2:], 
                        graduate[:2], graduate[2:])
    return

# 연혁
def club_event_to_db(
    db_,
    path='./www/static/sample_data/', 
    filename='sample_club_event.csv'):
    sql = db.Sql(db_)
    # 파일 존재하면
    if os.path.exists(path + filename):
        with open(path + filename, "rt", encoding="utf-8") as f:
            for line in f.readlines():
                year, title = line.split(",")[0], "".join(line.split(",")[1:])
                title.replace('"', "")

                sql.insert_club_event(title, year)
        
    return

# 부원-프로필 사진
def profile_to_db(
    db_,
    path='./www/static/img/members/'):
    sql = db.Sql(db_)
    for filename in os.listdir(path):
        profile = filename
        if filename.count("_")!=2: 
            continue
        extensions = [".jpg", ".jpeg", ".png"]
        for ext in extensions:
            filename = filename.lower().replace(ext, "")
        
        number, major, name = filename.split("_")
        # print(profile)
        # if sql.check_user_exist(number, name):
        #     sql.update_user(number, major, name, profile)
        #     continue

        sql.insert_user(name, 
                    major, 
                    number, 
                    profile, 
                    "", 
                    0)
    return

# 작품
def photo_to_db(
    db_,
    path='./www/static/img/pieces/'):
    sql = db.Sql(db_)
    for filename in os.listdir(path):
        photoname = filename
        if filename.count("_")!=2: 
            continue
        extensions = [".jpg", ".jpeg", ".png"]
        for ext in extensions:
            filename = filename.lower().replace(ext, "")
        number, name, _ = filename.split("_")
        user_id = sql.get_user_id(number, name)
        sql.insert_photo(user_id, photoname, title="", loc="")

    return 

# faq
def faq_to_db(
    db_,
    path='./www/static/sample_data/',
    filename='faq.txt'):
    sql = db.Sql(db_)
    # 파일 존재하면
    if os.path.exists(path + filename):
         with open(path + filename, "rt", encoding="utf-8") as f:
            for line in f.readlines():
                # print("faq",line)
                if not line: 
                    continue
                if line[0]=="Q":
                    question = line[2:].strip(" ").strip()
                else: #A
                    answer = line[2:].strip(" ").strip()
                    sql.faq_insert(question, answer)
    return

# 동아리 역사
def history_to_db(
    db_,
    path='./www/static/img/history/'):
    sql = db.Sql(db_)
    for filename in os.listdir(path):
        history_file = filename
        if filename.count("_")!=2: 
            continue
        extensions = [".jpg", ".jpeg", ".png"]
        for ext in extensions:
            filename = filename.lower().replace(ext, "")
        year, title, no = filename.split("_")
        sql.insert_history(history_file, title, year)
    return

def intro_to_db(
    db_,
    path='./www/static/sample_data/',
    filenames=["student_intro", "graduate_intro", "club_intro"]):
    sql = db.Sql(db_)
    
    for filename in filenames:
        poster, intro, student, graduate = sql.get_site()
        if os.path.exists(path + filename+".txt"):
            with open(path + filename+".txt", "rt", encoding="utf-8") as f:
                
                # update_site(self, poster, intro, student_intro, grad_intro)
                if "student" in filename:
                    sql.update_site(poster, intro, f.read(), graduate)
                if "graduate" in filename:
                    sql.update_site(poster, intro, student, f.read())
                if "club_" in filename:
                    sql.update_site(poster, f.read(), student, graduate)
    return