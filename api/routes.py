from os import getenv

from flask import flash, redirect, render_template, request, session, url_for

from api.app import app
from api.services.exhibition_service import (add_user_to_exhibition,
                                             check_missing_fields,
                                             create_new_exhibition,
                                             get_days_left, get_exhibitions,
                                             get_museums,
                                             remove_user_from_exhibition)
from api.services.user_service import create_new_user, create_user_session

app.secret_key = getenv("SECRET_KEY")


@app.route("/sign_up_page", methods=["GET"])
def sign_up_page():
    return render_template("sign_up.html")


@app.route("/create_user", methods=["GET", "POST"])
def create_user():
    new_user = create_new_user(
        username=request.form["username"],
        password_first=request.form["password_first"],
        password_second=request.form["password_second"],
        first_name=request.form["first_name"],
    )
    if new_user[0]:
        flash("User created successfully")
        return redirect(url_for("login_page"))
    else:
        flash(new_user[1])
        return redirect(url_for("sign_up_page"))


@app.route("/login_page", methods=["GET"])
def login_page():
    return render_template("login.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user_session = create_user_session(username, password)
        if user_session[0]:
            session["user_id"] = user_session[1]["id"]
            session["username"] = username
            return redirect(url_for("index"))
        flash(user_session[1])
        return redirect(url_for("login_page"))
    return redirect(url_for("login_page"))


@app.route("/logout")
def logout():
    del session["username"]
    flash("You have been logged out")
    return redirect(url_for("login_page"))


@app.route("/", methods=["GET", "POST"])
def index():
    all_exhibitions = get_exhibitions()

    username = session.get("username")
    user_id = session.get("user_id")

    for exhibition in all_exhibitions:
        exhibition["is_attending"] = any(
            user_id == attendee[0] for attendee in exhibition["attendees"]
        )
    return render_template(
        "index.html", all_exhibitions=all_exhibitions, username=username
    )


@app.route("/add_exhibition", methods=["GET"])
def add_exhibition():
    museum_names = get_museums()
    return render_template("add_exhibition.html", museum_names=museum_names)


@app.route("/create_exhibition", methods=["POST"])
def create_exhibition():
    if check_missing_fields():
        return redirect("/add_exhibition")
    new_exhibition = create_new_exhibition(
        exhibition_name=request.form["exhibition_name"],
        museum_name=request.form["museum_name"],
        start_date=request.form["start_date"],
        end_date=request.form["end_date"],
    )
    if new_exhibition[0]:
        flash(new_exhibition[1])
        return redirect(url_for("index"))
    flash(new_exhibition[1])
    return redirect(url_for("add_exhibition"))


@app.route("/join_exhibition/<int:exhibition_id>", methods=["POST"])
def join_exhibition(exhibition_id):
    user_id = session.get("user_id")
    if user_id and exhibition_id:
        add_user_to_exhibition(user_id, exhibition_id)
    return redirect(url_for("index"))


@app.route("/leave_exhibition/<int:exhibition_id>", methods=["POST"])
def leave_exhibition(exhibition_id):
    user_id = session.get("user_id")
    if user_id and exhibition_id:
        remove_user_from_exhibition(user_id, exhibition_id)
    return redirect(url_for("index"))
