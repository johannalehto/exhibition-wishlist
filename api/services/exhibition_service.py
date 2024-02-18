from flask import flash, request
from sqlalchemy import text

from api.db import db


def get_museums() -> list:
    sql = text("SELECT museum_name FROM museums ORDER BY museum_name")
    result = db.session.execute(sql)
    museums = result.fetchall()
    return [museum[0] for museum in museums]


def get_exhibitions():
    sql = text(
        """
        SELECT e.exhibition_name, e.start_date, e.end_date, m.museum_name
        FROM exhibitions e
        JOIN museums m ON e.museum_id = m.id
    """
    )
    result = db.session.execute(sql)
    all_exhibitions = result.fetchall()
    return all_exhibitions


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


def check_missing_fields():
    required_fields = ["exhibition_name", "museum_name", "start_date", "end_date"]

    missing_fields = [
        field.replace("_", " ").capitalize()
        for field in required_fields
        if not request.form.get(field, "").strip()
    ]
    if missing_fields:
        flash(f'Please fill in: {", ".join(missing_fields)}')
        return True
    return False


def create_new_exhibition(
    exhibition_name,
    museum_name,
    start_date,
    end_date,
):

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

    db.session.execute(sql, new_exhibition)
    db.session.commit()

    return True, "Added exhibition succesfully"
