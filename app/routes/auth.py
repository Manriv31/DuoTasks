from flask import Blueprint, render_template, request, redirect, url_for, session
from ..supabase_client import supabase

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        res = supabase.auth.sign_up({"email": email, "password": password})
        if res.user:
            return redirect(url_for("auth.login"))
    return render_template("register.html")

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        res = supabase.auth.sign_up({"email": email, "password": password})
        if res.user:
            session["user"] = res.user.id
            return redirect(url_for("home.index"))
    return render_template("login.html")

@auth_bp.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("auth.login"))
