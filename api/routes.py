from os import getenv

from flask import redirect, render_template, request, session, flash

from api.app import app
from api.services.exhibition_service import create_new_exhibition, get_exhibitions, get_museums
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
        return render_template("login.html", response_message=new_user[1])
    return render_template("sign_up.html", response_message=new_user[1])


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
            session["username"] = username
            return redirect("/")
        return render_template("login.html", response_message=user_session[1])
    return render_template("login.html", response_message="Please log in.")


@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")


@app.route("/", methods=["GET", "POST"])
def index():
    all_exhibitions = get_exhibitions()
    username = session.get("username")
    return render_template(
        "index.html", all_exhibitions=all_exhibitions, username=username
    )


@app.route("/add_exhibition", methods=["GET"])
def add_exhibition():
    museum_names = get_museums()
    return render_template(
    "add_exhibition.html",museum_names=museum_names)


@app.route("/create_exhibition", methods=["POST"])
def create_exhibition():
    required_fields = ['exhibition_name', 'museum_name', 'start_date', 'end_date']
    missing_fields = []

    for field in required_fields:
        if not request.form.get(field, '').strip():
            missing_fields.append(field.replace("_", " ").capitalize())
    if missing_fields:
        flash(f'Please fill in: {", ".join(missing_fields)}')
        return redirect("/add_exhibition")

    new_exhibition = create_new_exhibition(
        exhibition_name=request.form["exhibition_name"],
        museum_name=request.form["museum_name"],
        start_date=request.form["start_date"],
        end_date=request.form["end_date"],
    )
    if new_exhibition[0]:
        flash(new_exhibition[1])
        return redirect("/")
    flash(new_exhibition[1])
    return redirect("/add_exhibition")


