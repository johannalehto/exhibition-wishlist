from os import getenv

from flask import Flask, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
db = SQLAlchemy(app)


@app.route("/", methods=["GET", "POST"])
def index():
    sql = text(
        """
        SELECT e.exhibition_name, e.start_date, e.end_date, m.museum_name
        FROM exhibitions e
        JOIN museums m ON e.museum_id = m.id
    """
    )
    result = db.session.execute(sql)
    all_exhibitions = result.fetchall()
    return render_template("index.html", all_exhibitions=all_exhibitions)


def handle_museum(museum_name: str) -> int:
    sql = text("SELECT id FROM museums WHERE museum_name = :museum_name")
    result = db.session.execute(sql, {"museum_name": museum_name})
    existing_museum_id = result.fetchone()

    if existing_museum_id:
        return existing_museum_id[0]
    else:
        sql = text(
            "INSERT INTO museums (museum_name) VALUES (:museum_name) RETURNING id"
        )
        result = db.session.execute(sql, {"museum_name": museum_name})
        new_museum_id = result.fetchone()
        db.session.commit()
        return new_museum_id[0]


@app.route("/add_exhibition", methods=["GET"])
def add_exhibition():
    return render_template("add_exhibition.html")


@app.route("/create_exhibition", methods=["POST"])
def create_exhibition():
    exhibition_name = request.form["exhibition_name"]
    museum_name = request.form["museum_name"]
    start_date = request.form["start_date"]
    end_date = request.form["end_date"]

    museum_id = handle_museum(museum_name)

    new_exhibition = {
        "exhibition_name": exhibition_name,
        "museum_id": museum_id,
        "start_date": start_date,
        "end_date": end_date,
    }
    sql = text(
        """
        INSERT INTO exhibitions (exhibition_name, museum_id, start_date, end_date)
        VALUES (:exhibition_name, :museum_id, :start_date, :end_date)
    """
    )
    try:
        db.session.execute(sql, new_exhibition)
        db.session.commit()
    except Exception as e:
        print("&&&& Error is this:", e)
        print("&&&& new_exhibition values are these:", new_exhibition)
    return redirect("/")


@app.route("/exhibitions", methods=["POST"])
def exhibitions():
    return render_template("exhibitions.html")
