import secrets
from os import getenv

from flask import flash, redirect, render_template, request, session, url_for

from api.app import app
from api.services.common_service import check_missing_fields
from api.services.exhibition_service import (add_user_to_exhibition,
                                             create_new_exhibition,
                                             get_current_exhibitions,
                                             get_museums, get_past_exhibitions,
                                             remove_user_from_exhibition, is_user_attending,
                                             get_current_exhibitions_by_group, get_past_exhibitions_by_group)
from api.services.group_service import create_new_group, get_all_groups_by_user, \
    remove_user_from_group, add_user_to_group, get_groups_without_user, get_selected_group, get_groups_by_user_id
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
            session["csrf_token"] = secrets.token_hex(16)
            return redirect(url_for("index"))
        flash(user_session[1])
        return redirect(url_for("login_page"))
    return redirect(url_for("login_page"))


@app.route("/logout")
def logout():
    del session["username"]
    flash("You have been logged out")
    return redirect(url_for("login_page"))


@app.route("/", methods=["GET"])
def index():
    if 'username' in session:
        return redirect(url_for('display_exhibitions'))
    return render_template('index.html')

@app.route('/display_exhibitions', methods=["GET", "POST"])
def display_exhibitions():
    username = session.get('username')
    user_id = session.get("user_id")
    if not username:
        flash("Please login to view exhibitions.")
        return redirect(url_for('login'))

    all_groups_by_user = get_all_groups_by_user(user_id)
    selected_group_id = request.args.get('group_id')

    if not selected_group_id and all_groups_by_user:
        selected_group_id = all_groups_by_user[0]["id"]

    current_exhibitions = []
    past_exhibitions = []
    if selected_group_id:
        selected_group_id = int(selected_group_id)
        current_exhibitions = get_current_exhibitions_by_group(selected_group_id)
        past_exhibitions = get_past_exhibitions_by_group(selected_group_id)

    for exhibition in current_exhibitions:
        exhibition["is_attending"] = is_user_attending(user_id, exhibition["attendees"])

    return render_template(
        'exhibitions.html',
        groups=all_groups_by_user,
        current_exhibitions=current_exhibitions,
        past_exhibitions=past_exhibitions,
        selected_group_id=selected_group_id,
        username=username)


@app.route("/add_exhibition", methods=["GET"])
def add_exhibition():
    user_id = session.get("user_id")
    museum_names = get_museums()
    groups = get_groups_by_user_id(user_id)
    return render_template(
        "add_exhibition.html",
        museum_names=museum_names,
        groups=groups
    )


@app.route("/create_exhibition", methods=["POST"])
def create_exhibition():
    # TODO: create a separate method for csrf
    if session["csrf_token"] != request.form["csrf_token"]:
        flash("Something went wrong, please try again.")
        return redirect(url_for("index"))

    required_fields = [
        "exhibition_name",
        "museum_name",
        "start_date",
        "end_date",
        "group_id"
    ]
    if check_missing_fields(required_fields):
        return redirect("/add_exhibition")
    new_exhibition = create_new_exhibition(
        exhibition_name=request.form["exhibition_name"],
        museum_name=request.form["museum_name"],
        start_date=request.form["start_date"],
        end_date=request.form["end_date"],
        group_id=request.form["group_id"]
    )

    if new_exhibition[0]:
        flash("Exhibition added successfully.")
        return redirect(
            url_for("display_exhibitions",
                    group_id=request.form["group_id"]))
    # TODO: check the error message here
    flash("Failed to add exhibition. Please try again.")
    return redirect(url_for("add_exhibition"))


@app.route("/join_exhibition/<int:exhibition_id>", methods=["POST"])
def join_exhibition(exhibition_id):
    user_id = session.get("user_id")
    group_id = request.form.get("group_id")
    if user_id and exhibition_id:
        add_user_to_exhibition(user_id, exhibition_id)
    return redirect(url_for("display_exhibitions", group_id=group_id))


@app.route("/leave_exhibition/<int:exhibition_id>", methods=["POST"])
def leave_exhibition(exhibition_id):
    user_id = session.get("user_id")
    group_id = request.form.get("group_id")
    if user_id and exhibition_id:
        remove_user_from_exhibition(user_id, exhibition_id)
    return redirect(url_for("display_exhibitions", group_id=group_id))


@app.route("/groups", methods=["GET", "POST"])
def groups():
    user_id = session.get("user_id")
    all_groups_by_user = get_all_groups_by_user(user_id)
    groups_without_user = get_groups_without_user(user_id)

    return render_template(
        "groups.html",
        all_groups_by_user=all_groups_by_user,
        groups_without_user=groups_without_user
    )


@app.route("/add_group", methods=["GET"])
def add_group():
    return render_template("add_group.html")

@app.route("/create_group", methods=["POST"])
def create_group():
    # TODO: create a separate method for csrf
    if session["csrf_token"] != request.form["csrf_token"]:
        flash("Something went wrong, please try again.")
        return redirect(url_for("display_exhibitions"))

    required_fields = ["group_name"]
    if check_missing_fields(required_fields):
        return redirect("/create_group")
    new_group = create_new_group(
        group_name=request.form["group_name"],
        group_description=request.form["group_description"],
    )
    if new_group[0]:
        flash(new_group[1])
        return redirect(url_for("display_exhibitions"))
    flash(new_group[1])
    return redirect(url_for("add_group"))

@app.route("/join_group/<int:group_id>", methods=["POST"])
def join_group(group_id: int):
    user_id: int = session.get("user_id")
    if user_id and group_id:
        add_user_to_group(user_id, group_id)
    return redirect(url_for("groups"))


@app.route("/leave_group/<int:group_id>", methods=["POST"])
def leave_group(group_id: int):
    user_id: int = session.get("user_id")
    if user_id and group_id:
        remove_user_from_group(user_id, group_id)
    return redirect(url_for("groups"))


