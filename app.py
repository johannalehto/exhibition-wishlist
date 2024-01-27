import datetime

from flask import Flask
from flask import render_template, request
from pydantic import BaseModel

app = Flask(__name__)
class ExhibitionEntry(BaseModel):
    name: str
    museum: str
    start_date: datetime.date
    end_date: datetime.date


all_exhibitions = []


def create_exhibition_entry(
        exhibition_name: str, museum_name: str, start_date: datetime, end_date: datetime
) -> ExhibitionEntry | None:
    return ExhibitionEntry(
        name=exhibition_name if exhibition_name else None,
        museum=museum_name if museum_name else None,
        start_date=start_date if start_date else None,
        end_date=end_date if end_date else None
    )

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        exhibition_entry = create_exhibition_entry(
            exhibition_name=str(request.form["exhibition_name"]),
            museum_name=str(request.form["museum_name"]),
            start_date=request.form["start_date"],
            end_date=request.form["end_date"]
        )
        all_exhibitions.append(exhibition_entry)
    return render_template(
        "index.html",
        all_exhibitions=all_exhibitions
    )


@app.route("/add_exhibition")
def add_exhibition():
    return render_template("add_exhibition.html")


@app.route("/exhibitions", methods=["POST"])
def exhibitions():
    return render_template(
        "exhibitions.html"
    )
