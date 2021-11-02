
import os
import db
import db_info as info

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
        if sql.check_user_exist(number, name):
            sql.update_user(number, major, name, profile)
            continue

        sql.insert_user(name, 
                    major, 
                    number, 
                    profile, 
                    "", 
                    0)
    return

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

