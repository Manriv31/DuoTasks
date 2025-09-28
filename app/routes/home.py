from flask import Blueprint, render_template, request, redirect, url_for, session
from ..supabase_client import supabase

home_bp = Blueprint("home", __name__)

@home_bp.route("/")
def index():
    if "user" not in session:
        return redirect(url_for("auth.login"))
    user_id = session["user"]
    tasks = supabase.table("tasks").select("*").eq("user_id", user_id).eq("done", False).order("created_at", desc=False).execute().data
    completed_tasks = supabase.table("tasks").select("*").eq("user_id", user_id).eq("done", True).order("created_at", desc=False).execute().data
    return render_template("index.html", tasks=tasks, completed_tasks=completed_tasks)
