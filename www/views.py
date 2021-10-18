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
    # sql = Sql(__db__)
    # poster, intro_text, student, graduated = sql.get_last('photo')
    
    # #추후에 user에서 회장 찾아서 입력
    # name = sql.get_username(1)
    # profile = sql.get_userpic(1)

    # print(f"name : {name}")
    # print(f"profile : {profile}")

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

    return render_template(
        "intro_piece.html",
        piece_list_student = piece_list_student,
        piece_list_freshman = piece_list_freshman,
        piece_list_clubman = piece_list_clubman
    )

@views.route("/intro_club", methods=["GET"])
def intro_club():
    chairman_info = "41st 회장"
    chairman_name = "조민혁"

    club_chairman_info = "동호인 회장"
    club_chairman_name = "박은규"

    club_intro_txt = """개강이라는 첫 설렘으로 만나 어느덧 첫 눈이 내리는 겨울이 되었습니다.
새로운 사람들을 만나, 전국 각지로 사진을 찍으며 추억을 쌓다 보니
어느 새 일년이 지나 전시회를 개최하게 되었습니다.
지난 44회 전시회 때, 임원진으로 참여하여 전시회를 준비하였는데,
이번 행사에는 회장으로서 전시회를 준비하니 감회가 깊습니다.

사진예술연구회는 청주대학ㅇ교ㅑㅈㄷ노ㅑ뢰너ㅠㅓ리ㅏㄴ어ㅏㅗㅓㅏ우ㅏ린
ㅇ아럼누ㅏㅣㅇ너ㅣㄷ러ㅏ너독발노ㅓㅏㅣㅇㅈ눠ㅏㅣㅇ;ㄴㅊ,ㅠㅡ치ㅡㅋ.,ㅟ
퉈ㅜㅏ ㅋ/,ㅏㅓㅣㅣㅏㅇㄴ츠,ㅜ라치ㅡㅜ.,"""

    chairman_txt = """애들이 제 말 안들어요 ㅠㅠ
엉ㅇ어엉융아이ㅓ어ㅕ영ㅇ우유히
원유ㅠ아ㅓㅏㅗ놓ㅎㄴ짜증ㅇ나아 융
ㅇ내ㅓㅐㅑㅑㄹ ㅓㅣㅏㄹ옹ㄶㅎ바보
 멍청ㅎ이 조민혁 메롱 이건 내맘이다"""

    club_chairman_txt = """애들이 제 말 안들어요 ㅠㅠ
엉ㅇ어엉융아이ㅓ어ㅕ영ㅇ우유히
원유ㅠ아ㅓㅏㅗ놓ㅎㄴ짜증ㅇ나아 융
ㅇ내ㅓㅐㅑㅑㄹ ㅓㅣㅏㄹ옹ㄶㅎ바보
멍청ㅎ이 조민혁 메롱 이건 내맘이다"""

    return render_template(
        "intro_club.html",
        club_intro_txt = club_intro_txt,
        chairman_txt = chairman_txt,
        club_chairman_txt = club_chairman_txt,
        chairman_info = chairman_info,
        chairman_name = chairman_name,
        club_chairman_info = club_chairman_info,
        club_chairman_name = club_chairman_name
    )


@views.route("/intro_member", methods=["GET"])
def intro_member():
    chairman_info = "41st 회장"
    chairman_name = "조민혁"

    club_chairman_info = "동호인 회장"
    club_chairman_name = "박은규"

    club_intro_txt = """개강이라는 첫 설렘으로 만나 어느덧 첫 눈이 내리는 겨울이 되었습니다.
새로운 사람들을 만나, 전국 각지로 사진을 찍으며 추억을 쌓다 보니
어느 새 일년이 지나 전시회를 개최하게 되었습니다.
지난 44회 전시회 때, 임원진으로 참여하여 전시회를 준비하였는데,
이번 행사에는 회장으로서 전시회를 준비하니 감회가 깊습니다.

사진예술연구회는 청주대학ㅇ교ㅑㅈㄷ노ㅑ뢰너ㅠㅓ리ㅏㄴ어ㅏㅗㅓㅏ우ㅏ린
ㅇ아럼누ㅏㅣㅇ너ㅣㄷ러ㅏ너독발노ㅓㅏㅣㅇㅈ눠ㅏㅣㅇ;ㄴㅊ,ㅠㅡ치ㅡㅋ.,ㅟ
퉈ㅜㅏ ㅋ/,ㅏㅓㅣㅣㅏㅇㄴ츠,ㅜ라치ㅡㅜ.,"""

    chairman_txt = """애들이 제 말 안들어요 ㅠㅠ
엉ㅇ어엉융아이ㅓ어ㅕ영ㅇ우유히
원유ㅠ아ㅓㅏㅗ놓ㅎㄴ짜증ㅇ나아 융
ㅇ내ㅓㅐㅑㅑㄹ ㅓㅣㅏㄹ옹ㄶㅎ바보
 멍청ㅎ이 조민혁 메롱 이건 내맘이다"""

    club_chairman_txt = """애들이 제 말 안들어요 ㅠㅠ
엉ㅇ어엉융아이ㅓ어ㅕ영ㅇ우유히
원유ㅠ아ㅓㅏㅗ놓ㅎㄴ짜증ㅇ나아 융
ㅇ내ㅓㅐㅑㅑㄹ ㅓㅣㅏㄹ옹ㄶㅎ바보
멍청ㅎ이 조민혁 메롱 이건 내맘이다"""

    return render_template(
        "intro_member.html",
        club_intro_txt = club_intro_txt,
        chairman_txt = chairman_txt,
        club_chairman_txt = club_chairman_txt,
        chairman_info = chairman_info,
        chairman_name = chairman_name,
        club_chairman_info = club_chairman_info,
        club_chairman_name = club_chairman_name
    )

@views.route("/club_history", methods=["GET"])
def club_history():

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

    return render_template(
        "club_history.html",
        piece_list_student = piece_list_student,
        piece_list_freshman = piece_list_freshman,
        piece_list_clubman = piece_list_clubman
    )


@views.route("/faq", methods=["GET"])
def faq():
    faq_list = [
        {"q" : "조민혁이 누구인가요?", "a" : "회장입니다."},
        {"q" : "회비는 언제 내나요? 방학에도 내나요???", "a" : "방학을 제외한 학기 중에 월 1일마다 냅니다."},
        {"q" : "회비는 언제 내나요? 방학에도 내나요???", "a" : "방학을 제외한 학기 중에 월 1일마다 냅니다."},
        {"q" : "회비는 언제 내나요? 방학에도 내나요???", "a" : "방학을 제외한 학기 중에 월 1일마다 냅니다."},
        {"q" : "회비는 언제 내나요? 방학에도 내나요???", "a" : "방학을 제외한 학기 중에 월 1일마다 냅니다."}
    ]

    return render_template(
        "faq.html",
        faq_list = faq_list
    )


@views.route("/brief_history", methods=["GET"])
def brief_history():
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