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
    # poster, intro_text, student, graduated = sql.get_last('photo')
    
    # #추후에 user에서 회장 찾아서 입력
    # name = sql.get_username(1)
    # profile = sql.get_userpic(1)

    # print(f"name : {name}")
    # print(f"profile : {profile}")

    photo_list = [
        {"42th 이지우": "logo.jpg"},
        {"41th 조민혁": "logo.jpg"},
        {"41th 조민혁": "logo.jpg"},
        {"42th 이지우": "logo.jpg"},
        {"41th 조민혁": "logo.jpg"},
        {"41th 조민혁": "logo.jpg"},
        {"42th 이지우": "logo.jpg"},
        {"41th 조민혁": "logo.jpg"},
        {"41th 조민혁": "logo.jpg"},
        {"41th 조민혁": "logo.jpg"},
        {"41th 조민혁": "logo.jpg"},
        {"41th 조민혁": "logo.jpg"},
        {"41th 조민혁": "logo.jpg"}
    ]

    return render_template("intro_piece.html",
                            photo_list=photo_list
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