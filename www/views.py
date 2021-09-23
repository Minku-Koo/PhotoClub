from flask import Flask, request, render_template, jsonify, Blueprint, redirect, url_for, session, current_app
import os

views = Blueprint("server", __name__)

@views.route("/", methods=["GET"])
def index():
    print("CJU Photo Club Flask Server")
    return render_template("index.html")