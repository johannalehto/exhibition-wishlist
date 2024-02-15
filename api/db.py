from os import getenv

from flask_sqlalchemy import SQLAlchemy

from api.app import app

database_url = getenv("DATABASE_URL")
if database_url.startswith("postgres://"):
    database_url = database_url.replace("postgres://", "postgresql://", 1)
app.config["SQLALCHEMY_DATABASE_URI"] = database_url


db = SQLAlchemy(app)
