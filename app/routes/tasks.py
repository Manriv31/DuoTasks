from flask import Blueprint, request, redirect, url_for, session
from ..supabase_client import supabase

tasks_bp = Blueprint("tasks", __name__)

@tasks_bp.route("/add_task", methods=["POST"])
def add_task():
    if "user" not in session:
        return redirect(url_for("auth.login"))
    description = request.form["description"]
    user_id = session["user"]
    supabase.table("tasks").insert({"user_id": user_id, "description": description, "done": False}).execute()
    return redirect(url_for("home.index"))

@tasks_bp.route("/complete_task/<int:task_id>", methods=["POST"])
def complete_task(task_id):
    if "user" not in session:
        return redirect(url_for("auth.login"))
    supabase.table("tasks").update({"done": True}).eq("id", task_id).execute()
    return redirect(url_for("home.index"))

@tasks_bp.route("/delete_task/<int:task_id>", methods=["POST"])
def delete_task(task_id):
    if "user" not in session:
        return redirect(url_for("auth.login"))
    supabase.table("tasks").delete().eq("id", task_id).execute()
    return redirect(url_for("home.index"))
    
@tasks_bp.route("/reopen_task/<int:task_id>", methods=["POST"])
def reopen_task(task_id):
    if "user" not in session:
        return redirect(url_for("auth.login"))
    supabase.table("tasks").update({"done": False}).eq("id", task_id).execute()
    return redirect(url_for("home.index"))
