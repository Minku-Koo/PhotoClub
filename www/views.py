from flask import Flask, request, render_template, jsonify, Blueprint, redirect, url_for, session, current_app
import os, pymysql
import utils.db_info as info
from utils.db import Sql

views = Blueprint("server", __name__)

__db__ = pymysql.connect(
                db = info.db_name,
                host = info.host,
                user = info.user,
                passwd = info.pwd ,
                charset = info.charset 
            )

@views.route("/", methods=["GET"])
def index():
    print("CJU Photo Club Flask Server")
    session["admin"] = False
    return render_template("index.html")

@views.route("/intro_piece", methods=["GET"])
def intro_piece():
    sql = Sql(__db__)
    piece_list_student, piece_list_freshman, piece_list_clubman = sql.get_user_photo_info()
    # poster, intro_text, student, graduated = sql.get_last('photo')
    
    # #추후에 user에서 회장 찾아서 입력
    # name = sql.get_username(1)
    # profile = sql.get_userpic(1)

    # print(f"name : {name}")
    # print(f"profile : {profile}")
    '''
    piece_list_student = [
        {"artist" : "42th 일지우", "image" : "logo.jpg"},
        {"artist" : "41th 이지우", "image" : "logo.jpg"},
        {"artist" : "41th 삼지우", "image" : "logo.jpg"},
        {"artist" : "42th 사지우", "image" : "logo.jpg"},
        {"artist" : "41th 오지우", "image" : "logo.jpg"},
        {"artist" : "41th 조민혁", "image" : "logo.jpg"},
        {"artist" : "42th 이지우", "image" : "logo.jpg"},
        {"artist" : "41th 조민혁", "image" : "logo.jpg"},
        {"artist" : "41th 조민혁", "image" : "logo.jpg"},
        {"artist" : "41th 조민혁", "image" : "logo.jpg"},
        {"artist" : "41th 조민혁", "image" : "logo.jpg"},
        {"artist" : "41th 조민혁", "image" : "logo.jpg"},
        {"artist" : "41th 끝지우", "image" : "logo.jpg"}
    ]

    piece_list_freshman = [
        {"artist" : "43th 새내기", "image" : "logo.jpg"},
        {"artist" : "43th 새내기", "image" : "logo.jpg"},
        {"artist" : "43th 새내기", "image" : "logo.jpg"},
        {"artist" : "43th 새내기", "image" : "logo.jpg"},
        {"artist" : "43th 새내기", "image" : "logo.jpg"},
        {"artist" : "43th 새내기", "image" : "logo.jpg"}
    ]

    piece_list_clubman = [
        {"artist" : "1th 일동호", "image" : "logo.jpg"},
        {"artist" : "2th 이동호", "image" : "logo.jpg"},
        {"artist" : "3th 삼동호", "image" : "logo.jpg"},
        {"artist" : "10th 십동호", "image" : "logo.jpg"}
    ]
    '''

    return render_template(
        "intro_piece.html",
        piece_list_student = piece_list_student,
        piece_list_freshman = piece_list_freshman,
        piece_list_clubman = piece_list_clubman
    )

@views.route("/intro_club", methods=["GET"])
def intro_club():
    sql = Sql(__db__)
    chairs = sql.get_chairs()

    chairman_info = "재학생 회장"
    chairman_name = chairs["student"][0]
    chairman_photo = sql.get_userpic(chairs["student"][0], chairs["student"][2])

    club_chairman_info = "동호인 회장"
    club_chairman_name = chairs["club_member"][0]
    club_chairman_photo = "logo.png"

    _, club_intro_txt, chairman_txt, club_chairman_txt = sql.get_site()
    print("_, club_intro_txt, chairman_txt, club_chairman_txt")
    print(_, club_intro_txt, chairman_txt, club_chairman_txt)

    return render_template(
        "intro_club.html",
        club_intro_txt = club_intro_txt,
        chairman_txt = chairman_txt,
        club_chairman_txt = club_chairman_txt,
        chairman_info = chairman_info,
        chairman_name = chairman_name,
        chairman_photo = chairman_photo,
        club_chairman_info = club_chairman_info,
        club_chairman_name = club_chairman_name,
        club_chairman_photo = club_chairman_photo
    )


@views.route("/intro_member", methods=["GET"])
def intro_member():
    sql = Sql(__db__)
    chairs = sql.get_chairs()
    other_users = sql.get_other_users()


    student_chairman = {
                        "profile" : " ".join([chairs["student"][1],
                                        str(chairs["student"][2]),
                                        chairs["student"][0]]), 
                        "image" : sql.get_userpic(chairs["student"][0], chairs["student"][2])
                        }
    student_list = [
        {
            "profile" : " ".join([user[1],
                            str(user[2]),
                            user[0]]), 
            "image" : sql.get_userpic(user[0], user[2])
        }
        for user in other_users["student"]
    ]
    #print(f'other_users["club_member"] : {other_users["club_member"]}')

    club_chairman = {"profile" : " ".join([str(chairs["club_member"][1]),
                                        chairs["club_member"][0]]), 
                        "image" : "logo.jpg"}
    clubmember_list = [
        {
            "profile" : " ".join([str(user[1]), user[0]])
        }
        for user in other_users["club_member"]
    ]

    return render_template(
        "intro_member.html",
        student_chairman = student_chairman,
        club_chairman = club_chairman,
        student_list = student_list,
        clubmember_list = clubmember_list
    )

@views.route("/club_history", methods=["GET"])
def club_history():
    sql = Sql(__db__)
    history = sql.get_history()
    club_history_list = [
        {"년도 미상":[]},
        {"90년대 이전":[]},
        {"1990년대":[]},
        {"2000년대":[]},
        {"2010년대":[]},
        {"2020년대":[]},
    ]
    for file, year, title in history:
        if year == 0:
            club_history_list[0]["년도 미상"].append(file)
        elif year <1990:
            club_history_list[1]["90년대 이전"].append(file)
        elif year <2000:
            club_history_list[2]["1990년대"].append(file)
        elif year <2010:
            club_history_list[3]["2000년대"].append(file)
        elif year <2020:
            club_history_list[4]["2010년대"].append(file)
        elif year <2030:
            club_history_list[5]["2020년대"].append(file)
        else:
            pass
    print(club_history_list)
    '''
    club_history_list = [
        {"2021년도" : [
            "logo.jpg",
            "logo.jpg",
            "logo.jpg",
            "logo.jpg",
            "logo.jpg",
            "logo.jpg",
            "logo.jpg",
            "logo.jpg",
            "logo.jpg",
            "logo.jpg",
            "logo.jpg",
            "logo.jpg",
            "logo.jpg",
            "logo.jpg"
            ]
        },
        {"77년도 ~ 00년도" : [
            "logo.jpg",
            "logo.jpg",
            "logo.jpg",
            "logo.jpg",
            "logo.jpg",
            "logo.jpg",
            "logo.jpg",
            "logo.jpg",
            "logo.jpg",
            "logo.jpg",
            "logo.jpg",
            "logo.jpg",
            "logo.jpg",
            "logo.jpg",
            "logo.jpg",
            "logo.jpg",
            "logo.jpg",
            "logo.jpg"
            ]
        },
        {"00년도 ~ 10년도" : [
            "logo.jpg",
            "logo.jpg",
            "logo.jpg",
            "logo.jpg",
            "logo.jpg",
            "logo.jpg",
            "logo.jpg",
            "logo.jpg",
            "logo.jpg",
            "logo.jpg"
            ]
        },
        {"10년도 ~ 20년도" : [
            "logo.jpg",
            "logo.jpg",
            "logo.jpg",
            "logo.jpg",
            "logo.jpg",
            "logo.jpg",
            "logo.jpg",
            "logo.jpg",
            "logo.jpg",
            "logo.jpg"
            ]
        }
    ]
    ''' 
    return render_template(
        "club_history.html",
        club_history_list = club_history_list
    )


@views.route("/faq", methods=["GET"])
def faq():
    sql = Sql(__db__)
    faq_db = sql.get_faq()
    faq_list = []
    for q, a in faq_db:
        faq_list.append( {"q":q, "a":a} )
    '''
    faq_list = [
        {"q" : "조민혁이 누구인가요?", "a" : "회장입니다."},
        {"q" : "회비는 언제 내나요? 방학에도 내나요???", "a" : "방학을 제외한 학기 중에 월 1일마다 냅니다."},
        {"q" : "회비는 언제 내나요? 방학에도 내나요???", "a" : "방학을 제외한 학기 중에 월 1일마다 냅니다."},
        {"q" : "회비는 언제 내나요? 방학에도 내나요???", "a" : "방학을 제외한 학기 중에 월 1일마다 냅니다."},
        {"q" : "회비는 언제 내나요? 방학에도 내나요???", "a" : "방학을 제외한 학기 중에 월 1일마다 냅니다."}
    ]
    '''
    # print(faq_list)
    return render_template(
        "faq.html",
        faq_list = faq_list
    )


@views.route("/brief_history", methods=["GET"])
def brief_history():
    sql = Sql(__db__)
    history_list = [
        {"2020년대":[]},
        {"2010년대":[]},
        {"2000년대":[]},
        {"1990년대":[]},
        {"90년대 이전":[]},
    ]

    for title, year in sql.get_club_event():
        content = " ".join([str(year), title])
        if year <1990:
            history_list[4]["90년대 이전"].append(content)
        elif year <2000:
            history_list[3]["1990년대"].append(content)
        elif year <2010:
            history_list[2]["2000년대"].append(content)
        elif year <2020:
            history_list[1]["2010년대"].append(content)
        elif year <2030:
            history_list[0]["2020년대"].append(content)
        else:
            pass
    '''
    history_list = [
        {"1970년대" : [
            "1977 사진예술연구회 창립 / 초대 지도교수",
            "1978 제 1회 사진전시회 / 하계워크샵 (설악산)",
            "1979 제 2회 사진전시회 / 하계워크샵 (안면도) / 동계워크샵"
            ]
        },
        {"1980년대" : [
            "1980 제 3회 사진전시화 / 하계워크샵 (소백산)",
            "1981 제 4회 사진전시회 / 2대 지도교수 김두영교수님 / 하계워크샵 (남해안 일대)",
            "1982 제 5회 사진전시회 / 3대 지도교수 정상진교수님 / 하계워크샵 (제주도)"
            ]
        }
    ]
    '''
    return render_template(
        "brief_history.html",
        history_list = history_list
    )






@views.route("/manager", methods=["GET"])
def manager():
    print("Manager Page")
    if session["admin"] :
        print("session[admin]", session["admin"])
        return render_template("manager.html")
    else:
        msg = "올바르지 못한 접근입니다."        
        print("올바르지 못한 접근입니다.")
        return render_template("login.html", msg=msg)

@views.route("/login", methods=["GET"])
def login():
    print("Login Page")
    return render_template("login.html", msg="")

@views.route("/check", methods=["POST"])
def check():
    print("Check Page")
    input_pw = request.form['input_pw_value']
    manager_pw = info.manager_password
    # login success
    if input_pw == manager_pw:
        session["admin"] = True
        print(session["admin"])
        return render_template("manager.html")
    elif input_pw != manager_pw :
        msg = "비밀번호 틀렸습니다.\n비밀번호는 회장에게 물어보세요."        
        print("비번 틀렷어요")
        return render_template("login.html", msg=msg)
    # login failed
    elif not session["admin"] :
        msg = "올바르지 못한 접근입니다."        
        print("올바르지 못한 접근입니다.")
        return render_template("login.html", msg=msg)

    return render_template("login.html", msg="")


@views.route("/setuser", methods=["GET"])
def setuser():
    print("setuser page")
    if not session["admin"] :
        msg = "올바르지 못한 접근입니다."    
        print("올바르지 못한 접근입니다.")
        return render_template("login.html", msg=msg)
    return render_template("set_user.html")

@views.route("/setsite", methods=["GET"])
def setsite():
    print("setsite page")
    if not session["admin"] :
        msg = "올바르지 못한 접근입니다."    
        print("올바르지 못한 접근입니다.")
        return render_template("login.html", msg=msg)
    
    sql = Sql(__db__)
    site = sql.get_last("site")
    history = sql.get_all("history")
    events =  sql.get_all("club_event")
    faq_list = sql.get_all("faq")
    return render_template("set_site.html", 
                            history=history,
                            site  = site[1:],
                            events=events,
                            faq_list = faq_list)