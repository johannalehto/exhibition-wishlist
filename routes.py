from app import app

from flask import redirect, render_template, request

from services import exhibition_service


@app.route("/", methods=["GET", "POST"])
def index():
    all_exhibitions = exhibition_service.get_exhibitions()
    return render_template("index.html", all_exhibitions=all_exhibitions)


@app.route("/add_exhibition", methods=["GET"])
def add_exhibition():
    return render_template("add_exhibition.html")


@app.route("/create_exhibition", methods=["POST"])
def create_exhibition():
    exhibition_service.create_new_exhibition(
        exhibition_name=request.form["exhibition_name"],
        museum_name=request.form["museum_name"],
        start_date=request.form["start_date"],
        end_date=request.form["end_date"]
    )
    return redirect("/")


@app.route("/exhibitions", methods=["POST"])
def exhibitions():
    return render_template("exhibitions.html")
