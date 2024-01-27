from flask import Flask

app = Flask(__name__)


def create


@app.route("/")
def index():
    return render_template("index.html")


@app.route/("/add_exhibition")
def add_exhibition():
    return render_template("add_exhibition.html")


@app.route/("/display_exhibitions" methods=["POST"])
def display_exhibitions():
    return render_template(
        "exhibitions.html",
        exhibition_name=request.form["exhibition_name"],
        museum_name=request.form["museum_name"],
        start_date=request.form["start_date"],
        end_date=request.form["end_date"]
    )