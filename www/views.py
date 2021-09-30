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
    return render_template("index.html")

@views.route("/manager", methods=["GET"])
def manager():
    print("Manager Page")
    return render_template("manager.html")

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
        return render_template("manager.html")
    # login failed
    else:
        msg = "비밀번호 틀렸습니다.\n비밀번호는 회장에게 물어보세요."        
        return render_template("login.html", msg=msg)

@views.route("/intro", methods=["GET"])
def intro():
    print("Intro Page")
    sql = Sql(__db__)
    poster, chairman_num, intro_text = sql.get_site()
    
    name = sql.get_username(chairman_num)
    profile = sql.get_userpic(chairman_num)

    return render_template("intro.html",
                            profile=profile, 
                            chairman=" ".join(name), 
                            intro_text=intro_text)
